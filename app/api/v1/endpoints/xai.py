from app.analytics.xai_engine import XAIEngine

def explain_decision(decision):
    engine = XAIEngine()
    return engine.explain(decision)
