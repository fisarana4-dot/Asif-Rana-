# NEXRA V16000 – Enterprise AI Decision Operating System

## Architecture Overview

NEXRA V16000 is a production-grade **Enterprise AI Decision Operating System (EDOS)** designed for:

- **Gold Trading Intelligence** (XAUUSD)
- **Amazon Business Intelligence**
- **Export Decision Operating System** (EDOS)
- **Multi-Agent Orchestration**
- **Human-in-the-Loop Governance**

**Core Principle:** AI is a reasoning layer, not final authority. All high-risk decisions require human approval.

---

## Mission Statement

Build a scalable, event-driven, schema-first Enterprise AI Decision Operating System that:

1. Provides intelligent decision support across multiple business domains
2. Maintains human governance for all business-critical decisions
3. Tracks decision history and audit trails
4. Integrates with external data sources (market data, business systems)
5. Supports future Digital Twins and advanced orchestration

---

## Technology Stack

### Core Technologies
- **Language:** Python 3.11
- **API Framework:** FastAPI
- **Database:** PostgreSQL
- **Cache/Queue:** Redis
- **Message Broker:** RabbitMQ
- **Containerization:** Docker
- **CI/CD:** GitHub Actions

### Future Technologies
- **Agent Orchestration:** LangGraph
- **Vector Search:** Vector Database (Pinecone/Weaviate/Milvus)
- **Orchestration:** Kubernetes
- **Monitoring:** Prometheus + Grafana

---

## Architectural Principles

### 1. Schema-First Architecture
- All data structures defined before implementation
- Database-agnostic domain models
- Type safety through Pydantic V2

### 2. Production-First Engineering
- Security by default (no exceptions)
- Backward compatibility always maintained
- Strong typing throughout codebase
- Comprehensive error handling

### 3. Event-Driven Architecture
- All state changes are events
- Event sourcing for audit trails
- RabbitMQ for event distribution
- Redis for event caching

### 4. Domain-Driven Design
- Clear domain boundaries
- Repository pattern for data access
- Service layer for business logic
- Domain events for cross-boundary communication

### 5. Repository Pattern
- Abstract data access layer
- Interchangeable storage backends
- Testable business logic
- No infrastructure coupling

### 6. Human Governance for High-Risk Decisions
- Trading decisions require CEO approval
- Governance rules engine
- Audit logging for all decisions
- Decision memory for learning

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                   External Data Sources                      │
│  (Market Data, Amazon APIs, Export Systems, Trading APIs)   │
└────────────────────┬────────────────────────────────────────┘
                     │
        ┌────────────▼─────────────┐
        │   API Gateway / Router    │
        │  (FastAPI + Auth Layer)   │
        └────────────┬──────────────┘
                     │
      ┌──────────────┼──────────────┐
      │              │              │
   ┌──▼────┐    ┌───▼────┐    ┌───▼────┐
   │ Agent  │    │ Decision│   │ Market  │
   │ Layer  │    │ Engine  │   │ Monitor │
   └────┬───┘    └───┬────┘    └────┬───┘
        │            │             │
   ┌────▼────────────▼─────────────▼────┐
   │    Event Bus (RabbitMQ/Redis)       │
   └────┬──────────────────────────────┬─┘
        │                              │
   ┌────▼──────────┐         ┌────────▼──┐
   │ Governance    │         │ Decision  │
   │ Rules Engine  │         │ Memory    │
   └────┬──────────┘         └────┬──────┘
        │                        │
   ┌────▼────────────────────────▼────┐
   │   Human Authority Gateway         │
   │  (CEO/Admin Approval)             │
   └────┬─────────────────────────────┘
        │
   ┌────▼──────────────────────────────┐
   │  Data Layer (PostgreSQL + Redis)   │
   │  - Decision Records                │
   │  - Audit Logs                      │
   │  - Agent State                     │
   │  - Trading History                 │
   └────────────────────────────────────┘
