import logging
from models.messaging import Messaging

from payloads.disbeac_location_information_payload import DisbeacLocationInformationPayload
from repositories import LocationRepository
from python_client import LocationDisbeac
from python_client import LocationDisbeacDTO

class DisbeacActionDisbeacMacLocation:

    def __init__(self, config, topic, configBack):
        self.messenger = Messaging(config, topic, self.action)
        self.messenger.loop_start()
        self.repository = LocationRepository(configBack)
    
    def action(self, client, userdata, msg):
        jsonString = msg.payload.decode('utf-8')
        logging.info('Received json: ' + jsonString)
        disbeacLocationInformationPayload = DisbeacLocationInformationPayload.from_json(jsonString)
        self.save_data(disbeacLocationInformationPayload)

    def save_data(self, payload: DisbeacLocationInformationPayload):
        locationDTO = LocationDisbeacDTO(longitude = payload.longitude, latitude = payload.latitude, date = payload.sentAt, disbeac_mac = payload.disbeacMac)
        self.repository.save(locationDTO)