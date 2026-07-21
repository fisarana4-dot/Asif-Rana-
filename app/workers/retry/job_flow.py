from .job_status import set_status
from .retry_manager import should_retry
from .dead_letter_queue import add
def start(job): set_status(job,"RUNNING")
from .retry_manager import fail
def success(job): set_status(job,"SUCCESS")
def failed(job): fail(job); set_status(job,"FAILED")
def send_dlq(job): add(job)
