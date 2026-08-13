import importlib
def scan(): return importlib.import_module('app.trading.global.registry.assets').ASSETS