```

---

## Core Components

### 1. Human Authority Gateway
**Responsibility:** Gate-keeper for all high-risk decisions

- Decision approval workflow
- Role-based access control (RBAC)
- Approval chain management
- Audit trail logging
- Rejection/modification workflows

**Key Services:**
- `AuthorityService` - Manages approval flows
- `RoleService` - RBAC management
- `AuditService` - Logs all decisions

### 2. Multi-Agent Foundation
**Responsibility:** Orchestrate intelligent agents across domains

**Agent Types:**
- **Trading Agent** - XAUUSD market analysis
- **Amazon Agent** - Business intelligence
- **Export Agent** - Export decision support
- **Monitor Agent** - System health monitoring

**Agent Lifecycle:**
```
Initialize → Analyze → Reason → Propose Decision → Wait for Human Approval
                                         ↓
                        Human Reviews & Approves/Rejects
                                         ↓
                        Execute Approved Decision / Log Rejection
```

### 3. Event Bus
**Responsibility:** Central nervous system for all events

- **Event Types:**
  - `AgentStateChanged`
  - `DecisionProposed`
  - `DecisionApproved`
  - `DecisionRejected`
  - `TradeExecuted`
  - `ErrorOccurred`

- **Properties:**
  - Event sourcing capabilities
  - Temporal ordering
  - Domain tracking
  - User attribution

### 4. Decision Memory & Knowledge Engine
**Responsibility:** Learn from decisions and outcomes

**Decision Record:**
```python
{
  "id": "uuid",
  "agent_id": "trading-agent-001",
  "domain": "XAUUSD",
  "proposal": {...},
  "reasoning": "...",
  "human_decision": "approved|rejected|modified",
  "approved_by": "asif.rana@nexra.com",
  "executed_at": "timestamp",
  "outcome": "...",
  "impact": "...",
  "learned_at": "timestamp"
}
```

### 5. Observability & Monitoring
**Responsibility:** System health and performance tracking

- **Metrics:**
  - Decision latency
  - Approval rate
  - Agent accuracy
  - Error rates

- **Logs:**
  - Structured logging
  - Correlation IDs
  - Request tracing
  - Audit trails

- **Alerts:**
  - Threshold breaches
  - Anomaly detection
  - Agent failures
  - Authority gateway issues

### 6. Audit System
**Responsibility:** Complete decision trail for compliance

**Audit Log Entry:**
```python
{
  "timestamp": "iso8601",
  "actor": "user_id|agent_id",
  "action": "decision_proposed|approved|rejected|executed",
  "resource": "decision_id",
  "old_state": {},
  "new_state": {},
  "reason": "...",
  "ip_address": "...",
  "user_agent": "..."
}
```

### 7. Governance Rules Engine
**Responsibility:** Enforce business and security policies

**Rule Types:**
- **Trading Rules:** Min/max lot size, daily limit, volatility constraints
- **Approval Rules:** CEO-only decisions, escalation procedures
- **Security Rules:** IP whitelisting, rate limiting, MFA requirements
- **Audit Rules:** What must be logged, retention policies

---

## Data Layer Architecture

### PostgreSQL Schema Layers

#### 1. Governance Layer
```sql
- users (id, email, role, active)
- roles (id, name, permissions)
- approval_workflows (id, domain, steps, active)
```

#### 2. Decision Layer
```sql
- decisions (id, agent_id, domain, proposal, status)
- decision_approvals (id, decision_id, approver_id, status, reason)
- decision_outcomes (id, decision_id, result, impact, learned_at)
```

#### 3. Agent Layer
```sql
- agents (id, name, type, domain, config, active)
- agent_states (id, agent_id, state, last_update)
- agent_performance (id, agent_id, accuracy, latency, error_rate)
```

#### 4. Audit Layer
```sql
- audit_logs (id, timestamp, actor, action, resource, details)
- error_logs (id, timestamp, component, error, stack_trace)
- system_events (id, timestamp, event_type, details)
```

#### 5. Trading Layer
```sql
- trades (id, symbol, volume, price, direction, status)
- trade_history (id, trade_id, event, timestamp)
- market_data (id, symbol, timestamp, ohlcv)
```

### Redis Cache Layers
- **Agent State Cache** - Current agent configurations
- **Decision Proposals Cache** - Pending approvals (TTL: 24h)
- **Market Data Cache** - Real-time quotes (TTL: 1m)
- **User Session Cache** - Active sessions (TTL: 8h)

---

## Event Flow Example: Trading Decision

```
1. Market Monitor detects XAUUSD spike (>2%)
        ↓
