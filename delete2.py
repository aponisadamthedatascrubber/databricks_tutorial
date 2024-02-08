import time
import threading
import random

class TimeoutException(Exception):
    pass

def sleep_with_timeout(timeout):
    event = threading.Event()

    def sleeper():
        event.wait(timeout)
        if not event.is_set():
            print("Sleep exceeded timeout.")
            raise TimeoutException("STOP IN THE NAME OF LOVE!!!!")

    thread = threading.Thread(target=sleeper)
    thread.start()
    
    sleep_time = round(random.random()*5)
    print(f'sleep time: {sleep_time}')
    time.sleep(sleep_time)  # Simulatingpytho some blocking operation
    print('success')
    event.set()  # Set the event to unblock the sleeper thread

def main():
    timeout = 2  # Maximum duration allowed for the sleep
    while True:
        try:
            start_time = time.time()
            sleep_with_timeout(timeout)
            print(f'duration: {time.time() - start_time}')
        except TimeoutException as e:
            print("STOP IN THE NAME OF LOVE!")

if __name__ == "__main__":
    main()
    