AGING_FACTOR = 1
def increase_priority(p):
    return max(0, p - AGING_FACTOR)
