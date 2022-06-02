import logging
from models.messaging import Messaging

from payloads.disband_mesured_information_payload import DisbandMesuredInformationPayload

class DisbandActionDisbandIdAmbientNoise:

    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.disband_action_disband_id_ambient_noise)
        self.messenger.loop_start()
    
    
    def disband_action_disband_id_ambient_noise(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        logging.info('Received json: ' + jsonString)
        disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
        logging.info('Received message: ' + str(disbandMesuredInformationPayload))