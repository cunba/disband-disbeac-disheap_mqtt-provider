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


# def disbandActionDisbandIdAmbientNoise(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     disbandMeasureInformationPayload = DisbandMeasureInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(disbandMeasureInformationPayload))


# def disbandActionDisbandIdHeartRate(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     disbandMeasureInformationPayload = DisbandMeasureInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(disbandMeasureInformationPayload))


# def disbandActionDisbandIdHumidity(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     disbandMeasureInformationPayload = DisbandMeasureInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(disbandMeasureInformationPayload))


# def disbandActionDisbandIdLightning(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     disbandMeasureInformationPayload = DisbandMeasureInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(disbandMeasureInformationPayload))


# def disbandActionDisbandIdOxygen(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     disbandMeasureInformationPayload = DisbandMeasureInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(disbandMeasureInformationPayload))


# def disbandActionDisbandIdPressure(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     disbandMeasureInformationPayload = DisbandMeasureInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(disbandMeasureInformationPayload))


# def disbandActionDisbandIdTemperature(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     disbandMeasureInformationPayload = DisbandMeasureInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(disbandMeasureInformationPayload))


# def disbandsActionUserIdPair(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     pairDisbandInformationPayload = PairDisbandInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(pairDisbandInformationPayload))


# def disbeacActionUserIdPair(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     pairDisbeacInformationPayload = PairDisbeacInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(pairDisbeacInformationPayload))


# def disbeacActionDisbeacIdLocation(client, userdata, msg):
#     jsonString = msg.payload.decode('utf-8')
#     logging.info('Received json: ' + jsonString)
#     disbeacLocationInformationPayload = DisbeacLocationInformationPayload.from_json(jsonString)
#     logging.info('Received message: ' + str(disbeacLocationInformationPayload))








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
    
    # disbandActionDisbandIdAmbientNoiseMessenger = Messaging(config, 'disbands/action/*/ambient-noise', disbandActionDisbandIdAmbientNoise)
    # disbandActionDisbandIdAmbientNoiseMessenger.loop_start()
    # disbandActionDisbandIdHeartRateMessenger = Messaging(config, 'disbands/action/*/heart-rate', disbandActionDisbandIdHeartRate)
    # disbandActionDisbandIdHeartRateMessenger.loop_start()
    # disbandActionDisbandIdHumidityMessenger = Messaging(config, 'disbands/action/*/humidity', disbandActionDisbandIdHumidity)
    # disbandActionDisbandIdHumidityMessenger.loop_start()
    # disbandActionDisbandIdLightningMessenger = Messaging(config, 'disbands/action/*/lightning', disbandActionDisbandIdLightning)
    # disbandActionDisbandIdLightningMessenger.loop_start()
    # disbandActionDisbandIdOxygenMessenger = Messaging(config, 'disbands/action/+/oxygen', disbandActionDisbandIdOxygen)
    # disbandActionDisbandIdOxygenMessenger.loop_start()
    # disbandActionDisbandIdPressureMessenger = Messaging(config, 'disbands/action/+/pressure', disbandActionDisbandIdPressure)
    # disbandActionDisbandIdPressureMessenger.loop_start()
    # disbandActionDisbandIdTemperatureMessenger = Messaging(config, 'disbands/action/+/temperature', disbandActionDisbandIdTemperature)
    # disbandActionDisbandIdTemperatureMessenger.loop_start()
    # disbandsActionUserIdPairMessenger = Messaging(config, 'disbands/action/+/pair', disbandsActionUserIdPair)
    # disbandsActionUserIdPairMessenger.loop_start()
    # disbeacActionUserIdPairMessenger = Messaging(config, 'disbeacs/action/+/pair', disbeacActionUserIdPair)
    # disbeacActionUserIdPairMessenger.loop_start()
    # disbeacActionDisbeacIdLocationMessenger = Messaging(config, 'disbeacs/action/+/location', disbeacActionDisbeacIdLocation)
    # disbeacActionDisbeacIdLocationMessenger.loop_start()

    # Example of how to publish a message. You will have to add arguments to the constructor on the next line:
    # payload = DisbandSyncInformationPayload()
    # payloadJson = payload.to_json()

    while (True):
        topic = str(EventTopics.DISBAND_EVENT_DISBAND_MAC_VIBRATE)
        topic.format(disbandMac = '4')
        # disband_event_disband_id_vibrate_topic='disbands/action/{disbandMac}/vibrate'
        # disband_event_disband_id_vibrate_topic.format(disbandMac = str(4))
        disband_event_disband_id_vibrate.publish(topic, True)
        print()
        time.sleep(1)

if __name__ == '__main__':
    main()

