import threading
import time
from concurrent import futures


def process_b() -> None:
    print("Process B started")
    # while True:
    #     time.sleep(1)
    print("Process B finished")


class A:
    def process_a(self) -> None:
        print("Process A started")
        thread = threading.Thread(target=process_b, daemon=True)
        thread.start()
        print("START")
        thread.join()
        print("END")
        time.sleep(3)
        print("Process A finished")
        # thread.stop()


def main_1() -> None:
    a = A()
    threading.Thread(target=a.process_a, daemon=True).start()

    i = 0
    while True:
        print(f"active_count: {threading.active_count()}")
        time.sleep(1)
        i += 1
        if i == 5:
            break

def wait(a:str, b:int) -> None:
    print(f"sleep start {a}, {b}")
    time.sleep(1)
    print("sleep end")

class Main2:
    def __init__(self, num: int) -> None:
        pass
    
    def start(self, num: int) -> None:
        self.executor = futures.ThreadPoolExecutor(num)
        start = time.time()
        for i in range(3):
            print(f"submit start {i}")
            self.executor.submit(wait, a="x", b=123+i) 
            print(f"submit end {i}")

        self.executor.shutdown(wait=True)
        self.executor.shutdown(wait=True)
        print(f"{time.time() - start}")

def main_2() -> None:

    m = Main2(3)
    m.start(3)
    m.start(3)


if __name__ == "__main__":
    main_2()
