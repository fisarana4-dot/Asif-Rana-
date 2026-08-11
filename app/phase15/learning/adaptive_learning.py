import sqlite3
class AdaptiveLearning:
 def learn(self,e):
  c=sqlite3.connect("nexra_experience.db")
  c.execute("INSERT INTO experience(task) VALUES(?)",(e,));c.commit();return {"saved":True,"experience":e}
