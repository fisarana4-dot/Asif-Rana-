from .priority_scheduler import enqueue, dequeue
def dispatch(priority, job):
    enqueue(priority, job)
def next_job():
    return dequeue()
