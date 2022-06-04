from utils.timestamp import Timestamp
from models.messaging import Messaging
from payloads.disband_alarm_information_payload import DisbandAlarmInformationPayload

class DisbandEventSyncAlarm:
    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def create_payload(self, date, isRepetition, repetitionWeekDays):
        payload = DisbandAlarmInformationPayload(date, isRepetition, repetitionWeekDays, Timestamp().get_now_timestamp_miliseconds())
        return payload.to_json()

    def public_sync(self, date, isRepetition, repetitionWeekDays):
        payloadJson = self.create_payload(date, isRepetition, repetitionWeekDays)
        self.action.publish(self.topic, payloadJson)