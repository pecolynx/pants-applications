import logging
from collections.abc import MutableMapping
from typing import Any


class CustomLogger(logging.LoggerAdapter[logging.Logger]):
    def process(
        self, msg: Any, kwargs: MutableMapping[str, Any]
    ) -> tuple[Any, MutableMapping[str, Any]]:
        extra = kwargs.get("extra")
        if extra and self.extra:
            kwargs.update(extra=dict(**extra, **self.extra))
        return msg, kwargs