2. Trading Agent analyzes market (multi-timeframe)
        ↓
3. Agent proposes: "Buy 10 lots at current price"
        ↓
4. Decision Event → Event Bus
        ↓
5. Governance Rules validate: ✓ Within limits
        ↓
6. Decision Memory scores: ✓ Similar past decisions 85% success
        ↓
7. Event → Human Authority Gateway
        ↓
8. CEO receives notification + detailed analysis
        ↓
9. CEO approves/rejects
        ↓
10. Execution Event → Trading System OR Rejection logged
        ↓
11. Outcome tracked for future learning
```

---

## API Contract

### Decision Request
```python
POST /api/v1/decisions/propose

{
  "agent_id": "trading-agent-001",
  "domain": "XAUUSD",
  "decision_type": "trade",
  "proposal": {
    "action": "buy",
    "instrument": "XAUUSD",
    "volume": 10,
    "entry_price": 2150.50
  },
  "reasoning": "Market broke above key resistance...",
  "confidence": 0.87,
  "risk_score": 0.23
}
```

### Decision Approval
```python
POST /api/v1/decisions/{decision_id}/approve

{
  "approved_by": "asif.rana@nexra.com",
  "approval_reason": "Market analysis is sound",
  "modifications": null
}
```

### Decision Query
```python
GET /api/v1/decisions?domain=XAUUSD&status=approved&days=7

Response: [
  {
    "id": "uuid",
    "agent_id": "...",
    "domain": "XAUUSD",
    "status": "approved",
    "proposed_at": "...",
    "approved_at": "...",
    "executed_at": "...",
    "outcome": "..."
  }
]
```

---

## Security Architecture

### Authentication & Authorization
- **JWT Tokens** for API authentication
- **RBAC** for role-based access control
- **MFA** for sensitive operations
- **OAuth 2.0** for third-party integrations

### Data Security
- **Encryption at Rest** (PostgreSQL)
- **Encryption in Transit** (TLS 1.3)
- **Secrets Management** (GitHub Secrets / HashiCorp Vault)
- **Audit Logging** (All data access)

### API Security
- **Rate Limiting** (Redis-based)
- **CORS** (Whitelist only)
- **HTTPS** (Mandatory)
- **Request Validation** (Pydantic)
- **SQL Injection Prevention** (ORM-based queries)

### Operational Security
- **Container Security** (Signed images)
- **Network Segmentation** (VPC / Private subnets)
- **Dependency Scanning** (Regular updates)
- **SAST/DAST** (GitHub Actions automated)

---

## Deployment Architecture

### Development Environment
```
Developer Machine
    ↓
Docker Compose (Local)
├── FastAPI dev server
├── PostgreSQL
├── Redis
└── RabbitMQ
```

### Staging Environment
```
GitHub Actions Pipeline
    ↓
Docker Registry
    ↓
Staging Cluster (Kubernetes)
├── FastAPI replicas (3)
├── PostgreSQL (HA)
├── Redis (Cluster)
└── RabbitMQ (Cluster)
```

### Production Environment
```
GitHub Actions Pipeline (Manual approval by CEO)
    ↓
Docker Registry
    ↓
