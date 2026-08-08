from app.ai_gateway.provider_router import router

class AIGateway:
    def process(self, provider, request):
        selected = router.route(provider)
        return {'provider': selected, 'request': request}

gateway = AIGateway()
