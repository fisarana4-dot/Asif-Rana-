import csv
class GoldDataLoader:
    def load(self,p):
        return [{k:(float(v) if k!="Date" else v) for k,v in r.items()} for r in csv.DictReader(open(p))]
data_loader=GoldDataLoader()
