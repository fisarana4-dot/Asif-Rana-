from app.scheduler.redis_queue import pop
from app.workers.retry.job_flow import success,failed
def run(): job=pop(); return job
