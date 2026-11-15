#!/usr/bin/env python3
"""Panel schedule generator (standard Canadian commercial format).
Input: a JSON file {"panel": {...}, "circuits": [{"desc": "...", "va": 1200, "poles": 1, "breaker": 20, "type": "Receptacle"}, ...]}
Usage:
  python3 panel_schedule.py schedule.json
Prints the schedule as a text table with per-phase totals and balance.
"""
import json, sys
def build(circuits, phases=3):
    rows, per = [], [0.0] * phases
    r1 = r2 = 0
    for i, c in enumerate(circuits):
        va = float(c.get("va", 0)); poles = int(c.get("poles", 1))
        if phases == 1:
            ph = ["A"]; per[0] += va
        elif poles == 1:
            ph = [["A", "B", "C"][r1 % 3]]; per[r1 % 3] += va; r1 += 1
        elif poles == 2:
            pair = [["A", "B"], ["B", "C"], ["C", "A"]][r2 % 3]; ph = pair
            per[["A", "B", "C"].index(pair[0])] += va / 2; per[["A", "B", "C"].index(pair[1])] += va / 2; r2 += 1
        else:
            ph = ["A", "B", "C"]
            for j in range(3): per[j] += va / 3
        rows.append((i + 1, c.get("desc", ""), c.get("type", ""), c.get("breaker", ""), poles, "/".join(ph), va))
    return rows, per
def main():
    doc = json.load(open(sys.argv[1]))
    p = doc.get("panel", {})
    phases = 1 if "1-phase" in str(p.get("system", "")) else 3
    print(f"PANEL {p.get('name', '')} | {p.get('system', '')} | Bus {p.get('bus_a', '')} A | Main {p.get('main', '')}")
    print(f"{'CKT':>4} {'DESCRIPTION':32s} {'TYPE':14s} {'BKR':>5} {'P':>2} {'PH':5s} {'VA':>8}")
    rows, per = build(doc["circuits"], phases)
    for r in rows:
        print(f"{r[0]:>4} {r[1]:32s} {r[2]:14s} {str(r[3]):>5} {r[4]:>2} {r[5]:5s} {r[6]:>8,.0f}")
    names = ["A", "B", "C"][:phases]
    print("Per-phase connected load:", ", ".join(f"{names[i]} {per[i]:,.0f} VA" for i in range(phases)))
    if phases == 3:
        avg = sum(per) / 3
        spread = (max(per) - min(per)) / avg * 100 if avg else 0
        print(f"Phase balance spread: {spread:.1f}% of average phase load")
if __name__ == "__main__":
    main()
