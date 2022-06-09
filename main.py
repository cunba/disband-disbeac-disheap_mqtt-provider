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


from python_client.disheap.openapi_client.configuration import Configuration
from repositories import LoginRepository
from actions import *
from events import *
from utils.convert_mac import ConvertMac


backend_configuration = Configuration(host = "http://63.33.86.240:8080")
CREDENTIALS_EMAIL = 'ire.cunba@gmail.com'
CREDENTIALS_PASSWORD = '282629_Project'
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

    disbandMacToTopic = ConvertMac().mac_to_string(DISBAND_MAC)

    # Creating the messaging for publications

    topic = 'disbands/event/{disbandMac}/sync'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_event_sync = DisbandEventSync(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    topic = 'disbands/event/{disbandMac}/sync/alarm'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_event_sync = DisbandEventSyncAlarm(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    topic = 'disbands/event/{disbandMac}/sync/measure-times'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_event_sync = DisbandEventSyncMeasureTimes(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    topic = 'disbeacs/event/{disbeacMac}/active/{disbandMac}'
    topicFormat = topic.format(disbeacMac = '', disbandMac = disbandMacToTopic)
    disband_event_sync = DisbeacEventActive(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    topic = 'disbands/event/{disbandMac}/vibrate'
    topicFormat = topic.format(disbandMac = disbandMacToTopic)
    disband_event_sync = DisbandEventVibrate(config, topicFormat)
    print('Connected to publication topic: ', topicFormat)

    # Subscribing to the topics
    
    topic = 'disbands/action/+/ambient-noise'
    DisbandActionDisbandMacAmbientNoise(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbands/action/+/heart-rate'
    DisbandActionDisbandMacHeartRate(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbands/action/+/humidity'
    DisbandActionDisbandMacHumidity(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbands/action/+/lightning'
    DisbandActionDisbandMacLightning(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbands/action/+/oxygen'
    DisbandActionDisbandMacOxygen(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbands/action/+/pressure'
    DisbandActionDisbandMacPressure(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbands/action/+/temperature'
    DisbandActionDisbandMacTemperature(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbands/action/+/pair'
    DisbandActionUserIdPair(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbands/action/+/location'
    DisbeacActionDisbeacMacLocation(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    topic = 'disbeacs/action/+/pair'
    DisbeacActionUserIdPair(config, topic, backend_configuration)
    print('Subscribed to topic: ', topic)

    print()

    while (True):
        time.sleep(1)

if __name__ == '__main__':
    main()

