STATUS={}
def set_status(job,s): STATUS[job]=s
def get_status(job): return STATUS.get(job,"NEW")
