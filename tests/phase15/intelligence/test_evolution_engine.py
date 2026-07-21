from app.phase15.intelligence.evolution_engine import EvolutionEngine


def test_evolution_engine():
    engine = EvolutionEngine()
    result = engine.analyze("signal")

    assert result["evolution"
