import logging
from models.messaging import Messaging

from payloads.disband_mesured_information_payload import DisbandMesuredInformationPayload
from repositories import AmbientNoiseRepository
from python_client import AmbientNoise
from python_client import MeasureDTO

class DisbandActionDisbandIdAmbientNoise:

    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.disband_action_disband_id_ambient_noise)
        self.messenger.loop_start()
    
    def disband_action_disband_id_ambient_noise(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        print(str(client))
        print(str(userdata))
        print(str(msg))
        logging.info('Received json: ' + jsonString)
        disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
        logging.info('Received message: ' + str(disbandMesuredInformationPayload))

    def save_data(self, disbandId, payload):
        measureDTO = MeasureDTO(payload.get('data'), payload.get('date'), disbandId)
        AmbientNoiseRepository.save(measureDTO)