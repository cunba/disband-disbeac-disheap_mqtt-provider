from models.messaging import Messaging

class DisbandEventVibrate:
    def __init__(self, config, topic):
        self.action = Messaging(config)
        self.topic = topic

    def public_sync(self):
        self.action.publish(self.topic, True)