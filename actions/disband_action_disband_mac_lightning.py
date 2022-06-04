import logging
from models.messaging import Messaging

from payloads.disband_lightning_information_payload import DisbandLightningInformationPayload
from repositories import LightningRepository
from python_client import Lightning
from python_client import LightningDTO

class DisbandActionDisbandMacLightning:

    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        print(str(client))
        print(str(userdata))
        print(str(msg))
        logging.info('Received json: ' + jsonString)
        disbandLightningInformationPayload = DisbandLightningInformationPayload.from_json(jsonString)
        logging.info('Received message: ' + str(disbandLightningInformationPayload))

    def save_data(self, disbandMac, payload):
        lightningDTO = LightningDTO(payload.get('data'), payload.get('date'), disbandMac)
        LightningRepository.save(lightningDTO)