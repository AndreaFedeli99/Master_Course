import threading
import queue
import time

def sleepsort(l):
    sleepsort.result = queue.Queue()
    def put_item(x):
        time.sleep(x * 0.001)
        sleepsort.result.put(x)
    
    for i in l:
        threading.Thread(target=put_item, args=[i]).start()
    print(' '.join([str(sleepsort.result.get()) for i in range(len(l))]))

if __name__ == "__main__":
    sleepsort([7, 2 ,100, 1, 9, 45, 2, 33, 7, 77, 25])
    sleepsort([333, 222 ,112, 777, 901, 455, 256, 313, 125, 625, 825, 999, 316])
    sleepsort([1000, 10, 10.5, 100, 22, 77, 700, 3.145, 2000, 150, 35, 287, 4, 7, 777, 2525, 255, 256, 25])