import logging
from models.messaging import Messaging

from repositories import DisbeacRepository
from python_client import DisbeacDTO
from payloads.pair_disbeac_information_payload import PairDisbeacInformationPayload

class DisbeacActionUserIdPair:

    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        print(str(client))
        print(str(userdata))
        print(str(msg))
        logging.info('Received message: ' + msg.payload)
        pairDisbeacInformationPayload = PairDisbeacInformationPayload.from_json(jsonString)
        logging.info('Received message: ' + str(pairDisbeacInformationPayload))
        # self.save()


    def save(self, payload):
        disbeacDTO = DisbeacDTO(payload.get('mac'), payload.get('model'), payload.get('version'), payload.get('userId'))
        DisbeacRepository.save(disbeacDTO)