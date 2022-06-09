import logging
from models.messaging import Messaging

from payloads.disband_lightning_information_payload import DisbandLightningInformationPayload
from repositories import LightningRepository
from python_client.disband.openapi_client.model.lightning import Lightning
from python_client.disband.openapi_client.model.lightning_dto import LightningDTO

class DisbandActionDisbandMacLightning:

    def __init__(self, config, topic, configBack):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
        self.repository = LightningRepository(configBack)
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        logging.info('Received json: ' + jsonString)
        disbandLightningInformationPayload = DisbandLightningInformationPayload.from_json(jsonString)
        self.save_data(disbandLightningInformationPayload)

    def save_data(self, payload: DisbandLightningInformationPayload):
        lightningDTO = LightningDTO(lightning = payload.lightning, red_lightning = payload.redLightning, green_lightning = payload.greenLightning, blue_lightning = payload.blueLightning, date =  payload.sentAt, disband_mac = payload.disbandMac)
        self.repository.save(lightningDTO)