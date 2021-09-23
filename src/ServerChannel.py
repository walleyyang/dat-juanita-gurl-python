import enum


class ServerChannel(enum.Enum):
    FLOW = 'flow'
    GOLDEN_SWEEPS = 'golden-sweeps'
    UNUSUAL_ACTIVITY = 'unusual-activity'
