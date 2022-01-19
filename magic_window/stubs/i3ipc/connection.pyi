from ._private import (
    EventType as EventType,
    MessageType as MessageType,
    PubSub as PubSub,
    Synchronizer as Synchronizer,
)
from .con import Con as Con
from .events import (
    BarconfigUpdateEvent as BarconfigUpdateEvent,
    BindingEvent as BindingEvent,
    Event as Event,
    InputEvent as InputEvent,
    IpcBaseEvent as IpcBaseEvent,
    ModeEvent as ModeEvent,
    OutputEvent as OutputEvent,
    ShutdownEvent as ShutdownEvent,
    TickEvent as TickEvent,
    WindowEvent as WindowEvent,
    WorkspaceEvent as WorkspaceEvent,
)
from .replies import (
    BarConfigReply as BarConfigReply,
    CommandReply as CommandReply,
    ConfigReply as ConfigReply,
    InputReply as InputReply,
    OutputReply as OutputReply,
    SeatReply as SeatReply,
    TickReply as TickReply,
    VersionReply as VersionReply,
    WorkspaceReply as WorkspaceReply,
)
from typing import Any, Callable, List, Optional, Union

class Connection:
    subscriptions: int = ...
    def __init__(
        self, socket_path: Optional[Any] = ..., auto_reconnect: bool = ...
    ) -> None: ...
    @property
    def socket_path(self) -> str: ...
    @property
    def auto_reconnect(self) -> bool: ...
    def command(self, payload: str) -> List[CommandReply]: ...
    def get_version(self) -> VersionReply: ...
    def get_bar_config(self, bar_id: str = ...) -> Optional[BarConfigReply]: ...
    def get_bar_config_list(self) -> List[str]: ...
    def get_outputs(self) -> List[OutputReply]: ...
    def get_inputs(self) -> List[InputReply]: ...
    def get_seats(self) -> List[SeatReply]: ...
    def get_workspaces(self) -> List[WorkspaceReply]: ...
    def get_tree(self) -> Con: ...
    def get_marks(self) -> List[str]: ...
    def get_binding_modes(self) -> List[str]: ...
    def get_config(self) -> ConfigReply: ...
    def send_tick(self, payload: str = ...) -> TickReply: ...
    def off(self, handler: Callable[[Connection, IpcBaseEvent], None]) -> Any: ...
    def on(
        self,
        event: Union[Event, str],
        handler: Callable[[Connection, IpcBaseEvent], None],
    ) -> Any: ...
    def main(self, timeout: float = ...) -> Any: ...
    def main_quit(self) -> None: ...
