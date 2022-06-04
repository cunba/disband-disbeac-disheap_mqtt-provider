from utils.timestamp import Timestamp
from models.messaging import Messaging
from payloads.disband_sync_information_payload import DisbandSyncInformationPayload

class DisbandEventSync:
    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, measures):
        payload = DisbandSyncInformationPayload(measures, Timestamp().get_now_timestamp_miliseconds())
        return payload.to_json()

    def public_sync(self, measures):
        payloadJson = self.create_payload(measures)
        self.action.publish(self.topic, payloadJson)