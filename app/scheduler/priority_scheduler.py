from queue import PriorityQueue
queue = PriorityQueue()
def enqueue(priority, job):
    queue.put((priority, job))
def dequeue():
    return queue.get()
def size():
    return queue.qsize()
