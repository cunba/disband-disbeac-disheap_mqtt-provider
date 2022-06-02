#!/usr/bin/env python3
import configparser
import logging
import time

from models.messaging import Messaging

from payloads.disband_mesured_information_payload import DisbandMesuredInformationPayload
from payloads.pair_disband_information_payload import PairDisbandInformationPayload
from payloads.pair_disbeac_information_payload import PairDisbeacInformationPayload
from payloads.disbeac_location_information_payload import DisbeacLocationInformationPayload
from payloads.disband_sync_information_payload import DisbandSyncInformationPayload
from payloads.disband_alarm_information_payload import DisbandAlarmInformationPayload
from payloads.disband_mesured_times_information_payload import DisbandMesuredTimesInformationPayload
from models.sent_at import SentAt


from python_client.openapi_client.configuration import Configuration
from repositories.login_repository import LoginRepository

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


def disbandActionDisbandIdAmbientNoise(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandMesuredInformationPayload))


def disbandActionDisbandIdHeartRate(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandMesuredInformationPayload))


def disbandActionDisbandIdHumidity(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandMesuredInformationPayload))


def disbandActionDisbandIdLightning(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandMesuredInformationPayload))


def disbandActionDisbandIdOxygen(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandMesuredInformationPayload))


def disbandActionDisbandIdPressure(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandMesuredInformationPayload))


def disbandActionDisbandIdTemperature(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbandMesuredInformationPayload = DisbandMesuredInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbandMesuredInformationPayload))


def disbandsActionUserIdPair(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    pairDisbandInformationPayload = PairDisbandInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(pairDisbandInformationPayload))


def disbeacActionUserIdPair(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    pairDisbeacInformationPayload = PairDisbeacInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(pairDisbeacInformationPayload))


def disbeacActionDisbeacIdLocation(client, userdata, msg):
    jsonString = msg.payload.decode('utf-8')
    logging.info('Received json: ' + jsonString)
    disbeacLocationInformationPayload = DisbeacLocationInformationPayload.from_json(jsonString)
    logging.info('Received message: ' + str(disbeacLocationInformationPayload))








def main():
    logging.basicConfig(level=logging.INFO)
    logging.info('Start of main.')
    config = getConfig()

    login(credentials_email, credentials_password)
    print(backend_configuration.access_token)

    # Creating the messaging for publications
    disbandEventDisbandIdSync = Messaging(config)
    disbandEventDisbandIdSyncAlarm = Messaging(config)
    disbeacEventDisbeacIdActiveDisbandId = Messaging(config)
    disbandEventDisbandIdVibrate = Messaging(config)

    # Subscribing to the topics
    disbandActionDisbandIdAmbientNoiseMessenger = Messaging(config, 'disband/action/*/ambient-noise', disbandActionDisbandIdAmbientNoise)
    disbandActionDisbandIdAmbientNoiseMessenger.loop_start()
    disbandActionDisbandIdHeartRateMessenger = Messaging(config, 'disband/action/*/heart-rate', disbandActionDisbandIdHeartRate)
    disbandActionDisbandIdHeartRateMessenger.loop_start()
    disbandActionDisbandIdHumidityMessenger = Messaging(config, 'disband/action/*/humidity', disbandActionDisbandIdHumidity)
    disbandActionDisbandIdHumidityMessenger.loop_start()
    disbandActionDisbandIdLightningMessenger = Messaging(config, 'disband/action/*/lightning', disbandActionDisbandIdLightning)
    disbandActionDisbandIdLightningMessenger.loop_start()
    disbandActionDisbandIdOxygenMessenger = Messaging(config, 'disband/action/+/oxygen', disbandActionDisbandIdOxygen)
    disbandActionDisbandIdOxygenMessenger.loop_start()
    disbandActionDisbandIdPressureMessenger = Messaging(config, 'disband/action/+/pressure', disbandActionDisbandIdPressure)
    disbandActionDisbandIdPressureMessenger.loop_start()
    disbandActionDisbandIdTemperatureMessenger = Messaging(config, 'disband/action/+/temperature', disbandActionDisbandIdTemperature)
    disbandActionDisbandIdTemperatureMessenger.loop_start()
    disbandsActionUserIdPairMessenger = Messaging(config, 'disbands/action/+/pair', disbandsActionUserIdPair)
    disbandsActionUserIdPairMessenger.loop_start()
    disbeacActionUserIdPairMessenger = Messaging(config, 'disbeac/action/+/pair', disbeacActionUserIdPair)
    disbeacActionUserIdPairMessenger.loop_start()
    disbeacActionDisbeacIdLocationMessenger = Messaging(config, 'disbeac/action/+/location', disbeacActionDisbeacIdLocation)
    disbeacActionDisbeacIdLocationMessenger.loop_start()

    # Example of how to publish a message. You will have to add arguments to the constructor on the next line:
    # payload = DisbandSyncInformationPayload()
    # payloadJson = payload.to_json()

    while (True):
        disbandEventDisbandIdVibrateTopic='disband/action/{disbandId}/vibrate'
        disbandEventDisbandIdVibrateTopic.format(disbandId = str(4))
        disbandEventDisbandIdVibrate.publish('disband/event/{disbandId}/vibrate', True)
        time.sleep(120)

if __name__ == '__main__':
    main()

