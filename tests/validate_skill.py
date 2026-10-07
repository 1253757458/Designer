from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skill" / "designing-education-ecommerce-graphics"
REFERENCES = [
    "intake-and-strategy.md",
    "education-visual-system.md",
    "deliverable-playbooks.md",
    "platform-specs.md",
    "compliance.md",
    "image-generation.md",
    "quality-assurance.md",
    "source-notes.md",
]
REQUIRED = [SKILL / "SKILL.md", SKILL / "agents" / "openai.yaml"] + [
    SKILL / "references" / name for name in REFERENCES
]

errors = []
for path in REQUIRED:
    if not path.is_file():
        errors.append(f"missing file: {path.relative_to(ROOT)}")

if not errors:
    entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if "name: designing-education-ecommerce-graphics" not in entry:
        errors.append("incorrect skill name")
    for name in REFERENCES:
        if name not in entry:
            errors.append(f"SKILL.md does not route to {name}")

    all_text = "\n".join(path.read_text(encoding="utf-8") for path in REQUIRED)
    for marker in ("TODO", "TBD", "Replace with", "Example reference"):
        if marker in all_text:
            errors.append(f"unfinished scaffold marker: {marker}")

    compliance = (SKILL / "references" / "compliance.md").read_text(encoding="utf-8")
    for state in ("已核验可商用", "限制使用", "待补证", "禁止使用"):
        if state not in compliance:
            errors.append(f"missing asset-rights state: {state}")

    qa = (SKILL / "references" / "quality-assurance.md").read_text(encoding="utf-8")
    for gate in ("信息准确", "转化清晰", "视觉可靠", "权利完整", "合规可交付"):
        if gate not in qa:
            errors.append(f"missing quality gate: {gate}")

if errors:
    print("FAIL")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)

print("PASS: education ecommerce graphics skill structure and gates are complete")
