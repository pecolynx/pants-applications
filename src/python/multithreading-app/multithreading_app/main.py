import threading
import time


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


def main() -> None:
    a = A()
    threading.Thread(target=a.process_a, daemon=True).start()

    i = 0
    while True:
        print(f"active_count: {threading.active_count()}")
        time.sleep(1)
        i += 1
        if i == 10:
            break


if __name__ == "__main__":
    main()
