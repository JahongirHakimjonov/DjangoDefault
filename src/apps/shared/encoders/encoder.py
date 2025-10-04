import json
from typing import Any


class PrettyJSONEncoder(json.JSONEncoder):
    def __init__(
        self,
        *args: Any,
        indent: int = 4,
        sort_keys: bool = True,
        **kwargs: Any,
    ) -> None:
        """
        JSONEncoder с предустановленным красивым форматированием.
        Параметры indent и sort_keys можно переопределить при необходимости.
        """
        super().__init__(*args, indent=indent, sort_keys=sort_keys, **kwargs)
