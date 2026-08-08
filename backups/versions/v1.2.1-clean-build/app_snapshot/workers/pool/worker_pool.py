from multiprocessing import Process
from app.workers.consumer.loop import start
workers=[]
def create(count):
    for _ in range(count): workers.append(Process(target=start))
def start_all():
    for w in workers: w.start()
def stop_all():
    for w in workers: w.terminate()
