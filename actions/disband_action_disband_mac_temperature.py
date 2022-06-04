import logging
from models.messaging import Messaging

from payloads.disband_measure_information_payload import DisbandMeasureInformationPayload
from repositories import TemperatureRepository
from python_client import Temperature
from python_client import MeasureDTO

class DisbandActionDisbandMacTemperature:

    def __init__(self, config, topic, configBack):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
        self.repository = TemperatureRepository(configBack)
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        logging.info('Received json: ' + jsonString)
        disbandMeasureInformationPayload = DisbandMeasureInformationPayload.from_json(jsonString)
        self.save_data(disbandMeasureInformationPayload)

    def save_data(self, payload: DisbandMeasureInformationPayload):
        measureDTO = MeasureDTO(payload.data, payload.sentAt, payload.disbandMac)
        self.repository.save(measureDTO)