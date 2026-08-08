class WorkflowOrchestrator:

    def run(self, workflow):
        return {
            "workflow": workflow,
            "status": "executed"
        }
