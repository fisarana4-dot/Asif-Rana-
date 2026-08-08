


import csv

class DataLoader:
    def load(self, path):
        with open(path, newline="") as f:
            return list(csv.DictReader(f))

data_loader = DataLoader()