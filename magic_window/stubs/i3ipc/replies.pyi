from .model import OutputMode as OutputMode, Rect as Rect
from typing import Any

class _BaseReply:
    ipc_data: Any = ...
    def __init__(self, data: Any) -> None: ...

class CommandReply(_BaseReply): ...
class WorkspaceReply(_BaseReply): ...
class OutputReply(_BaseReply): ...

class BarConfigGaps:
    left: Any = ...
    right: Any = ...
    top: Any = ...
    bottom: Any = ...
    def __init__(self, data: Any) -> None: ...

class BarConfigReply(_BaseReply): ...
class VersionReply(_BaseReply): ...
class ConfigReply(_BaseReply): ...
class TickReply(_BaseReply): ...
class InputReply(_BaseReply): ...
class SeatReply(_BaseReply): ...