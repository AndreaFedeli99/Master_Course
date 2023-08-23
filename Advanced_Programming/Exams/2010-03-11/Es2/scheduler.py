class process:
    def __init__(self, id, time, duration=1):
        self.id = id
        self.time = time
        self.duration = duration
    def run(self):
        print(self.id)

class scheduler:
    def __init__(self, processes, alghorithm):
        self.alghorithm = alghorithm(processes)
    def scheduling(self):
        for p in self.alghorithm:
            p.run()

class fifo:
    def __init__(self, processes):
        self.ready_list = processes
    def __iter__(self):
        self.ready_list = sorted(self.ready_list, key=lambda p: p.time)
        return self
    def __next__(self):
        try:
            return self.ready_list.pop(0)
        except:
            raise StopIteration
    
class round_robin:
    def __init__(self, processes, quantum=2):
        self.ready_list = processes
        self.quantum = quantum
    def __iter__(self):
        p = min(self.ready_list, key=lambda p: p.time)
        self.t = p.time
        self.p_list = [p]
        return self
    def __next__(self):
        while len(self.ready_list) != 0:
            p_ids = set(p.id for p in self.p_list)
            try:
                p = self.p_list.pop(0)
            except:
                self.t += 1
                self.p_list.extend(sorted(filter(lambda pr: pr.time <= self.t and pr.id not in p_ids, self.ready_list), key=lambda p: p.time))
                continue
            self.p_list.extend(sorted(filter(lambda pr: pr.time <= (self.t + min(p.duration, self.quantum)) and pr.id not in p_ids, self.ready_list), key=lambda p: p.time))
            if p.duration > self.quantum:
                p.duration -= self.quantum
                self.t += self.quantum
                self.p_list.append(p)
            else:
                self.ready_list.remove(p)
                self.t += p.duration
            return p
        raise StopIteration
    