from app.ai_gateway import gateway

class ProductResearchAgent:
    def research_product(self, product):
        return gateway.process('openai', product)

product_agent = ProductResearchAgent()
