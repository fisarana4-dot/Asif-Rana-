def paper_order(d): return {"status":"BLOCK"} if not d.get("sl") else {"symbol":"XAUUSD","side":d["side"],"sl":d["sl"],"status":"PAPER"}
