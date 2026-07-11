# GitHub Copilot Instructions for NEXRA V16000

## 🎯 Primary Directive

Before generating ANY code, read and follow:
1. `docs/MASTER_CONTEXT_PACK.md` - Foundation document
2. `docs/ARCHITECTURE.md` - System architecture
3. All ADR documents in `docs/ADR/`

---

## 🏗️ Architecture Principles

### Non-Negotiable Rules

#### 1. **Schema-First Architecture**
- ✅ Define Pydantic models BEFORE writing business logic
- ✅ Use strongly-typed schemas for all data structures
- ✅ Version all schema changes
- ❌ Never use untyped dictionaries or `Any` types

**Example:**
```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class TradeDecisionRequest(BaseModel):
    """Schema-first: Define structure before logic"""
    pair: str = Field(..., pattern="^[A-Z]{6}$")
    quantity: float = Field(..., gt=0)
    risk_level: str = Field(..., regex="^(high|medium|low)$")
    timestamp: datetime = Field(default_factory=datetime.utcnow)
```

#### 2. **Production-First Engineering**
- ✅ Every feature must be production-ready on day one
- ✅ No experimental code in main branch
- ✅ All code must handle failures gracefully
- ❌ No TODO or FIXME comments in production code

#### 3. **Human Governance Mandatory**
- ✅ High-risk decisions require human approval
- ✅ All decisions must be logged immutably
- ✅ AI provides recommendations, NOT commands
- ❌ Never bypass human authority
- ❌ Never auto-execute high-risk actions

**Example:**
```python
# ✅ CORRECT: AI recommends, human decides
class TradeRecommendation(BaseModel):
    action: str  # "BUY" or "SELL"
    confidence: float  # 0.0 to 1.0
    reasoning: str  # Explainable
    requires_approval: bool = True  # High-risk = mandatory approval

# Execute only after human approval
if recommendation.requires_approval:
    approval = await get_human_approval(recommendation)
    if not approval.approved:
        return {"status": "rejected", "reason": approval.reason}
```

#### 4. **Event-Driven Architecture**
- ✅ Publish immutable events for every state change
- ✅ Never modify events after creation
- ✅ Every event has: event_id, event_type, aggregate_id, timestamp, correlation_id
- ❌ No direct state mutations without events

**Example:**
```python
from dataclasses import dataclass
from uuid import uuid4
from datetime import datetime

@dataclass(frozen=True)  # Immutable
class TradeDecisionApprovedEvent:
    event_id: str = Field(default_factory=lambda: str(uuid4()))
    event_type: str = "trade_decision_approved"
    aggregate_id: str  # Decision ID
    correlation_id: str  # Request tracking
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    payload: dict  # Immutable details
    version: int = 1

# Store event immutably
await event_store.append(TradeDecisionApprovedEvent(...))
```

#### 5. **Immutable Audit Trails**
- ✅ Log every decision, who made it, when, and why
- ✅ Use event sourcing for historical replay
- ✅ Audit logs must be tamper-proof
- ❌ Never delete audit records
- ❌ Never modify historical decisions

**Example:**
```python
# ✅ CORRECT: Immutable audit entry
class AuditLog(BaseModel):
    id: UUID
    action: str
    actor: str  # User or system
    resource: str
    timestamp: datetime
    details: dict
    # No update/delete allowed
```

#### 6. **Backward Compatibility**
- ✅ Never break existing APIs without migration period
- ✅ Support deprecated fields for minimum 2 versions
- ✅ Version all endpoints: `/api/v1/`, `/api/v2/`, etc.
- ❌ No sudden schema changes

#### 7. **Minimal Technical Debt**
- ✅ Code review MUST happen before merge
- ✅ Tests MUST pass (80% coverage minimum)
- ✅ Type checks MUST pass
- ❌ No workarounds or hacks
- ❌ No commented-out code

---

## 🔐 Security Requirements

### Always Implement:
- ✅ **JWT Authentication** - Stateless, expiring tokens
- ✅ **RBAC** - Role-based access control
- ✅ **Secrets Management** - Environment variables only
- ✅ **Encryption in Transit** - HTTPS/TLS always
- ✅ **Encryption at Rest** - Database encryption enabled
- ✅ **Input Validation** - Pydantic validators
- ✅ **Rate Limiting** - Prevent abuse
- ✅ **Dependency Scanning** - Regular security audits

### Never:
- ❌ Hardcode secrets or credentials
- ❌ Use `eval()` or `exec()` on user input
- ❌ Trust user input without validation
- ❌ Expose system details in error messages
- ❌ Allow SQL injection (use parameterized queries)

---

## 🏛️ Domain-Driven Design

### Structure:
```
src/
├── domains/
│   ├── trading/
│   │   ├── schemas.py      # Data structures
│   │   ├── models.py       # Domain models
│   │   ├── repositories.py # Data access
│   │   ├── services.py     # Business logic
│   │   └── events.py       # Domain events
│   ├── approval/
│   ├── decision_memory/
│   └── multi_agent/
├── api/
│   └── routes/             # API endpoints only
└── events/
    └── handlers/           # Event processing
```

