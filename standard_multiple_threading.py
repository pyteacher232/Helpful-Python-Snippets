import threading

threads = []
max_threads = 100
input_dt = []

def func_1(param1):
    pass

while threads or input_dt:
    for thread in threads:
        if not thread.is_alive():
            threads.remove(thread)

    while len(threads) < max_threads and input_dt:
        thread = threading.Thread(target=func_1, args=("sub",))
        thread.setDaemon(True)
        thread.start()
        threads.append(thread)