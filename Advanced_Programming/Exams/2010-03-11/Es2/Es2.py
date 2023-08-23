from scheduler import *

if __name__ == "__main__":
    pl = [process("one", 10), process("two", 3, 5), process("three", 15), \
          process("four", 30, 5), process("five", 10), process("six", 6, 10), \
          process("seven", 10), process("eight", 25, 5)]
    
    print("fifo scheduling")
    s = scheduler(pl, fifo)
    s.scheduling()
    print("round-robin scheduling")
    s = scheduler(pl, round_robin)
    s.scheduling()