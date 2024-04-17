import json
import logging


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        # print(f"record: {record.__dict__}")
        logging.Formatter.format(self, record)

        ret = {}
        for attr, value in record.__dict__.items():
            if attr == "levelno":
                continue
            if attr == "processName":
                continue
            if attr == "funcName":
                continue
            if attr == "lineno":
                continue
            if attr == "relativeCreated":
                continue
            if attr == "filename":
                continue
            if attr == "msecs":
                continue
            if attr == "module":
                continue
            if attr == "created":
                continue
            if attr == "created":
                continue
            if attr == "pathname":
                continue
            if attr == "args":
                continue
            if attr == "process":
                continue
            if attr == "thread":
                continue
            if attr == "threadName":
                continue

            if attr == "exc_info" and value is None:
                continue
            if attr == "exc_text" and value is None:
                continue
            if attr == "stack_info" and value is None:
                continue

            if attr == "asctime":
                value = self.formatTime(record)
            if attr == "exc_info" and value is not None:
                value = self.formatException(value)
            if attr == "stack_info" and value is not None:
                value = self.formatStack(value)

            if attr == "asctime":
                attr = "timestamp"
            if attr == "msg":
                attr = "message"
            if attr == "levelname":
                attr = "level"

            try:
                json.dumps(value)
            except Exception:
                value = str(value)

            ret[attr] = value

        return json.dumps(ret)
