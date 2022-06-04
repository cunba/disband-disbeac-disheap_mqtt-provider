import logging
from models.messaging import Messaging

from payloads.disbeac_location_information_payload import DisbeacLocationInformationPayload
from repositories import LocationRepository
from python_client import LocationDisbeac
from python_client import LocationDisbeacDTO

class DisbeacActionDisbeacMacLocation:

    def __init__(self, config, topic):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        print(str(client))
        print(str(userdata))
        print(str(msg))
        logging.info('Received json: ' + jsonString)
        disbeacLocationInformationPayload = DisbeacLocationInformationPayload.from_json(jsonString)
        logging.info('Received message: ' + str(disbeacLocationInformationPayload))

    def save_data(self, disbeacMac, payload):
        locationDTO = LocationDisbeacDTO(payload.get('data'), payload.get('date'), disbeacMac)
        LocationRepository.save(locationDTO)