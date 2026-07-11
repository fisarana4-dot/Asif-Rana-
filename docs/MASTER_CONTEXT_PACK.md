# NEXRA V16000 – MASTER CONTEXT PACK v1.0

## Project Identity

**Project Name:** NEXRA V16000

**Full Name:** NEXRA V16000 – Enterprise AI Decision Operating System (EDOS)

**Owner:** Asif Rana, Pakistan

**Mission Statement:** Build a production-grade AI Decision Operating System that helps humans make better, safer and auditable decisions across:

- Gold Trading Intelligence (XAUUSD)
- Amazon Business Intelligence
- Export Decision Operating System (EDOS)
- Multi-Agent Decision Systems
- Human Governance and Approval
- Decision Memory and Knowledge Engine
- Future Digital Twins

---

## Core Philosophy

### Principle 1
**AI is a reasoning engine, not the final authority.**

### Principle 2
**Human approval is mandatory for high-risk decisions.**

### Principle 3
**Every decision must be explainable and auditable.**

### Principle 4
**Production-first engineering.**

### Principle 5
**Schema-first architecture.**

### Principle 6
**Backward compatibility.**

### Principle 7
**Minimal technical debt.**

---

## Non-Negotiable Engineering Rules

- ✅ Strong typing everywhere
- ✅ Pydantic schemas first
- ✅ Repository pattern
- ✅ Domain-driven design
- ✅ Event-driven architecture
- ✅ Immutable audit logs
- ✅ Structured logging
- ✅ Automated testing
- ✅ Security by default
- ❌ No business logic inside API routes
- ❌ No direct database access from controllers
- ❌ No hidden side effects

---

## Technology Stack

### Current Stack
- **Language:** Python 3.11
- **Web Framework:** FastAPI
- **Database:** PostgreSQL
- **Cache:** Redis
- **Message Queue:** RabbitMQ
- **Container:** Docker
- **CI/CD:** GitHub Actions

### Future Stack
- LangGraph
- Vector Database
- Digital Twins
- Kubernetes
- Analytics Platform

---

## System Domains

### Domain 1: Gold Trading Intelligence
**Responsibilities:**
- Market data ingestion
- Trading signals
- Risk scoring
- Trade recommendations
- Performance analytics

**Rules:**
- AI recommendations are advisory only
- Human approval required for execution

### Domain 2: Amazon Business Intelligence
**Responsibilities:**
- Product research
- Opportunity scoring
- Keyword intelligence
- Market analysis
- Competitor analysis

### Domain 3: Export Decision Operating System
**Responsibilities:**
- Trade compliance
- Import/export analysis
- Tariff intelligence
- Risk assessment
- Business recommendations

### Domain 4: Multi-Agent Orchestration
**Responsibilities:**
- Agent registry
- Agent communication
- Consensus engine
- Failure handling
- Task routing

### Domain 5: Human Authority Gateway
**Responsibilities:**
- Risk-based approvals
- Escalation workflows
- Approval audit trails
- Human override capabilities

### Domain 6: Decision Memory
**Responsibilities:**
- Store every decision
- Store reasoning
- Store outcomes
- Learn from history
- Support explainability

---

## Decision Lifecycle

```
Create Request
    ↓
Collect Context
    ↓
Run Agents
    ↓
Calculate Risk
    ↓
Human Approval (if required)
    ↓
Execute Decision
    ↓
Store Decision Memory
    ↓
Feedback Loop & Continuous Improvement
```

---

## Architecture Style

**Primary Architecture:**
- Modular Monolith

**Future Evolution:**
```
Modular Monolith
    ↓
Distributed Services
    ↓
Enterprise Platform
```

**Important:** Microservices are NOT allowed until justified by measurable bottlenecks.

---

## Repository Structure

