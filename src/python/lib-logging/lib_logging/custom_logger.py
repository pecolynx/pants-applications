import logging
from collections.abc import MutableMapping
from typing import TYPE_CHECKING, Any

# https://github.com/python/typeshed/issues/7855
if TYPE_CHECKING:
    _LoggerAdapter = logging.LoggerAdapter[logging.Logger]
else:
    _LoggerAdapter = logging.LoggerAdapter


class CustomLogger(_LoggerAdapter):
    def process(
        self, msg: Any, kwargs: MutableMapping[str, Any]
    ) -> tuple[Any, MutableMapping[str, Any]]:
        extra = kwargs.get("extra")
        print(f"PROCESS, {extra}, {self.extra}")
        if extra and self.extra:
            kwargs.update(extra=dict(**extra, **self.extra))
        if extra is None and self.extra:
            kwargs.update(extra=self.extra)
        return msg, kwargs
