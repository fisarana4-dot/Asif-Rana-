from app.phase14.orchestration.workflow_orchestrator import WorkflowOrchestrator

def test_orchestration():
    result = WorkflowOrchestrator().run("flow")
    assert result["status"] == "executed"