```
project-root/
├── docs/
│   ├── MASTER_CONTEXT_PACK.md
│   └── ARCHITECTURE.md
├── src/
│   ├── domains/
│   ├── schemas/
│   ├── repositories/
│   ├── services/
│   ├── api/
│   └── events/
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── docker/
├── config/
├── scripts/
├── migrations/
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/
└── README.md
```

---

## Security Requirements

- ✅ JWT authentication
- ✅ Role-based access control (RBAC)
- ✅ Secrets in environment variables (never in code)
- ✅ Encryption at rest
- ✅ Encryption in transit (TLS/HTTPS)
- ✅ Immutable audit trails
- ✅ Dependency scanning
- ✅ Security testing
- ✅ OWASP compliance

---

## Observability Requirements

- **Structured Logs:** JSON format with correlation IDs
- **Metrics:** Prometheus-compatible metrics
- **Tracing:** Distributed tracing with correlation IDs
- **Health Checks:** Readiness and liveness probes
- **Error Monitoring:** Real-time error tracking and alerts
- **Audit Dashboards:** Decision and approval dashboards

---

## Database Principles

**PostgreSQL is the source of truth.**

### Rules:
- ✅ Use migrations (Alembic or similar)
- ❌ Never edit production tables manually
- ✅ Prefer JSONB for evolving schemas
- ✅ Maintain backward compatibility
- ✅ Version all schema changes

---

## Event Principles

**Events are immutable.**

### Every event must contain:
```python
{
    "event_id": "uuid",
    "event_type": "string",
    "aggregate_id": "uuid",
    "correlation_id": "uuid",
    "timestamp": "ISO8601",
    "payload": "object",
    "version": "integer"
}
```

---

## Multi-Agent Principles

### Agents CAN:
- ✅ Analyze data
- ✅ Recommend actions
- ✅ Score options
- ✅ Explain reasoning

### Agents CANNOT:
- ❌ Directly execute decisions
- ❌ Bypass humans
- ❌ Modify audit logs
- ❌ Change historical decisions

---

## Human Governance Rules

### Risk-Based Approval Matrix:

| Risk Level | Approval Required | Auto-Approve Allowed |
|-----------|------------------|-------------------|
| High Risk | Mandatory | ❌ No |
| Medium Risk | Policy Based | ❓ Conditional |
| Low Risk | Optional | ✅ Yes |

**Immutable Rule:** Humans always have override authority.

---

## Production Rules

- ❌ No direct deployment to production
- ✅ Required pipeline:

```
Development
    ↓
Testing
    ↓
Staging
    ↓
Production
```

- ✅ All deployments tracked in audit logs
- ✅ Rollback capability maintained
- ✅ Health checks before production release

---

## Code Quality Standards

### Minimum Test Coverage:
- **Overall:** 80%
- **Critical Paths:** 95%

### Every Pull Request Requires:
- ✅ Unit tests
- ✅ Type checks (mypy/pyright)
- ✅ Linting (flake8/pylint)
- ✅ Security scan (bandit/safety)
- ✅ Architecture review
- ✅ Code review approval

---

## Long-Term Vision

**NEXRA V16000 will become:**

An Enterprise AI Decision Operating System capable of supporting thousands of users and mission-critical business decisions with:

- ✅ Complete explainability
- ✅ Full governance and oversight
- ✅ Human-in-the-loop architecture
- ✅ Real-time decision analytics
- ✅ Multi-tenant support
- ✅ Enterprise SLA compliance
- ✅ Industry-leading security and auditability

---

## Document References

Related documents for comprehensive understanding:

- `docs/ARCHITECTURE.md` - System architecture deep dive
- `docs/ADR/` - Architecture Decision Records
- `docs/API.md` - API specifications
- `.github/copilot-instructions.md` - AI agent guidelines
- `CONTRIBUTING.md` - Development guidelines

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-11 | Asif Rana | Initial Master Context Pack |

---

**Last Updated:** 2026-07-11

**Next Review:** 2026-08-11

**Owner:** Asif Rana, Pakistan
