import logging
from models.messaging import Messaging

from repositories import DisbandRepository
from python_client import DisbandDTO
from payloads.pair_disband_information_payload import PairDisbandInformationPayload

class DisbandActionDisbandMacPair:

    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        print(str(client))
        print(str(userdata))
        print(str(msg))
        logging.info('Received message: ' + msg.payload)
        pairDisbandInformationPayload = PairDisbandInformationPayload.from_json(jsonString)
        logging.info('Received message: ' + str(pairDisbandInformationPayload))
        # self.save()


    def save(self, disbandMac, payload):
        disbandDTO = DisbandDTO(payload.get('model'), payload.get('version'), disbandMac)
        DisbandRepository.save(disbandDTO)