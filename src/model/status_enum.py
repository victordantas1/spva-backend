from enum import Enum

class StatusEnum(Enum):
    SENT = 'sent'
    ANALYSE = 'analyse'
    REJECTED = 'rejected'
    ACCEPTED = 'accepted'
