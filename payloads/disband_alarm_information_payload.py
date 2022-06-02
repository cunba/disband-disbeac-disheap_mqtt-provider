from enum import Enum
from typing import Sequence
from models.entity import Entity



class DisbandAlarmInformationPayload(Entity):

    def __init__(
            self,
            date: float,
            isRepetition: bool,
            repetitionWeekDays: str,
            sentAt: float):
        self.date = date
        self.isRepetition = isRepetition
        self.repetitionWeekDays = repetitionWeekDays
        self.sentAt = sentAt


