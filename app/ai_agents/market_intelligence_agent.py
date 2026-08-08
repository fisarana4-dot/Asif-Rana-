from app.ai_gateway import gateway

class MarketIntelligenceAgent:
    def analyze_market(self, market):
        return gateway.process('openai', market)

market_agent = MarketIntelligenceAgent()
