class RSIEngine:
    def value(self,prices,period=14):
        if len(prices)<=period: return None
        gains=[];losses=[]
        for i in range(1,len(prices)):
            change=prices[i]-prices[i-1];gains.append(max(change,0));losses.append(max(-change,0))
        avg_gain=sum(gains[:period])/period;avg_loss=sum(losses[:period])/period
        for i in range(period,len(gains)):
            avg_gain=(avg_gain*(period-1)+gains[i])/period;avg_loss=(avg_loss*(period-1)+losses[i])/period
        if avg_loss==0: return 100.0
        rs=avg_gain/avg_loss;return 100-(100/(1+rs))
rsi_engine=RSIEngine()
