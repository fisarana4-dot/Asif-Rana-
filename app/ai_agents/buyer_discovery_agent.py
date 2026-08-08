from app.ai_gateway import gateway

class BuyerDiscoveryAgent:
    def find_buyers(self, market):
        return gateway.process('openai', market)

buyer_agent = BuyerDiscoveryAgent()
