NEXRA V16000 v1.1: audit crash, duplicate, persistence, reconciliation, SL, unknown execution and broker mismatch.
## Persistence
WAL; crash recovery; immutable log; atomic transitions; durable DB.
## Duplicate
Unique key; atomic reservation; broker query; reject duplicates.
## AUDIT TASKS
1. STATE MACHINE: Missing states? Deadlocks? Race conditions?
2. PERSISTENCE: Corruption? Crash-during-write? Stale reads?
3. CRASH: Crash at each state - duplicate? Lost state?
4. DUPLICATE: Slips through? Idempotency fails?
5. BROKER: Internal!=broker? Missing SL? Position mismatch?
6. ERROR: Not detected? Safe mode not triggered?
7. AUDIT TRAIL: Incomplete? Lost? Missing fields?
8. EDGE: Broker error but order executed? Network partition?
9. PARTIAL FILL: Not detected? Wrong handling?
10. UNKNOWN EXEC: Not triggered? Wrong resolution?
11. POST-FILL RISK: Actual!=planned? Risk breach?
12. SL: Silent widen? Broker conflict? SL removed?
13. ORPHAN: Not detected? Wrong adoption?
14. CLOCK: Drift? Timestamp mismatch?
## OUTPUT: Per finding - Scenario, Section, Impact, Fix, Test
## RULE: Do NOT mark safe without evidence. Find failures.
