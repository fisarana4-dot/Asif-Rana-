from queue import PriorityQueue
pq = PriorityQueue()
def put(priority, job):
    pq.put((priority, job))
def get():
    return pq.get()
def empty():
    return pq.empty()
