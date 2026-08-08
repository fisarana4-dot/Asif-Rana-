import subprocess
def run():
 r=subprocess.run(["python","gold_vsa_bt.py"],capture_output=True,text=True)
 return r.stdout
