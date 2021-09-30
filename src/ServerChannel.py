import enum


class ServerChannel(enum.Enum):
    FLOW = 'flow'
    GOLDEN_SWEEPS = 'golden-sweeps'
    ALERTS = 'alerts'
