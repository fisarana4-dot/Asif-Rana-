import time
def is_num(v): return isinstance(v,(int,float))
def is_num(v): return isinstance(v,(int,float))
def is_fresh(t,h=24): return (time.time()-t)/3600<=h
def is_trusted(s,a): return any(d in s for d in a)
print('Validator OK')
