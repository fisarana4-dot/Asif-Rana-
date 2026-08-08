class GoldDataLoader:
    def load(self,p):
        with open(p,newline='') as f:return list(csv.DictReader(f))
data_loader=GoldDataLoader()
