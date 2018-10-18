import threading
import multithreading
import time

def loopdemo(x):
    for x in range(x):
        print("thread started")
        print(x)
        #time.sleep(2)
        print("thread completed")

for y in range(1):
    p= multithreading.Process(target=loopdemo(y))
    p.start()

    #threading.Thread(target=loopdemo(4,"thread 1")).start()
    #threading.Thread(target=loopdemo(5, "thread 2")).start()