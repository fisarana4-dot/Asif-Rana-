# NEXRA V16000 – Domain Model

## Executive Summary

The NEXRA V16000 Domain Model defines the core business concepts, entities, and relationships that drive the Enterprise AI Decision Operating System. This model spans three primary domains:

1. **Trading Domain** - XAUUSD market intelligence and decision support
2. **Business Domain** - Amazon procurement and vendor management
3. **Export Domain** - Global trade optimization and compliance

---

## Core Domain Concepts

### 1. Decision (Root Aggregate)

**Purpose:** Central entity representing a proposal for action by an AI agent that requires human approval.

```python
class Decision:
    id: UUID
    decision_id: str  # Human-readable: DEC-2026-07-001
    
    # Source
    agent_id: str  # Which agent proposed this
    domain: DomainType  # trading | business | export
    decision_type: str  # trade | procurement | shipment
    
    # Content
    proposal: ProposalDetails  # What action is proposed
    reasoning: str  # Why the agent recommends this
    confidence_score: float  # 0.0-1.0
    risk_score: float  # 0.0-1.0
    
    # Governance
    status: DecisionStatus  # proposed | approved | rejected | executed | cancelled
    approval_chain: List[ApprovalStep]  # Who approved and when
    
    # Timeline
    proposed_at: datetime
    approved_at: Optional[datetime]
    executed_at: Optional[datetime]
    
    # Outcome
    outcome: Optional[DecisionOutcome]
    impact_score: Optional[float]  # -1.0 to +1.0
    learned_at: Optional[datetime]
```

**Invariants:**
- A decision must have a proposal
- Status transitions follow strict lifecycle rules
- Approved decisions can only be executed once
- All approvals must be recorded

**Business Rules:**
- Trading decisions > $10K require CEO approval
- High-risk decisions (risk_score > 0.8) require CEO approval
- Decision latency must be < 500ms from proposal to human
- All decisions must be audited

---

### 2. Proposal (Value Object)

**Purpose:** Encapsulates what action is being proposed, with all parameters needed for execution.

```python
# Trading Domain
class TradeProposal:
    instrument: str  # XAUUSD
    action: TradeAction  # buy | sell
    volume: int  # Micro-lots (0.01)
    entry_price: float
    stop_loss: Optional[float]
    take_profit: Optional[float]
    leverage: Optional[float]
    time_in_force: str  # IOC | GTC | GTD

# Business Domain
class ProcurementProposal:
    vendor_id: str
    item_id: str
    quantity: int
    unit_price: float
    payment_terms: str  # Net 30, 2/10 Net 30, etc
    delivery_date: date
    special_conditions: Optional[str]

# Export Domain
class ShipmentProposal:
    destination_country: str
    items: List[ExportItem]
    preferred_route: str  # Port code or air freight
    hedge_percentage: float  # 0-100% currency hedging
    insurance_type: str  # basic | comprehensive
```

**Invariants:**
- All proposals must be valid for their domain
- Quantities must be positive integers
- Prices must be positive floats
- Required fields cannot be null

---

### 3. Agent (Aggregate Root)

**Purpose:** Represents an autonomous reasoning entity that proposes decisions within its domain.

```python
class Agent:
    id: UUID
    agent_id: str  # trading-agent-001
    name: str
    description: str
    domain: DomainType
    agent_type: str  # market_monitor | analyzer | strategist
    
    # Capabilities
    capabilities: List[str]
    supported_decisions: List[str]
    max_decision_value: Optional[float]
    
    # Configuration
    config: AgentConfig
    rules: List[Rule]
    
    # Performance
    total_decisions: int
    successful_decisions: int
    accuracy_score: float
    
    # State
    status: AgentStatus  # active | paused | error
    last_decision_at: Optional[datetime]
    error_log: Optional[str]
```

**Responsibilities:**
- Monitor external data sources
- Analyze market/business conditions
- Generate proposals with reasoning
- Accept/handle rejections
- Learn from outcomes

**Agent Types:**

