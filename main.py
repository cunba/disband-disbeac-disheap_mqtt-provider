#!/usr/bin/env python3
import configparser
import logging
import time

from models.messaging import Messaging

from payloads.disband_measure_information_payload import DisbandMeasureInformationPayload
from payloads.pair_disband_information_payload import PairDisbandInformationPayload
from payloads.pair_disbeac_information_payload import PairDisbeacInformationPayload
from payloads.disbeac_location_information_payload import DisbeacLocationInformationPayload
from payloads.disband_sync_information_payload import DisbandSyncInformationPayload
from payloads.disband_alarm_information_payload import DisbandAlarmInformationPayload
from payloads.disband_measure_times_information_payload import DisbandMeasureTimesInformationPayload
from models.sent_at import SentAt


from python_client import Configuration
from repositories import LoginRepository
from utils.topics import ActionTopics
from actions import *
from events import *


backend_configuration = Configuration(host = "http://63.33.86.240:8080")
CREDENTIALS_EMAIL = 'ire.cunba@gmail.com'
CREDENTIALS_PASSWORD = '282629_Cunba'
DISBAND_MAC = 'C0:50:08:32:26:56'

def login(email, password):
    login_api = LoginRepository(backend_configuration)
    token = login_api.login(email, password)
    # Configure Bearer authorization (JWT): bearer
    backend_configuration.access_token = token


# Config has the connection properties.
def getConfig():
    configParser = configparser.ConfigParser()
    configParser.read('config.ini')
    config = configParser['DEFAULT']
    return config



def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Start of main.')
    config = getConfig()

    login(CREDENTIALS_EMAIL, CREDENTIALS_PASSWORD)

    # Creating the messaging for publications

    topic = 'disbands/event/{disbandMac}/sync'
    topicFormat = topic.format(disbandMac = DISBAND_MAC)
    disband_event_sync = DisbandEventSync(config, topicFormat)

    topic = 'disbands/event/{disbandMac}/sync/alarm'
    topicFormat = topic.format(disbandMac = DISBAND_MAC)
    disband_event_sync = DisbandEventSyncAlarm(config, topic)

    topic = 'disbands/event/{disbandMac}/sync/measure-times'
    topicFormat = topic.format(disbandMac = DISBAND_MAC)
    disband_event_sync = DisbandEventSyncMeasureTimes(config, topicFormat)

    topic = 'disbeacs/event/{disbeacMac}/active/{disbandMac}'
    topicFormat = topic.format(disbandMac = DISBAND_MAC)
    disband_event_sync = DisbeacEventActive(config, topic)

    topic = 'disbands/event/{disbandMac}/vibrate'
    topicFormat = topic.format(disbandMac = DISBAND_MAC)
    disband_event_sync = DisbandEventVibrate(config, topic)

    # Subscribing to the topics
    
    topic = ActionTopics.DISBAND_ACTION_AMBIENT_NOISE
    DisbandActionDisbandMacAmbientNoise(config, topic)

    topic = ActionTopics.DISBAND_ACTION_HEART_RATE
    DisbandActionDisbandMacHeartRate(config, topic)

    topic = ActionTopics.DISBAND_ACTION_HUMIDITY
    DisbandActionDisbandMacHumidity(config, topic)

    topic = ActionTopics.DISBAND_ACTION_LIGHTNING
    DisbandActionDisbandMacLightning(config, topic)

    topic = ActionTopics.DISBAND_ACTION_OXYGEN
    DisbandActionDisbandMacOxygen(config, topic)

    topic = ActionTopics.DISBAND_ACTION_PRESSURE
    DisbandActionDisbandMacPressure(config, topic)

    topic = ActionTopics.DISBAND_ACTION_TEMPERATURE
    DisbandActionDisbandMacTemperature(config, topic)

    topic = ActionTopics.DISBAND_ACTION_PAIR
    DisbandActionUserIdPair(config, topic)

    topic = ActionTopics.DISBEAC_ACTION_LOCATION
    DisbeacActionDisbeacMacLocation(config, topic)

    topic = ActionTopics.DISBAND_ACTION_AMBIENT_NOISE
    DisbeacActionUserIdPair(config, topic)

    while (True):
        time.sleep(1)

if __name__ == '__main__':
    main()

