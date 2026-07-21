MAX_RETRIES = 3
def should_retry(count): return count < MAX_RETRIES
from .backoff import delay
