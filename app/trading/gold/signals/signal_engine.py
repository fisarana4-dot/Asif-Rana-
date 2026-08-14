from ..risk.sl_guard import sl_ready
from ..risk.power_guard import power_safe
from .trade_filter import trade_filter


class GoldSignals:
    def generate(self,d): return [{"signal":d.get("signal","NO_TRADE")}]
    def score(self,d): return sum(d.get(x)=="BUY" for x in ["ema_trend","rsi_signal","vwma_signal"])
    def sell_score(self,d): return sum(d.get(x)=="SELL" for x in ["ema_trend","rsi_signal","vwma_signal"])
signals=GoldSignals()
def signal_decision(d): return "WAIT" if power_safe(d)=="BLOCK" else "WAIT" if trade_filter.evaluate(d)=="WAIT" else "WAIT" if d.get("execute") and not sl_ready(d) else "BUY" if signals.score(d)>signals.sell_score(d) else "SELL" if signals.sell_score(d)>signals.score(d) else "NO_TRADE"
