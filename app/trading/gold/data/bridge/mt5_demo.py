class MT5DemoBridge:
    def status(self): return "READY"
    def load_csv(self,p):
        import csv
        return list(csv.DictReader(open(p)))
