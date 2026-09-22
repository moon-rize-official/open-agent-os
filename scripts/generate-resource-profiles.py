#!/usr/bin/env python3
"""Generate compact agent resource-profile manifests."""
from __future__ import annotations
import json
from pathlib import Path

DEPARTMENTS = {
  "executive-strategy": "Executive & Strategy",
  "product": "Product",
  "research-innovation": "Research & Innovation",
  "engineering": "Engineering",
  "ai-agent-systems": "AI & Agent Systems",
  "data-analytics": "Data & Analytics",
  "design-user-experience": "Design & User Experience",
  "platform-infrastructure": "Platform & Infrastructure",
  "security": "Security",
  "it-internal-systems": "IT & Internal Systems",
  "knowledge-documentation": "Knowledge & Documentation",
  "operations": "Operations",
  "quality-reliability": "Quality & Reliability",
  "sales": "Sales",
  "marketing-growth": "Marketing & Growth",
  "partnerships-business-development": "Partnerships & Business Development",
  "customer-success": "Customer Success",
  "customer-support": "Customer Support",
  "professional-services": "Professional Services",
  "finance-accounting": "Finance & Accounting",
  "people-hr": "People & HR",
  "legal": "Legal",
  "compliance-governance": "Compliance & Governance",
  "risk-management": "Risk Management",
  "procurement-vendor-management": "Procurement & Vendor Management",
  "corporate-development": "Corporate Development",
  "communications-pr": "Communications & Public Relations",
  "program-project-management": "Program & Project Management",
  "facilities-workplace": "Facilities & Workplace",
  "supply-chain-logistics": "Supply Chain & Logistics",
  "manufacturing-production": "Manufacturing & Production",
  "regulatory-affairs": "Regulatory Affairs",
  "trust-safety": "Trust & Safety",
  "internal-audit": "Internal Audit",
  "business-continuity-crisis": "Business Continuity & Crisis Management",
  "developer-experience": "Developer Experience",
  "architecture": "Architecture",
  "cloud-network-engineering": "Cloud & Network Engineering",
  "developer-platform": "Developer Platform",
  "data-platform": "Data Platform",
  "ai-platform": "AI Platform",
  "automation-integration-platform": "Automation & Integration Platform",
  "enterprise-architecture-shared-services": "Enterprise Architecture & Shared Services"
}
ROLE_FAMILIES = ["strategy-planning","analysis-research","implementation-delivery","operations-reliability","verification-governance","knowledge-coordination"]
LEVELS = {"L0":("utility-worker","R1"),"L1":("specialist","R1"),"L2":("senior-specialist","R2"),"L3":("team-lead","R2"),"L4":("department-lead","R3"),"L5":("executive-coordinator","R3")}

def build():
    rows=[]
    for dept_id, dept_name in DEPARTMENTS.items():
        for role in ROLE_FAMILIES:
            for level,(level_name,max_risk) in LEVELS.items():
                rows.append({
                    "id":f"{dept_id}-{role}-{level_name}",
                    "department":dept_name,
                    "department_pack":f"packs/departments/{dept_id}.yaml",
                    "role_family":role,
                    "role_overlay":f"packs/roles/{role}.yaml",
                    "common_pack":"packs/common/agent-baseline.yaml",
                    "capability_level":level,
                    "max_risk":max_risk,
                    "composition":"common+department+role+project+task+live",
                })
    assert len(rows)==1548
    return rows

def main():
    root=Path(__file__).resolve().parents[1]
    out=root/"generated"
    out.mkdir(exist_ok=True)
    rows=build()
    (out/"agent-resource-profiles.ndjson").write_text("\n".join(json.dumps(r,separators=(",",":")) for r in rows)+"\n",encoding="utf-8")
    summary={"version":1,"status":"PROPOSAL","departments":len(DEPARTMENTS),"role_families":len(ROLE_FAMILIES),"capability_levels":len(LEVELS),"profiles":len(rows)}
    (out/"resource-profile-summary.json").write_text(json.dumps(summary,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(summary,indent=2))

if __name__=="__main__":
    main()
