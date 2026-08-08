from app.trading.gold.core.mtf_engine import mtf_engine
from app.trading.gold.core.mtf_conflict import mtf_conflict
from app.trading.gold.core.trade_decision import trade_decision
class GoldStrategy:
    def run(self,d):
        bias=mtf_engine.bias(d)
        blocked=mtf_conflict.blocked(bias)
        return {"bias":bias,"blocked":blocked,"decision":trade_decision.decide({"blocked":blocked,"signal":d.get("signal","NO_TRADE")})}
strategy=GoldStrategy()
