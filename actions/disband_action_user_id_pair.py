import logging
import uuid
from models.messaging import Messaging

from repositories import DisbandRepository
from python_client import DisbandDTO
from payloads.pair_disband_information_payload import PairDisbandInformationPayload

class DisbandActionUserIdPair:

    def __init__(self, config, topic, configBack):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
        self.repository = DisbandRepository(configBack)
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        logging.info('Received message: ' + jsonString)
        pairDisbandInformationPayload = PairDisbandInformationPayload.from_json(jsonString)
        self.save(pairDisbandInformationPayload)


    def save(self, payload: PairDisbandInformationPayload):
        disbandDTO = DisbandDTO(str(payload.mac), str(payload.model), str(payload.version), str(payload.userId))
        self.repository.save(disbandDTO)