Production Cluster (Kubernetes)
├── FastAPI replicas (5+)
├── PostgreSQL (HA + Backup)
├── Redis (Cluster + Replication)
└── RabbitMQ (Cluster + HA)

Monitoring:
├── Prometheus metrics
├── Grafana dashboards
├── CloudWatch logs
└── PagerDuty alerts
```

---

## Scalability Considerations

### Horizontal Scaling
- **FastAPI:** Stateless, scales via load balancer
- **PostgreSQL:** Read replicas for queries, primary for writes
- **Redis:** Cluster mode for high throughput
- **RabbitMQ:** Cluster mode with federation

### Vertical Scaling
- Container resource limits (CPU, memory)
- Database connection pooling
- Message queue throughput tuning

### Performance Targets
- **Decision latency:** < 500ms (proposal to human)
- **Approval latency:** < 100ms (approval to execution)
- **Throughput:** 1000+ decisions/hour
- **Availability:** 99.95% uptime SLA

---

## Governance Flow

```
Decision Proposed by Agent
        ↓
Authority Gateway checks:
├─ Is user authorized?
├─ Meets policy rules?
└─ Within risk limits?
        ↓
If all pass → Present to Human
        ↓
Human Reviews:
├─ Full reasoning
├─ Historical outcomes
├─ Risk assessment
└─ Alternative options
        ↓
Human Decision:
├─ Approve (execute)
├─ Reject (log reason)
└─ Modify (change parameters)
        ↓
Execute OR Reject & Log
        ↓
Track Outcome for Learning
        ↓
Update Decision Memory
```

---

## Quality Assurance

### Testing Strategy
- **Unit Tests:** > 80% coverage
- **Integration Tests:** Event flow validation
- **End-to-End Tests:** Full decision workflows
- **Performance Tests:** Latency and throughput
- **Security Tests:** OWASP Top 10

### CI/CD Pipeline
```
1. Code Push → GitHub
2. Pre-commit checks
3. Linting & formatting
4. Unit tests
5. Integration tests
6. Security scanning
7. Build Docker image
8. Push to registry
9. Deploy to staging
10. Smoke tests
11. Approval required for production
12. Deploy to production
13. Post-deployment validation
```

### Monitoring & Alerting
- **SLO:** 99.95% availability
- **SLI:** Error rate < 0.1%
- **Error budget:** < 21 minutes/month downtime
- **Alert thresholds:**
  - CPU > 80% for 5 minutes
  - Memory > 85% for 5 minutes
  - Decision latency > 1 second
  - Error rate > 1%

---

## Future Roadmap

### Phase 1 (Current): Foundation
- ✅ Architecture documentation
- ✅ Core API framework
- ✅ Decision memory
- ✅ Human authority gateway
- ✅ Basic monitoring

### Phase 2: Advanced Orchestration
- LangGraph agent orchestration
- Vector database for semantic search
- Advanced decision reasoning
- Kubernetes deployment
- Multi-region support

### Phase 3: Digital Twins
- Predictive decision modeling
- Scenario simulation
- What-if analysis
- Machine learning integration
- Advanced analytics

### Phase 4: Enterprise Scale
- Multi-tenant support
- Advanced RBAC
- Compliance automation
- API marketplace
- Third-party integrations

---

## References & Standards

- **API Design:** OpenAPI 3.0
- **Data Validation:** JSON Schema + Pydantic
- **Logging:** JSON format, ISO 8601 timestamps
- **Error Codes:** HTTP semantics
- **Database:** PostgreSQL 14+
- **Container:** Docker best practices
- **CI/CD:** GitHub Actions best practices

---

## Contact & Governance

- **Owner:** Asif Rana (CEO & Final Authority)
- **Repository:** fisarana4-dot/Asif-Rana-
- **Review Requirements:** All PRs require CEO approval
- **Principle:** AI develops. Humans govern.