1. **Market Monitor Agent**
   - Responsibility: 24/7 market surveillance
   - Triggers: Price alerts, pattern detection, volatility spikes
   - Output: Trade proposals

2. **Analyzer Agent**
   - Responsibility: Deep analysis of proposals
   - Input: Raw market data
   - Output: Risk assessments, confidence scores

3. **Strategist Agent**
   - Responsibility: Long-term strategy
   - Input: Historical outcomes, trends
   - Output: Strategic recommendations

4. **Vendor Intelligence Agent**
   - Responsibility: Procurement analysis
   - Input: Vendor data, pricing
   - Output: Procurement proposals

---

### 4. Authority (Aggregate Root)

**Purpose:** Manages human approval authority and governance rules.

```python
class Authority:
    id: UUID
    user_id: str
    email: str
    name: str
    role: AuthorityRole  # CEO | CFO | COO | Trader | Manager
    
    # Permissions
    can_approve_decisions: bool
    max_approval_value: Optional[float]
    approved_domains: List[DomainType]
    
    # Activity
    total_approvals: int
    approval_rate: float  # % approved vs rejected
    avg_approval_time: timedelta
    
    # Status
    active: bool
    last_login: Optional[datetime]
    delegation: Optional['Authority']  # Can delegate to another
```

**Authority Rules:**
- CEO: Unlimited approval authority
- CFO: Financial decisions < $100K
- COO: Operational decisions < $50K
- Trader: Trading decisions < $10K
- Manager: Procurement < $5K

**Approval Logic:**
```
if decision.value > authority.max_approval_value:
    escalate_to_superior()
elif decision.domain not in authority.approved_domains:
    escalate_to_domain_expert()
else:
    allow_approval()
```

---

### 5. Approval (Value Object)

**Purpose:** Records a human decision to approve or reject a proposal.

```python
class Approval:
    id: UUID
    decision_id: UUID
    approved_by: str  # User ID
    approved_at: datetime
    approval_status: ApprovalStatus  # approved | rejected | modified
    
    # Reasoning
    approval_reason: Optional[str]
    approval_confidence: Optional[float]
    
    # Modifications
    modifications: Optional[ProposalModifications]
    
    # Audit
    ip_address: str
    user_agent: str
    signature: Optional[str]  # Digital signature for compliance
```

**Invariants:**
- Approval must reference a valid decision
- Approval reason required for rejections
- Cannot modify a decision after execution
- Digital signature required for high-value approvals

---

### 6. Event (Domain Event)

**Purpose:** Records all significant state changes for audit, learning, and event sourcing.

```python
class DomainEvent:
    id: UUID
    event_type: str
    aggregate_id: UUID
    aggregate_type: str
    
    # Content
    data: Dict[str, Any]
    
    # Timeline
    occurred_at: datetime
    recorded_at: datetime
    
    # Attribution
    caused_by: str  # user_id | agent_id
    correlation_id: UUID  # Links related events

# Event Types
class DecisionProposedEvent(DomainEvent):
    decision_id: UUID
    agent_id: str
    domain: DomainType

class DecisionApprovedEvent(DomainEvent):
    decision_id: UUID
    approved_by: str
    approval_reason: Optional[str]

class DecisionRejectedEvent(DomainEvent):
    decision_id: UUID
    rejected_by: str
    rejection_reason: str

class DecisionExecutedEvent(DomainEvent):
    decision_id: UUID
    execution_time: datetime
    execution_status: str

class OutcomeRecordedEvent(DomainEvent):
    decision_id: UUID
    outcome: DecisionOutcome
    impact_score: float
```

---

## Domain-Specific Models

### Trading Domain Model

