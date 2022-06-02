from enum import Enum
from typing import Sequence
from models.entity import Entity



class PairDisbeacInformationPayload(Entity):

    def __init__(
            self,
            userId: str,
            disbandId: str,
            sentAt: float):
        self.userId = userId
        self.disbandId = disbandId
        self.sentAt = sentAt


