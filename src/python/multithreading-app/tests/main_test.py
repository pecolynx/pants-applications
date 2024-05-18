import threading
import time

from multithreading_app.main import A


def test_a():
    a = A()
    threading.Thread(target=a.process_a, daemon=True).start()

    time.sleep(3)
    # assert False