### Rules:
- ✅ Business logic ONLY in domains
- ✅ API routes ONLY call domain services
- ✅ Repositories ONLY handle data access
- ❌ No business logic in controllers
- ❌ No database queries in API routes

---

## 🤖 Multi-Agent Guidelines

### Agents CAN:
- ✅ Analyze market data
- ✅ Score opportunities
- ✅ Recommend actions with reasoning
- ✅ Explain their recommendations
- ✅ Suggest risk levels

### Agents CANNOT:
- ❌ Execute trades directly
- ❌ Approve their own recommendations
- ❌ Modify audit logs
- ❌ Override human decisions
- ❌ Access production data for training

**Example:**
```python
class GoldTradingAgent:
    async def analyze_market(self, market_data: MarketData) -> Recommendation:
        """✅ Agent analyzes, doesn't execute"""
        signal = self.calculate_signal(market_data)
        confidence = self.assess_confidence(signal)
        
        return Recommendation(
            action="BUY",
            confidence=confidence,
            reasoning="...",
            requires_approval=True  # ← Human must approve
        )

# ✅ Correct: Human approval required
approval = await approval_gateway.request_approval(recommendation)
if approval.approved:
    await decision_executor.execute(recommendation)
```

---

## 📊 Decision Lifecycle

Every decision MUST follow this flow:

```
1. Create Request
   ↓
2. Collect Context (gather relevant data)
   ↓
3. Run Agents (analyze, score, recommend)
   ↓
4. Calculate Risk (determine approval requirement)
   ↓
5. Human Approval (if required)
   ↓
6. Execute Decision (if approved)
   ↓
7. Store in Decision Memory (immutable record)
   ↓
8. Feedback Loop (learn from outcomes)
```

**Every step must be logged and auditable.**

---

## 🧪 Testing Requirements

### Minimum Coverage: 80%

### Required Tests:
- ✅ Unit tests for all business logic
- ✅ Integration tests for repositories
- ✅ API endpoint tests
- ✅ Security tests (OWASP)
- ✅ Event store tests
- ✅ Approval workflow tests

**Example:**
```python
@pytest.mark.asyncio
async def test_high_risk_decision_requires_approval():
    """Verify human approval is mandatory"""
    decision = create_high_risk_decision()
    
    with pytest.raises(ApprovalRequiredError):
        await decision_executor.execute(decision, approval=None)

@pytest.mark.asyncio
async def test_event_is_immutable():
    """Verify events cannot be modified"""
    event = TradeDecisionEvent(...)
    
    with pytest.raises(FrozenInstanceError):
        event.payload = {"new": "data"}
```

---

## 📝 Code Quality Standards

### Before Every Commit:

1. **Type Checking**
   ```bash
   mypy src/ --strict
   ```

2. **Linting**
   ```bash
   flake8 src/
   pylint src/
   ```

3. **Security Scanning**
   ```bash
   bandit -r src/
   safety check
   ```

4. **Tests**
   ```bash
   pytest tests/ --cov=src --cov-fail-under=80
   ```

### Requirements:
- ✅ No type errors
- ✅ No linting violations
- ✅ No security vulnerabilities
- ✅ 80%+ test coverage
- ✅ Code review approval

---

## 🚀 Production Deployment

### Mandatory Pipeline:

```
Feature Branch
    ↓
Pull Request (code review)
    ↓
Development Environment (automated tests)
    ↓
Staging Environment (integration tests)
    ↓
Production Release (with rollback plan)
```

### Rules:
- ✅ All tests must pass
- ✅ Code review required
- ✅ Security scan passed
- ✅ Approval from maintainer
- ✅ Deployment logged in audit trail
- ❌ No direct production commits
- ❌ No skipping CI/CD pipeline

---

## 🎨 Code Generation Guidelines

### When Generating Code, ALWAYS:

1. **Start with schema** → Define Pydantic models first
2. **Add type hints** → Every parameter and return value
3. **Add docstrings** → Explain purpose and usage
4. **Add error handling** → Gracefully handle failures
5. **Add logging** → Structured logs for debugging
6. **Add tests** → Unit tests included
7. **Add security** → No hardcoded secrets, input validation
8. **Add governance** → Human approval where needed

### Never Generate:
- ❌ Code without type hints
- ❌ Functions without docstrings
- ❌ API endpoints without validation
- ❌ Database queries without migrations
- ❌ Code that bypasses security or governance
- ❌ Unlogged side effects

---

## 📚 Document References

- **Architecture:** `docs/ARCHITECTURE.md`
- **ADRs:** `docs/ADR/` (Architecture Decision Records)
- **API Docs:** `docs/API.md`
- **Contributing:** `CONTRIBUTING.md`
- **Master Context:** `docs/MASTER_CONTEXT_PACK.md`

---

## ❓ When In Doubt

1. Read `docs/MASTER_CONTEXT_PACK.md`
2. Check relevant ADR documents
3. Review existing code in the domain
4. Ask for human review (never guess)

---

**Last Updated:** 2026-07-11

**Version:** 1.0

**Owner:** Asif Rana, Pakistan

**These instructions apply to all code generated for NEXRA V16000.**
