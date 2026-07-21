
from app.phase15.learning.adaptive_learning import AdaptiveLearning


def test_adaptive_learning():
    result = AdaptiveLearning().learn("experience")
    assert result["learning"] == "adapted"
