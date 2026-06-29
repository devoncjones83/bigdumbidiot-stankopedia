#!/usr/bin/env bash
set -euo pipefail

BASE="STANKOPEDIA"

echo "Creating STANKOPEDIA directory structure..."

mkdir -p "$BASE"

mkdir -p "$BASE/00-Introduction"
mkdir -p "$BASE/01-Engineering-Principles"
mkdir -p "$BASE/02-Engineering-Program"
mkdir -p "$BASE/03-Production-Workflow"
mkdir -p "$BASE/04-Standards"
mkdir -p "$BASE/05-Current-Projects/STANK-RADIO"
mkdir -p "$BASE/Appendix"

touch "$BASE/README.md"

touch "$BASE/00-Introduction/Welcome.md"
touch "$BASE/00-Introduction/Engineering-Philosophy.md"
touch "$BASE/00-Introduction/Principle-0-The-Requirements-Are-Sacred.md"

touch "$BASE/01-Engineering-Principles/ENG-001-Engineering-Principles.md"
touch "$BASE/01-Engineering-Principles/DL-001-Decision-Log.md"
touch "$BASE/01-Engineering-Principles/FGR-001-Fools-Gold-Register.md"
touch "$BASE/01-Engineering-Principles/HZ-001-The-Horizon.md"

touch "$BASE/02-Engineering-Program/SEP-001-STANK-Engineering-Program.md"
touch "$BASE/02-Engineering-Program/SRR-001-SR-Register.md"
touch "$BASE/02-Engineering-Program/ECO-REG-001-ECO-Register.md"
touch "$BASE/02-Engineering-Program/PAR-001-Production-Asset-Register.md"
touch "$BASE/02-Engineering-Program/Engineering-Timeline.md"
touch "$BASE/02-Engineering-Program/Engineering-Status-Dashboard.md"

touch "$BASE/03-Production-Workflow/WF-001-Production-Workflow.md"
touch "$BASE/03-Production-Workflow/Candidate-Workflow.md"
touch "$BASE/03-Production-Workflow/Engineering-Review.md"
touch "$BASE/03-Production-Workflow/Production-Promotion.md"
touch "$BASE/03-Production-Workflow/Image-Engineering-Standard.md"
touch "$BASE/03-Production-Workflow/Software-Engineering-Standard.md"
touch "$BASE/03-Production-Workflow/Acceptance-Checklists.md"

touch "$BASE/04-Standards/STD-001-Prompt-Standards.md"
touch "$BASE/04-Standards/Naming-Standards.md"
touch "$BASE/04-Standards/File-Organization.md"
touch "$BASE/04-Standards/Asset-Standards.md"
touch "$BASE/04-Standards/Prompt-Templates.md"
touch "$BASE/04-Standards/Review-Templates.md"
touch "$BASE/04-Standards/ECO-Templates.md"

touch "$BASE/05-Current-Projects/STANK-RADIO/Requirements.md"
touch "$BASE/05-Current-Projects/STANK-RADIO/SRs.md"
touch "$BASE/05-Current-Projects/STANK-RADIO/ECOs.md"
touch "$BASE/05-Current-Projects/STANK-RADIO/Assets.md"
touch "$BASE/05-Current-Projects/STANK-RADIO/Timeline.md"

touch "$BASE/Appendix/Glossary.md"
touch "$BASE/Appendix/Terminology.md"
touch "$BASE/Appendix/Revision-History.md"

echo
echo "======================================="
echo " STANKOPEDIA scaffold created."
echo "======================================="
