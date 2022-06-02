from enum import Enum
from typing import Sequence
from models.entity import Entity



class PairDisbandInformationPayload(Entity):

    def __init__(
            self,
            userId: str,
            sentAt: float):
        self.userId = userId
        self.sentAt = sentAt


