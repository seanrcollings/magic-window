from enum import Enum
from typing import Any

class MessageType(Enum):
    COMMAND: int = ...
    GET_WORKSPACES: int = ...
    SUBSCRIBE: int = ...
    GET_OUTPUTS: int = ...
    GET_TREE: int = ...
    GET_MARKS: int = ...
    GET_BAR_CONFIG: int = ...
    GET_VERSION: int = ...
    GET_BINDING_MODES: int = ...
    GET_CONFIG: int = ...
    SEND_TICK: int = ...
    GET_INPUTS: int = ...
    GET_SEATS: int = ...

class ReplyType(Enum):
    COMMAND: int = ...
    WORKSPACES: int = ...
    SUBSCRIBE: int = ...
    OUTPUTS: int = ...
    TREE: int = ...
    MARKS: int = ...
    BAR_CONFIG: int = ...
    VERSION: int = ...
    BINDING_MODES: int = ...
    GET_CONFIG: int = ...
    TICK: int = ...

class EventType(Enum):
    WORKSPACE: Any = ...
    OUTPUT: Any = ...
    MODE: Any = ...
    WINDOW: Any = ...
    BARCONFIG_UPDATE: Any = ...
    BINDING: Any = ...
    SHUTDOWN: Any = ...
    TICK: Any = ...
    INPUT: Any = ...
    def to_string(self): ...
    @staticmethod
    def from_string(val: Any): ...
    def to_list(self): ...
