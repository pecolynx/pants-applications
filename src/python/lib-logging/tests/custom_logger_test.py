import logging

from lib_logging.custom_logger import CustomLogger


def test_a(caplog) -> None:  # type: ignore[no-untyped-def]
    logger_a = logging.getLogger(__name__)
    logger_a.warning("WARNING 1")
    logger_a.warning("WARNING 2", extra={"field_b": "FIELD_B"})

    assert len(caplog.records) == 2

    assert caplog.record_tuples[0] == ("tests.custom_logger_test", logging.WARNING, "WARNING 1")

    assert caplog.record_tuples[1] == ("tests.custom_logger_test", logging.WARNING, "WARNING 2")
    assert caplog.records[1].field_b == "FIELD_B"


def test_b(caplog) -> None:  # type: ignore[no-untyped-def]
    logger_a = logging.getLogger(__name__)
    logger_b = CustomLogger(logger=logger_a, extra={"field_a": "FIELD_A"})
    logger_b.warning("WARNING 1")
    logger_b.warning("WARNING 2", extra={"field_b": "FIELD_B"})

    assert len(caplog.records) == 2

    assert caplog.record_tuples[0] == ("tests.custom_logger_test", logging.WARNING, "WARNING 1")
    assert caplog.records[0].field_a == "FIELD_A"

    assert caplog.record_tuples[1] == ("tests.custom_logger_test", logging.WARNING, "WARNING 2")
    assert caplog.records[1].field_a == "FIELD_A"
    assert caplog.records[1].field_b == "FIELD_B"


# def test_a(caplog) -> None:
#     formatter = JsonFormatter("%(asctime)s")
#     log_handler = logging.StreamHandler()
#     log_handler.setFormatter(formatter)

#     # logging.basicConfig(handlers=[log_handler], level=logging.INFO, force=True)
#     # logging.basicConfig(handlers=[log_handler], level=logging.INFO)
#     # logging.basicConfig(level=logging.INFO, force=True)

#     caplog.set_level(logging.INFO)
#     logger_a = logging.getLogger(__name__)
#     logger_b = CustomLogger(logger_a, extra={"field_a": "FIELD_A"})
#     logger_b.warning("TEST")
#     logger_b.warning("TEST", extra={"field_b": "FIELD_B"})
#     # logger_b.warning("TEST")
#     print(f"caplog: {caplog.records}")
#     assert caplog.records[0].field_a == "FIELD_A"
#     assert caplog.record_tuples == [("tests.custom_logger_test", logging.WARNING, "TEST")]

#     # assert caplog.text == "TEST"

#     # assert caplog.record_tuples == [("root", logging.INFO, "boo arg")]

#     assert False
