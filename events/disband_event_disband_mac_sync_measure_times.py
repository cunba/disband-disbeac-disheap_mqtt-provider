from utils.timestamp import Timestamp
from models.messaging import Messaging
from payloads.disband_measure_times_information_payload import DisbandMeasureTimesInformationPayload

class DisbandEventSyncMeasureTimes:
    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, sensors):
        payload = DisbandMeasureTimesInformationPayload(sensors, Timestamp().get_now_timestamp_miliseconds())
        return payload.to_json()

    def public_sync(self, sensors):
        payloadJson = self.create_payload(sensors)
        self.action.publish(self.topic, payloadJson)