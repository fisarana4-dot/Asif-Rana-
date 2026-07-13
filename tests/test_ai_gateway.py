import pytest
import respx
import httpx
from httpx import Response
from app.services.ai_gateway_service import AIGatewayService

@pytest.mark.asyncio
async def test_successful_api_parsing():
    """Verifies that reasoning tags and JSON structures are successfully separated."""
    service = AIGatewayService()
    raw_mock_resp = "<think>Analyzing user risk parameters.</think>\n{\"status\": \"approved\", \"score\": 95}"
    
    reasoning, decision = service.parse_response(raw_mock_resp)
    
    assert reasoning == "Analyzing user risk parameters."
    assert decision["status"] == "approved"
    assert decision["score"] == 95

@pytest.mark.asyncio
@respx.mock
async def test_retry_on_timeout_and_fallback():
    """Simulates persistent network timeouts to verify retry triggers and ultimate safety fallback."""
    service = AIGatewayService(api_url="https://mockai.com", timeout=1.0)
    
    # Configure mock route to simulate continuous request time-outs
    respx.post("https://mockai.com").mock(side_effect=httpx.TimeoutException("Connection dropped"))
    
    # Execution should not crash; it must cleanly execute retries and drop to fallback
    reasoning, decision = await service.generate_decision("Evaluate local storage health", retries=2)
    
    assert "offline backup node" in reasoning
    assert decision["source"] == "local_mock"
    assert decision["status"] == "success"
