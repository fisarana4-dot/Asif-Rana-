from app.trading.gold.indicators.ema_engine import ema_engine
from app.trading.gold.indicators.rsi_engine import rsi_engine
from app.trading.gold.indicators.atr_engine import atr_engine
from app.trading.gold.indicators.vwma_engine import vwma_engine
from app.trading.gold.indicators.volume_ma import volume_ma
from app.trading.gold.indicators.fibonacci_engine import fibonacci_engine
from app.trading.gold.indicators.trendline_engine import trendline_engine
from app.trading.gold.indicators.rsi_divergence_engine import rsi_divergence_engine
from app.trading.gold.indicators.obv_divergence_engine import obv_divergence_engine
class GoldIndicators:
    def ema200(self,prices): return ema_engine.ema(prices,200)
    def rsi(self,prices,period=14): return rsi_engine.value(prices,period)
    def atr(self,high,low,close,period=14): return atr_engine.value(high,low,close,period)
    def vwma(self,prices,volume,period=20): return vwma_engine.value(prices,volume,period)
    def volume_ma(self,volume,period=20): return volume_ma.value(volume,period)
    def fibonacci(self,high,low): return fibonacci_engine.levels(high,low)
    def trendline(self,prices): return trendline_engine.detect(prices)
    def rsi_divergence(self,prices,rsi): return rsi_divergence_engine.detect(prices,rsi)
    def obv_divergence(self,prices,obv): return obv_divergence_engine.detect(prices,obv)
indicators=GoldIndicators()
