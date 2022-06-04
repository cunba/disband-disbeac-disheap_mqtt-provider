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
from actions import DisbandActionDisbandIdAmbientNoise
from utils.topics import ActionTopics, EventTopics
from actions import *


backend_configuration = Configuration(host = "http://63.33.86.240:8080")
credentials_email = 'ire.cunba@gmail.com'
credentials_password = '282629_Cunba'

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

    login(credentials_email, credentials_password)

    # Creating the messaging for publications
    disband_event_disband_id_sync = Messaging(config)
    disband_event_disband_id_sync_Alarm = Messaging(config)
    disbeac_event_disbeac_id_active_disband_id = Messaging(config)
    disband_event_disband_id_vibrate = Messaging(config)

    # Subscribing to the topics

    DisbandActionDisbandIdAmbientNoise(config, ActionTopics.DISBAND_ACTION_AMBIENT_NOISE)
    DisbandActionDisbandIdHeartRate(config, ActionTopics.DISBAND_ACTION_HEART_RATE)

    while (True):
        time.sleep(1)

if __name__ == '__main__':
    main()

