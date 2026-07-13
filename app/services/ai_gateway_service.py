import re
import json
import asyncio
import httpx
from app.core.logging import logger

class AIGatewayService:
    def __init__(self, api_url: str = "https://api.openai.com/v1", timeout: float = 10.0):
        self.api_url = api_url
        self.timeout = timeout

    def parse_response(self, text: str) -> tuple[str, dict]:
        # Extract reasoning tags <think>...</think>
        reasoning = ""
        think_match = re.search(r"<think>(.*?)</think>", text, re.DOTALL)
        if think_match:
            reasoning = think_match.group(1).strip()
        
        # Extract JSON part (outside the think tags)
        clean_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
        try:
            decision = json.loads(clean_text)
        except json.JSONDecodeError:
            decision = {"status": "error", "message": "Failed to parse json"}
        
        return reasoning, decision

    async def generate_decision(self, prompt: str, retries: int = 2) -> tuple[str, dict]:
        payload = {
            "model": "deepseek-reasoning",
            "messages": [{"role": "user", "content": prompt}]
        }
        
        for attempt in range(retries + 1):
            try:
                logger.info(f"AI Gateway attempt {attempt + 1}...")
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    response = await client.post(
                        f"{self.api_url}/chat/completions",
                        json=payload
                    )
                    response.raise_for_status()
                    data = response.json()
                    raw_text = data["choices"][0]["message"]["content"]
                    return self.parse_response(raw_text)
            except (httpx.HTTPError, httpx.TimeoutException) as e:
                logger.warning(f"Attempt {attempt + 1} failed: {e}")
                if attempt < retries:
                    await asyncio.sleep(0.1)  # brief wait before retry
                else:
                    logger.error("All retries exhausted. Dropping to local fallback...")
        
        # Local Safety Fallback
        fallback_reasoning = "Network failure. Dropped to offline backup node."
        fallback_decision = {
            "source": "local_mock",
            "status": "success",
            "action": "HOLD"
        }
        return fallback_reasoning, fallback_decision
