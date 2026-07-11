NEXRA V16000 Event Catalog

## Purpose

The Event Catalog defines all important events generated, consumed, and tracked inside NEXRA V16000.

Events provide a reliable communication layer between system components while maintaining auditability, traceability, and scalability.

NEXRA V16000 follows an event-driven architecture where important state changes are recorded as immutable events.

---

# Event Structure

Every event must contain:

## Event ID

Unique identifier for every event.

Example:

EVENT-2026-000001

---

## Event Timestamp

The exact time when the event occurred.

Example:

2026-07-12T10:30:00Z

---

## Event Type

Defines the category of the event.

Examples:

- DecisionCreated
- DecisionApproved
- AgentExecuted
- TradeSignalGenerated
- RiskCheckCompleted
- BusinessLeadCreated

---

## Source Service

The system component that generated the event.

Examples:

- Authority Gateway
- Trading Engine
- Amazon Intelligence Agent
- Export EDOS Engine

---

## Event Payload

Contains the information related to the event.

Example:

```json
{
  "decision_id": "DEC-001",
  "domain": "Gold Trading",
  "status": "approved"
}
