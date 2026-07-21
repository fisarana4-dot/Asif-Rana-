MAX_JOBS_PER_WORKER = 100
def can_accept(count):
    return count < MAX_JOBS_PER_WORKER
