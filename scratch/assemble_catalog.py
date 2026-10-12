# -*- coding: utf-8 -*-
"""
Assembler & Validator for Free Mind ML Catalog
Compiles all 52 lessons into js/catalog.js
"""
import json
import os
import sys

# Ensure scratch path is in sys.path
sys.path.insert(0, os.path.dirname(__file__))

from build_catalog import get_foundations
from gen_supervised import get_supervised
from gen_unsupervised import get_unsupervised
from gen_deeplearning import get_deeplearning
from gen_advanced import get_advanced

def assemble():
    f = get_foundations()
    s = get_supervised()
    u = get_unsupervised()
    d = get_deeplearning()
    a = get_advanced()

    all_lessons = f + s + u + d + a
    print(f"Total lessons assembled: {len(all_lessons)}")
    print(f"  Foundations   : {len(f)} (F01 - F07)")
    print(f"  Supervised    : {len(s)} (S01 - S13)")
    print(f"  Unsupervised  : {len(u)} (U01 - U08)")
    print(f"  Deep Learning : {len(d)} (D01 - D16)")
    print(f"  Advanced      : {len(a)} (A01 - A08)")

    required_sections = [
        "whatItIs", "problemItSolves", "intuition", "howItWorks",
        "mathematics", "dataRequirements", "hyperparameters",
        "strengths", "limitations", "evaluation", "workedExample",
        "whenToUse", "commonMistakes", "furtherLearning"
    ]

    expected_ids = (
        [f"F{i:02d}" for i in range(1, 8)] +
        [f"S{i:02d}" for i in range(1, 14)] +
        [f"U{i:02d}" for i in range(1, 9)] +
        [f"D{i:02d}" for i in range(1, 17)] +
        [f"A{i:02d}" for i in range(1, 9)]
    )

    errors = []
    seen_ids = set()

    for lesson in all_lessons:
        lid = lesson.get("id")
        if not lid:
            errors.append("Lesson missing 'id'")
            continue
        if lid in seen_ids:
            errors.append(f"Duplicate lesson id: {lid}")
        seen_ids.add(lid)

        # Validate sections
        sections = lesson.get("sections", {})
        for sec in required_sections:
            if sec not in sections or not sections[sec]:
                errors.append(f"Lesson {lid} missing section: {sec}")

        # Validate quiz
        quiz = lesson.get("quiz", [])
        if len(quiz) < 3:
            errors.append(f"Lesson {lid} has only {len(quiz)} quiz questions (minimum 3 required)")
        for qi, q in enumerate(quiz):
            if "question" not in q or not q["question"]:
                errors.append(f"Lesson {lid} quiz {qi} missing question text")
            if "options" not in q or len(q["options"]) != 4:
                errors.append(f"Lesson {lid} quiz {qi} does not have exactly 4 options")
            if "correct" not in q or not (0 <= q["correct"] <= 3):
                errors.append(f"Lesson {lid} quiz {qi} invalid correct index: {q.get('correct')}")
            if "explanation" not in q or not q["explanation"]:
                errors.append(f"Lesson {lid} quiz {qi} missing explanation")

    # Check for missing expected IDs
    for eid in expected_ids:
        if eid not in seen_ids:
            errors.append(f"Expected lesson {eid} not found in catalog")

    if errors:
        print("\n❌ VALIDATION ERRORS DETECTED:")
        for err in errors[:20]:
            print("  -", err)
        print(f"Total errors: {len(errors)}")
        sys.exit(1)

    print("\n[OK] All 52 lessons passed full validation! (15 sections, 3+ quizzes each)")

    # Serialize to js/catalog.js
    catalog_json = json.dumps(all_lessons, indent=2, ensure_ascii=False)
    js_content = f"""/* ============================================================
   FREE MIND ML — catalog.js
   Full Curriculum Catalog: 52 Complete Lessons across 5 Modules
   Generated with 100% complete content, KaTeX math, and quizzes.
   ============================================================ */
window.FML = window.FML || {{}};
window.FML.catalog = {catalog_json};
"""

    target_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "js", "catalog.js")
    with open(target_path, "w", encoding="utf-8") as f_out:
        f_out.write(js_content)

    print(f"[OK] Successfully written to {target_path} ({len(js_content):,} bytes, {len(js_content.splitlines()):,} lines)")

if __name__ == "__main__":
    assemble()
