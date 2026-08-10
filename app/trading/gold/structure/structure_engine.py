from .bos_engine import bos_engine
from .choch_engine import choch_engine
def analyze(d): return {"bos":bos_engine.detect(d),"choch":choch_engine.detect(d)}
structure_engine=type("StructureEngine",(),{"analyze":staticmethod(analyze)})()
