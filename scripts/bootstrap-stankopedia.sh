#!/usr/bin/env bash
set -euo pipefail

BASE="STANKOPEDIA"

mkdir -p "$BASE"/{
00-Introduction,
01-Engineering-Principles,
02-Engineering-Program,
03-Production-Workflow,
04-Standards,
05-Current-Projects/STANK-RADIO,
Appendix
}

touch \
"$BASE/README.md" \
"$BASE/00-Introduction/Welcome.md" \
"$BASE/00-Introduction/Engineering-Philosophy.md" \
"$BASE/00-Introduction/Principle-0-The-Requirements-Are-Sacred.md" \
"$BASE/01-Engineering-Principles/ENG-001-Engineering-Principles.md" \
"$BASE/01-Engineering-Principles/DL-001-Decision-Log.md" \
"$BASE/01-Engineering-Principles/FGR-001-Fools-Gold-Register.md" \
"$BASE/01-Engineering-Principles/HZ-001-The-Horizon.md" \
"$BASE/02-Engineering-Program/SEP-001-STANK-Engineering-Program.md" \
"$BASE/02-Engineering-Program/SRR-001-SR-Register.md" \
"$BASE/02-Engineering-Program/ECO-REG-001-ECO-Register.md" \
"$BASE/02-Engineering-Program/PAR-001-Production-Asset-Register.md" \
"$BASE/02-Engineering-Program/Timeline.md" \
"$BASE/02-Engineering-Program/Status-Dashboard.md" \
"$BASE/03-Production-Workflow/WF-001-Production-Workflow.md" \
"$BASE/03-Production-Workflow/Candidate-Workflow.md" \
"$BASE/03-Production-Workflow/Engineering-Review.md" \
"$BASE/03-Production-Workflow/Production-Promotion.md" \
"$BASE/03-Production-Workflow/Image-Engineering-Standard.md" \
"$BASE/03-Production-Workflow/Software-Engineering-Standard.md" \
"$BASE/03-Production-Workflow/Acceptance-Checklists.md" \
"$BASE/04-Standards/STD-001-Prompt-Standards.md" \
"$BASE/04-Standards/Naming-Standards.md" \
"$BASE/04-Standards/File-Organization.md" \
"$BASE/04-Standards/Asset-Standards.md" \
"$BASE/04-Standards/Prompt-Templates.md" \
"$BASE/04-Standards/Review-Templates.md" \
"$BASE/04-Standards/ECO-Templates.md" \
"$BASE/05-Current-Projects/STANK-RADIO/Requirements.md" \
"$BASE/05-Current-Projects/STANK-RADIO/SRs.md" \
"$BASE/05-Current-Projects/STANK-RADIO/ECOs.md" \
"$BASE/05-Current-Projects/STANK-RADIO/Assets.md" \
"$BASE/05-Current-Projects/STANK-RADIO/Timeline.md" \
"$BASE/Appendix/Glossary.md" \
"$BASE/Appendix/Terminology.md" \
"$BASE/Appendix/Revision-History.md"

echo "STANKOPEDIA scaffold created."
