from enum import Enum

class ActionTopics(Enum):
    # SUBCRIPTIONS
    DISBAND_ACTION_AMBIENT_NOISE = 'disbands/action/+/ambient-noise'
    DISBAND_ACTION_HEART_RATE = 'disbands/action/+/heart-rate'
    DISBAND_ACTION_HUMIDITY = 'disbands/action/+/humidity'
    DISBAND_ACTION_LIGHTNING = 'disbands/action/+/lightning'
    DISBAND_ACTION_OXYGEN = 'disbands/action/+/oxygen'
    DISBAND_ACTION_PRESSURE = 'disbands/action/+/pressure'
    DISBAND_ACTION_TEMPERATURE = 'disbands/action/+/temperature'
    DISBAND_ACTION_PAIR = 'disbands/action/+/pair'
    DISBEAC_ACTION_PAIR = 'disbeacs/action/+/pair'
    DISBEAC_ACTION_LOCATION = 'disbands/action/+/location'

class EventTopics(Enum):
    # PUBLICATIONS
    DISBAND_EVENT_DISBAND_MAC_SYNC = 'disbands/event/{disbandMac}/sync'
    DISBAND_EVENT_DISBAND_MAC_SYNC_ALARM = 'disbands/event/{disbandMac}/sync/alarm'
    DISBAND_EVENT_DISBAND_MAC_SYNC_MEASURE_TIMES = 'disbands/event/{disbandMac}/sync/measure-times'
    DISBEAC_EVENT_DISBEAC_MAC_ACTIVE_DISBAND_MAC = 'disbeacs/event/{disbeacMac}/active/{disbandMac}'
    DISBAND_EVENT_DISBAND_MAC_VIBRATE = 'disbands/event/{disbandMac}/vibrate'