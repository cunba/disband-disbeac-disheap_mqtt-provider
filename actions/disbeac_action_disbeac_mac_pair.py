import logging
from models.messaging import Messaging

from repositories import HumidityRepository
from python_client import DisbeacDTO
from payloads.pair_disbeac_information_payload import PairDisbeacInformationPayload

class DisbeacActionDisbeacMacPair:

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


    def save(self, DisbeacMac, payload):
        disbeacDTO = DisbeacDTO(payload.get('model'), payload.get('version'), DisbeacMac)
        HumidityRepository.save(disbeacDTO)