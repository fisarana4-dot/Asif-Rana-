from app.ai_agents.buyer_discovery_agent import buyer_agent
from app.ai_agents.market_intelligence_agent import market_agent
from app.ai_agents.product_research_agent import product_agent
from app.decision.decision_engine import decision_engine
from app.export_intelligence.export_analyzer import export_engine
from app.reports.export_report import report_engine
class BusinessOrchestrator:
    def analyze(self,request):
        results={'buyer':buyer_agent.find_buyers(request),'market':market_agent.analyze_market(request),'product':product_agent.research_product(request)}
        results['export']=export_engine.analyze(request,'Dubai')
        results['report']=report_engine.generate(request)
        return decision_engine.evaluate(results)
orchestrator=BusinessOrchestrator()
