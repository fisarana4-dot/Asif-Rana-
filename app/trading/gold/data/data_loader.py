import csv
class GoldDataLoader:
    def load(self,p):
        return list(csv.DictReader(open(p)))
data_loader=GoldDataLoader()
