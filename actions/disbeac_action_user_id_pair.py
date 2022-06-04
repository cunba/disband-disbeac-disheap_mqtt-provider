import logging
from models.messaging import Messaging

from repositories import DisbeacRepository
from python_client import DisbeacDTO
from payloads.pair_disbeac_information_payload import PairDisbeacInformationPayload

class DisbeacActionUserIdPair:

    def __init__(self, config, topic, configBack):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
        self.repository = DisbeacRepository(configBack)
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        logging.info('Received message: ' + msg.payload)
        pairDisbeacInformationPayload = PairDisbeacInformationPayload.from_json(jsonString)
        self.save(pairDisbeacInformationPayload)


    def save(self, payload: PairDisbeacInformationPayload):
        disbeacDTO = DisbeacDTO(payload.mac, payload.model, payload.version, payload.userId, date = payload.sentAt)
        self.repository.save(disbeacDTO)