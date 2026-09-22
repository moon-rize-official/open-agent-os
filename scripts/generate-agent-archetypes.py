#!/usr/bin/env python3
"""Generate the Open Agent OS public agent-archetype catalog.

This is a PROPOSAL catalog, not a recovered copy of the historical
AI-FLEET 1,332-role registry and not a recommendation to instantiate
all generated agents simultaneously.
"""
from __future__ import annotations

import csv
import json
import re
from pathlib import Path

DEPARTMENTS = [
    "Executive & Strategy",
    "Product",
    "Research & Innovation",
    "Engineering",
    "AI & Agent Systems",
    "Data & Analytics",
    "Design & User Experience",
    "Platform & Infrastructure",
    "Security",
    "IT & Internal Systems",
    "Knowledge & Documentation",
    "Operations",
    "Quality & Reliability",
    "Sales",
    "Marketing & Growth",
    "Partnerships & Business Development",
    "Customer Success",
    "Customer Support",
    "Professional Services",
    "Finance & Accounting",
    "People & HR",
    "Legal",
    "Compliance & Governance",
    "Risk Management",
    "Procurement & Vendor Management",
    "Corporate Development",
    "Communications & Public Relations",
    "Program & Project Management",
    "Facilities & Workplace",
    "Supply Chain & Logistics",
    "Manufacturing & Production",
    "Regulatory Affairs",
    "Trust & Safety",
    "Internal Audit",
    "Business Continuity & Crisis Management",
    "Developer Experience",
    "Architecture",
    "Cloud & Network Engineering",
    "Developer Platform",
    "Data Platform",
    "AI Platform",
    "Automation & Integration Platform",
    "Enterprise Architecture & Shared Services",
]

ROLE_FAMILIES = [
    "strategy-planning",
    "analysis-research",
    "implementation-delivery",
    "operations-reliability",
    "verification-governance",
    "knowledge-coordination",
]

LEVELS = [
    ("L0", "utility-worker", "R1"),
    ("L1", "specialist", "R1"),
    ("L2", "senior-specialist", "R2"),
    ("L3", "team-lead", "R2"),
    ("L4", "department-lead", "R3"),
    ("L5", "executive-coordinator", "R3"),
]

def slug(text: str) -> str:
    value = text.lower().replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return re.sub(r"-+", "-", value)

def build() -> list[dict]:
    out = []
    for department in DEPARTMENTS:
        dslug = slug(department)
        for family in ROLE_FAMILIES:
            for level, level_name, max_risk in LEVELS:
                out.append(
                    {
                        "id": f"{dslug}-{family}-{level_name}",
                        "department": department,
                        "role_family": family,
                        "capability_level": level,
                        "authority": {
                            "max_risk": max_risk,
                            "production_mutation": False,
                            "secrets": "none",
                        },
                        "capabilities": [
                            family,
                            "bounded-task-execution",
                            "evidence-recording",
                        ],
                        "provenance": {
                            "classification": "PROPOSAL",
                            "source": "Open Agent OS public archetype generator",
                        },
                    }
                )
    return out

def main() -> None:
    rows = build()
    expected = len(DEPARTMENTS) * len(ROLE_FAMILIES) * len(LEVELS)
    assert len(rows) == expected == 1548

    root = Path(__file__).resolve().parents[1]
    generated = root / "generated"
    generated.mkdir(exist_ok=True)

    (generated / "agent-archetypes.json").write_text(
        json.dumps(rows, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    with (generated / "agent-archetypes.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "id",
                "department",
                "role_family",
                "capability_level",
                "max_risk",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "id": row["id"],
                    "department": row["department"],
                    "role_family": row["role_family"],
                    "capability_level": row["capability_level"],
                    "max_risk": row["authority"]["max_risk"],
                }
            )

    summary = {
        "status": "PROPOSAL",
        "departments": len(DEPARTMENTS),
        "role_families": len(ROLE_FAMILIES),
        "capability_levels": len(LEVELS),
        "archetypes": len(rows),
        "warning": "Catalog only; do not instantiate every archetype simultaneously.",
    }
    (generated / "agent-archetypes-summary.json").write_text(
        json.dumps(summary, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, indent=2))

if __name__ == "__main__":
    main()
