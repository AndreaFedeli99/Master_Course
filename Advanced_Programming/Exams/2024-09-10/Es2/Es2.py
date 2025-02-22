from asynchronous import asynchronous

import time

@asynchronous
def call_me(n):
    time.sleep(10)
    return n * n

if __name__ == "__main__":
    result = call_me.start(12)

    for i in range(20):
        if result.is_done():
            print(f"[{i}]: {result.get_result()}")
        else:
            print(f"{[i]}: not ready yet")
        time.sleep(1)
    
    result = call_me.start(10)
    try:
        print(result.get_result())
    except asynchronous.NotDoneYetException as ex:
        print(ex.message)