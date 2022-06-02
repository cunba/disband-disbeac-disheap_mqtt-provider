from enum import Enum
from typing import Sequence
from models.entity import Entity



class PairDisbeacInformationPayload(Entity):

    def __init__(
            self,
            userId: str,
            disbandMac: str,
            sentAt: float):
        self.userId = userId
        self.disbandMac = disbandMac
        self.sentAt = sentAt