```python
class TradingContext:
    symbol: str  # XAUUSD
    current_price: float
    bid: float
    ask: float
    
    # Market data
    volume_24h: float
    high_24h: float
    low_24h: float
    
    # Indicators
    technical_indicators: TechnicalIndicators
    fundamental_factors: FundamentalFactors
    
    # Volatility
    atr: float  # Average True Range
    volatility: float  # 0-1 scale
    
    # Risk
    supported_leverage: float
    available_margin: float
    max_position_size: int

class TechnicalIndicators:
    rsi: float  # Relative Strength Index
    macd: MACDValue
    bollinger_bands: BollingerBands
    moving_averages: Dict[int, float]  # 20, 50, 200
    pattern: Optional[str]  # head_shoulders, double_top, etc

class FundamentalFactors:
    fed_rate: float
    usd_index: float
    real_rates: float
    geopolitical_risk: float  # 0-1
    inflation: float

class TradeOutcome:
    entry_price: float
    exit_price: float
    profit_loss: float
    profit_loss_pct: float
    hold_time: timedelta
    status: str  # win | loss | breakeven
```

**Trading Rules:**
```
- Min lot: 0.01 (micro-lot)
- Max position: 100 lots per trade
- Max daily loss: -5% of account
- Stop loss required for all trades
- Leverage: 1:1 to 1:100 based on volatility
```

---

### Business Domain Model

```python
class VendorProfile:
    vendor_id: str
    name: str
    category: str  # electronics | raw_materials | services
    
    # Performance
    on_time_delivery_rate: float
    quality_score: float  # 0-100
    compliance_score: float  # 0-100
    
    # Financial
    credit_rating: str  # A+ | A | B+ | B | C
    payment_history: List[PaymentRecord]
    
    # Relationship
    years_with_us: int
    total_orders: int
    total_spent: float
    
    # Risk
    geopolitical_risk: float
    financial_risk: float
    quality_risk: float

class ProcurementHistory:
    vendor_id: str
    order_id: str
    item_id: str
    quantity: int
    unit_price: float
    order_date: date
    delivery_date: date
    payment_date: date
    quality_rating: float
    on_time: bool

class ProcurementOutcome:
    proposal_id: UUID
    actual_price: float
    actual_delivery_date: date
    actual_quality: float
    negotiation_savings: float
    vendor_satisfaction: float
```

**Procurement Rules:**
```
- Vendor must have credit_rating >= B
- On-time delivery rate > 85%
- Quality score > 70%
- Get 3 quotes for items > $10K
- CEO approval for items > $50K
```

---

### Export Domain Model

```python
class ExportShipment:
    shipment_id: str
    origin_country: str
    destination_country: str
    
    # Items
    items: List[ExportItem]
    total_value: float
    total_weight: float
    
    # Route
    route: ShippingRoute
    departure_date: date
    estimated_arrival: date
    
    # Compliance
    hs_codes: Dict[str, str]  # Item -> HS Code
    certifications: List[str]
    compliance_status: str  # pending | approved | customs_hold
    
    # Currency
    currency: str  # USD, EUR, etc
    hedge_percentage: float
    hedge_instrument: Optional[str]
    
    # Insurance
    insurance_type: str
    insurance_value: float
    insurance_provider: str

class ShippingRoute:
    route_id: str
    departure_port: str
    arrival_port: str
    transit_days: int
    cost: float
    reliability_score: float
    risk_factors: List[str]

class ExportOutcome:
    shipment_id: str
    actual_delivery_date: date
    customs_delay: Optional[int]  # days
    final_cost: float
    cost_variance: float
    currency_impact: float
    margin_achieved: float
```

**Export Rules:**
```
- All exports must have valid HS codes
- Tariff must be calculated before export
- Currency hedge for > 50% of value recommended
- Insurance required for > $100K shipments
- Compliance check mandatory
```

---

## Relationships & Dependencies

### Decision Lifecycle

