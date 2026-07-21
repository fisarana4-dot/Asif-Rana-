from app.phase15.intelligence.evolution_engine import EvolutionEngine

def test_evolution_engine():
    result = EvolutionEngine().analyze("signal")
    assert result["evolution"] == "processed"
