from typing import Any

class Synchronizer:
    display: Any = ...
    screen: Any = ...
    root: Any = ...
    sync_atom: Any = ...
    send_window: Any = ...
    def __init__(self) -> None: ...
    def sync(self) -> None: ...