```
1. PROPOSED
   ├─ Agent generates proposal
   ├─ System validates against rules
   └─ Event: DecisionProposedEvent

2. AWAITING_APPROVAL
   ├─ Human Authority notified
   ├─ Decision details provided
   └─ Awaiting decision

3. APPROVED
   ├─ Authority approves
   ├─ Event: DecisionApprovedEvent
   └─ Ready for execution

4. REJECTED
   ├─ Authority rejects
   ├─ Event: DecisionRejectedEvent
   └─ Agent learns from rejection

5. EXECUTED
   ├─ Action taken (trade, purchase, shipment)
   ├─ Event: DecisionExecutedEvent
   └─ Outcome monitored

6. OUTCOME_RECORDED
   ├─ Result tracked
   ├─ Event: OutcomeRecordedEvent
   └─ Decision Memory updated

7. ARCHIVED
   └─ Historical record maintained
```

### Agent Decision Flow

```
Agent
├─ Monitor (observe market/business)
├─ Analyze (process data)
├─ Reason (apply logic)
├─ Generate Proposal (with confidence)
└─ Submit Decision
    ├─ Governance Rules Check
    ├─ Proposal Validation
    ├─ Risk Assessment
    └─ Authority Notification
```

### Authority Approval Flow

```
Decision (Awaiting Approval)
├─ Authority Reviews
│  ├─ Proposal details
│  ├─ AI reasoning
│  ├─ Risk assessment
│  ├─ Historical outcomes
│  └─ Similar decisions
├─ Authority Decides
│  ├─ Approve (with optional modifications)
│  ├─ Reject (with reason)
│  └─ Delegate (to another authority)
└─ Record Approval
   ├─ Create Approval event
   ├─ Update Decision status
   └─ Trigger execution or archive
```

---

## Entity Relationships (ERD)

```
┌─────────────────────────────────────────────┐
│ AUTHORITY                                   │
├──────────────────────────────────────────────┤
│ id (PK)                                      │
│ user_id (UNIQUE)                             │
│ role: CEO | CFO | COO | Trader | Manager    │
│ max_approval_value                           │
│ active: boolean                              │
└────────────────────────────┬──────────────────┘
                             │
                    1:N      │ approves
                             │
┌────────────────────────────▼──────────────────┐
│ DECISION                                      │
├────────────────────────────────────────────────┤
│ id (PK)                                        │
│ agent_id (FK)                                  │
│ domain: trading | business | export           │
│ proposal: JSON                                 │
│ status: proposed | approved | executed        │
│ proposed_at: timestamp                         │
│ approved_at: timestamp (nullable)              │
│ executed_at: timestamp (nullable)              │
└────┬──────────────────────────┬────────────────┘
     │                          │
     │ 1:N generates            │ 1:1 has_outcome
     │                          │
     ▼                          ▼
┌─────────────┐         ┌──────────────────┐
│ AGENT       │         │ DECISION_OUTCOME │
├─────────────┤         ├──────────────────┤
│ id (PK)     │         │ id (PK)          │
│ agent_id    │         │ decision_id (FK) │
│ domain      │         │ outcome: JSON    │
│ type        │         │ impact_score     │
│ status      │         │ learned_at       │
└─────────────┘         └──────────────────┘

┌──────────────────────────────┐
│ EVENT                         │
├──────────────────────────────┤
│ id (PK)                       │
│ event_type: string            │
│ aggregate_id (FK)             │
│ data: JSON                     │
│ occurred_at: timestamp        │
│ caused_by: user_id | agent_id │
└──────────────────────────────┘
```

---

## Value Objects

### DecisionStatus (Enum)

```python
class DecisionStatus(Enum):
    PROPOSED = "proposed"
    AWAITING_APPROVAL = "awaiting_approval"
    APPROVED = "approved"
    REJECTED = "rejected"
    EXECUTED = "executed"
    OUTCOME_RECORDED = "outcome_recorded"
    ARCHIVED = "archived"
```

### DomainType (Enum)

```python
class DomainType(Enum):
    TRADING = "trading"
    BUSINESS = "business"
    EXPORT = "export"
```

### ApprovalStatus (Enum)

```python
class ApprovalStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    MODIFIED = "modified"
```

---

## Repository Interfaces

