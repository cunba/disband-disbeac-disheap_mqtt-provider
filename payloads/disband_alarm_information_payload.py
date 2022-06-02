from enum import Enum
from typing import Sequence
from models.entity import Entity



class DisbandAlarmInformationPayload(Entity):

    def __init__(
            self,
            date: float,
            sentAt: float):
        self.date = date
        self.sentAt = sentAt