```python
class DecisionRepository:
    async def save(decision: Decision) -> None: ...
    async def find_by_id(decision_id: UUID) -> Optional[Decision]: ...
    async def find_by_status(status: DecisionStatus) -> List[Decision]: ...
    async def find_by_agent(agent_id: str) -> List[Decision]: ...
    async def find_by_domain(domain: DomainType) -> List[Decision]: ...

class AgentRepository:
    async def save(agent: Agent) -> None: ...
    async def find_by_id(agent_id: str) -> Optional[Agent]: ...
    async def find_by_domain(domain: DomainType) -> List[Agent]: ...

class AuthorityRepository:
    async def save(authority: Authority) -> None: ...
    async def find_by_user_id(user_id: str) -> Optional[Authority]: ...
    async def find_by_role(role: AuthorityRole) -> List[Authority]: ...

class EventStore:
    async def append(event: DomainEvent) -> None: ...
    async def get_events_for(aggregate_id: UUID) -> List[DomainEvent]: ...
    async def get_all_events_since(timestamp: datetime) -> List[DomainEvent]: ...
```

---

## Domain Services

### DecisionService

```python
class DecisionService:
    async def propose_decision(
        agent_id: str,
        domain: DomainType,
        proposal: ProposalDetails,
        reasoning: str
    ) -> Decision: ...
    
    async def validate_proposal(proposal: ProposalDetails) -> bool: ...
    
    async def calculate_risk_score(proposal: ProposalDetails) -> float: ...
    
    async def find_similar_decisions(
        proposal: ProposalDetails
    ) -> List[Decision]: ...
```

### ApprovalService

```python
class ApprovalService:
    async def get_pending_approvals(
        authority_id: str
    ) -> List[Decision]: ...
    
    async def approve_decision(
        decision_id: UUID,
        authority_id: str,
        reason: Optional[str]
    ) -> Decision: ...
    
    async def reject_decision(
        decision_id: UUID,
        authority_id: str,
        reason: str
    ) -> Decision: ...
    
    async def can_approve(
        authority_id: str,
        decision: Decision
    ) -> bool: ...
```

### OutcomeService

```python
class OutcomeService:
    async def record_outcome(
        decision_id: UUID,
        outcome_data: Dict
    ) -> DecisionOutcome: ...
    
    async def calculate_impact(
        decision: Decision,
        outcome: DecisionOutcome
    ) -> float: ...
    
    async def learn_from_decision(
        decision: Decision
    ) -> None: ...
```

---

## Invariants & Business Rules

### Global Invariants

1. **Every decision must be attributed to an agent**
   - A decision without an agent_id is invalid

2. **Approval chain must be maintained**
   - Cannot skip approval levels for high-value decisions
   - All approvals must be recorded

3. **Audit trail is immutable**
   - Events cannot be deleted
   - Events record the complete history

4. **Status transitions are ordered**
   - Cannot jump from PROPOSED to EXECUTED
   - Cannot revert to PROPOSED from EXECUTED

### Domain-Specific Rules

**Trading Domain:**
- Every trade must have a stop loss
- Position size cannot exceed 100 lots
- Leverage based on volatility assessment
- Daily loss limit: -5% of account

**Business Domain:**
- Vendors must meet minimum quality standards
- Multiple quotes required for large purchases
- Payment terms must match historical patterns
- Ethical sourcing verification required

**Export Domain:**
- HS codes must be valid for the country pair
- Tariff calculation mandatory before commitment
- Insurance required for high-value shipments
- Compliance checks must pass before execution

---

## Conclusion

The NEXRA V16000 Domain Model provides a clear, structured representation of the business concepts and entities that drive decision-making across three critical domains. By adhering to this model, the system maintains consistency, auditability, and human governance throughout the decision lifecycle.

**Core Principle:** Decisions drive value. Humans govern decisions. AI reasons about decisions.

---

## Document Control

| Property | Value |
|----------|-------|
| Version | 1.0 |
| Date | 2026-07-11 |
| Owner | Asif Rana (CEO) |
| Status | Active |
| Next Review | 2026-10-11 |
