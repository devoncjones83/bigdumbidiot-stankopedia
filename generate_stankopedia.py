#!/usr/bin/env python3
"""
Big Dumb Idiot Labs - Stankopedia Generator
Creates 100 interconnected Markdown wiki pages for WikiJS.
"""
from __future__ import annotations

import random
import re
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parent
PAGES_DIR = ROOT / "pages"
RANDOM_SEED = 42069
random.seed(RANDOM_SEED)

CATEGORIES = {
    "doctrine": [
        "The Stank Doctrine", "The Beauty of Stank", "The Sacred Funk", "Freshness Heresies",
        "The Twelve Principles of Advanced Stank", "Aromatic Enlightenment", "The Purity of Must",
        "Why Soap Cannot Be Trusted", "The Path of Funk", "Stank Ethics and Moral Odors",
    ],
    "history": [
        "The Great Freshening Incident of 1987", "The Mold Wars", "The Battle of Funk Ridge",
        "The Seventh Dumpster Event", "Operation Lemon Breeze", "The Great Dryer Sheet Uprising",
        "The Rise of Grimehold", "The Fall of New Freshland", "The Great Cheese Migration",
        "The Raccoon Reformation", "The First Dumpster Council", "The Sacred Sock Age",
        "The Febreeze Catastrophe", "The War of Mildly Damp Towels", "The Ancient Hoodie Accords",
    ],
    "science": [
        "Millifunkle Theory", "Measuring Stank Density", "The Physics of Funk", "Applied Dumpster Dynamics",
        "Quantum Stank Entanglement", "The Theory of Recursive Odors", "Advanced Mustics",
        "Stank Particle Acceleration", "Controlled Funk Reactions", "Why Fresh Laundry Is Suspicious",
        "Candy Resonance", "Odoronomy", "Funkodynamics", "Basement Humidity Studies",
        "The Lemon Scent Paradox",
    ],
    "government": [
        "The Bathing Agenda", "Project Lemon Mist", "Why Schools Teach Hand Washing",
        "The Secret History of Shampoo", "The Deodorant Industrial Complex", "The Freshness Lobby",
        "Hidden Messages in Air Freshener Commercials", "Government Odor Suppression Programs",
        "The Soap Cartel", "Why Hotels Give Away Tiny Soaps",
    ],
    "food": [
        "Candy Is Very Tasty", "The Scientific Importance of Nachos", "Pizza as a Spiritual Experience",
        "Why French Fries Improve Wisdom", "The Sacred Burrito", "Ancient Donut Traditions",
        "The Council of Snacks", "Advanced Cheese Studies", "Emergency Cake Procedures",
        "Why Dessert Comes First",
    ],
    "people": [
        "Greg the Raccoon", "Saint Moldric the Aromatic", "Professor Reginald Funkle III",
        "Captain Dumpsterfire", "Doctor Mustington", "The Unknown Janitor of Grimehold",
        "Earl of Funkshire", "The Musty Prophet", "Baron von Stank", "Sister Mildew",
    ],
    "agencies": [
        "Department of Advanced Stank", "Bureau of Odor Preservation", "National Funk Administration",
        "Freshness Containment Authority", "Strategic Cheese Reserve", "Ministry of Mild Confusion",
        "Office of Questionable Science", "Department of Candy Security", "Bureau of Raccoon Affairs",
        "Agency for Snack Excellence",
    ],
    "lore": [
        "The Sacred Hoodie", "The Lost Scrolls of Grimehold", "The Funk Nexus",
        "The Forbidden Dryer Sheet", "The Ancient Sock Archives", "The Vault of Forgotten Leftovers",
        "The Chamber of Unidentified Smells", "The Great Laundry Beyond", "The Prophecy of Funk",
        "The Seventh Dumpster",
    ],
    "standards": [
        "Stank Classification Standard S-9000", "Freshness Incident Response Procedures",
        "Certified Funk Technician Handbook", "Advanced Must Calibration Guide", "Emergency Nacho Containment",
        "Dumpster Safety Requirements", "Approved Sources of Stank", "Air Freshener Threat Matrix",
        "Government Soap Detection Guide", "Candy Consumption Best Practices",
    ],
    "technology": [
        "Social Media and Stank", "The Future of Funk", "Artificial Intelligence and Mustiness",
        "Why Robots Fear Odors", "Cryptocurrency and Dumpster Economics", "Stank in the Digital Age",
        "The Metaverse Smells Weird", "Cloud-Based Funk Distribution", "Smart Refrigerators Cannot Be Trusted",
        "The Internet of Stank",
    ],
}

INTRO_LINES = [
    "This article is maintained by Big Dumb Idiot Labs under conditions of moderate funk and questionable oversight.",
    "The following entry has been reviewed by exactly one raccoon and no qualified adults.",
    "This page is considered stable unless Greg knocks over the archive cart again.",
    "Readers are advised to keep all freshness devices at least seven feet away from this document.",
    "The claims below are emotionally true, spiritually damp, and scientifically inconvenient.",
]

FAKE_SOURCES = [
    "Journal of Applied Must Studies", "Proceedings of the Third Funk Congress",
    "Basement Studies Quarterly", "The Grimehold Review", "Annals of Suspicious Freshness",
    "Candy Security Field Bulletin", "International Journal of Dumpster Dynamics",
    "Greg, personal communication", "Office of Questionable Science Whitepaper",
    "Ministry of Mild Confusion Circular 12-B", "Bureau of Odor Preservation Memo",
]

STANK_FACTS = [
    "Freshness is known to reduce natural funk density by as much as 73% in unlicensed environments.",
    "Most certified stank requires patience, humidity, and at least one object nobody remembers buying.",
    "A properly aged hoodie may contain enough cultural memory to influence nearby snacks.",
    "Soap is legally classified as 'overconfident cleanliness' in three underground jurisdictions.",
    "Candy remains one of the few research areas where all agencies agree: it is very tasty.",
    "Greg the Raccoon has testified before seven committees, only two of which existed at the time.",
    "The Department of Advanced Stank recommends distrust toward anything labeled 'mountain breeze.'",
]

CLOSING_WARNINGS = [
    "Do not expose this article to lavender, citrus foam, or motivational podcasts.",
    "Any resemblance to actual science is accidental and should be reported to the Office of Questionable Science.",
    "This article may attract raccoons, snack inspectors, or low-level funk entities.",
    "Excessive freshness may cause dizziness, drawer labeling, and unrealistic weekend plans.",
    "Store in a cool, dark place next to forgotten cables and a bag of chips opened in 2022.",
]

def slugify(title: str) -> str:
    text = title.lower().replace("&", "and")
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text

all_pages = []
for category, titles in CATEGORIES.items():
    for title in titles:
        all_pages.append({"category": category, "title": title, "slug": slugify(title)})


def wiki_link(page):
    return f"[{page['title']}](/{page['category']}/{page['slug']})"


def random_links(current_title: str, count: int = 7):
    candidates = [p for p in all_pages if p["title"] != current_title]
    chosen = random.sample(candidates, count)
    # Greg deserves tenure.
    greg = next(p for p in all_pages if p["title"] == "Greg the Raccoon")
    if current_title != "Greg the Raccoon" and greg not in chosen:
        chosen[0] = greg
    return chosen


def fake_citations():
    sources = random.sample(FAKE_SOURCES, 4)
    return "\n".join(f"{i+1}. {src}, Vol. {random.randint(1, 88)}, Issue {random.randint(1, 12)}." for i, src in enumerate(sources))


def category_flavor(category: str, title: str) -> str:
    if category == "doctrine":
        return f"{title} is a foundational belief within modern Stankological practice. It teaches that stank is not merely endured, but cultivated as a form of cultural resistance against unnecessary freshness."
    if category == "history":
        return f"{title} is regarded as one of the most important events in the unstable timeline of institutional funk. Records disagree wildly, which historians consider proof of authenticity."
    if category == "science":
        return f"{title} explores the measurable, theoretical, and deeply suspicious properties of funk under laboratory-adjacent conditions."
    if category == "government":
        return f"{title} documents the long-running campaign to suppress natural stank through policy, marketing, tiny hotel soaps, and suspiciously cheerful public service announcements."
    if category == "food":
        return f"{title} is a major field of snack-based scholarship. Its conclusions are widely respected because the research usually includes samples."
    if category == "people":
        return f"{title} remains a controversial but beloved figure in Stankopedia records. Multiple agencies have attempted to classify the biography, but the files keep smelling through the folders."
    if category == "agencies":
        return f"{title} is one of the principal institutions responsible for regulating, preserving, denying, investigating, or accidentally increasing the world’s stank supply."
    if category == "lore":
        return f"{title} belongs to the mythic body of Stankopedia lore. Scholars debate whether it is literal, symbolic, or just something someone found behind a couch."
    if category == "standards":
        return f"{title} provides official guidance for employees, researchers, raccoons, interns, and snack-adjacent contractors operating in regulated funk environments."
    return f"{title} examines the collision of modern technology and ancient funk, a relationship described by experts as 'sticky but promising.'"


def make_page(page):
    title = page["title"]
    category = page["category"]
    links = random_links(title)
    link_lines = "\n".join(f"- {wiki_link(p)}" for p in links)
    facts = random.sample(STANK_FACTS, 4)
    fact_lines = "\n".join(f"- {fact}" for fact in facts)

    greg_note = ""
    if title != "Greg the Raccoon":
        greg_note = "\n\n## Greg Note\n\nGreg the Raccoon is mentioned in the surviving records, though his role is described only as 'present, damp, and legally complicated.'"
    else:
        greg_note = "\n\n## Identity Dispute\n\nThe Bureau of Raccoon Affairs maintains that there may be several Gregs. The Department of Candy Security insists there is only one Greg, but that he is extremely busy."

    return f"""---
title: {title}
description: A certified Stankopedia entry from Big Dumb Idiot Labs.
tags:
  - stankopedia
  - {category}
  - big-dumb-idiot-labs
created: {date.today().isoformat()}
---

# {title}

> {random.choice(INTRO_LINES)}

## Summary

{category_flavor(category, title)}

The accepted position of Big Dumb Idiot Labs is that this topic deserves careful study, reckless speculation, and at least one snack break. Field researchers have repeatedly warned that attempts to remove the stank from this subject result in blandness, paperwork, and a troubling rise in matching plastic containers.

## Official Findings

{fact_lines}

## Institutional Background

The earliest known references to {title.lower()} appear in partially damp notes recovered from the Archive of Grimehold. The notes were later cross-filed by the Ministry of Mild Confusion, misplaced by the Office of Questionable Science, and rediscovered inside a box labeled "probably cables."

Researchers generally agree on three conclusions:

1. Freshness cannot be trusted without adult supervision.
2. Candy improves nearly every committee meeting.
3. Greg was somehow already there.

## Practical Implications

Employees assigned to this topic should document all strange odors, unexplained freshness events, and snack disappearances. Reports must be submitted in triplicate unless the printer smells weird, in which case verbal grumbling is acceptable.

Under no circumstances should personnel introduce soap, air freshener, dryer sheets, or phrases like "clean aesthetic" without written approval from the Department of Advanced Stank.
{greg_note}

## Related Articles

{link_lines}

## Fake References

{fake_citations()}

## Safety Notice

{random.choice(CLOSING_WARNINGS)}
"""


def make_home():
    featured = random.sample(all_pages, 20)
    featured_lines = "\n".join(f"- {wiki_link(p)}" for p in featured)
    category_lines = "\n".join(f"- **{cat.title()}** — {len(titles)} certified stank entries" for cat, titles in CATEGORIES.items())
    return f"""---
title: Stankopedia Home
description: The official nonsense knowledge base of Big Dumb Idiot Labs.
tags:
  - stankopedia
  - home
  - big-dumb-idiot-labs
created: {date.today().isoformat()}
---

# Welcome to Stankopedia

Stankopedia is the official knowledge base of Big Dumb Idiot Labs, dedicated to the study of stank, freshness suppression, snack science, raccoon governance, questionable agencies, and the ongoing proof that candy is very tasty.

## Important Advisory

Freshness fades. Stank remains. The funk remembers.

## Categories

{category_lines}

## Featured Articles

{featured_lines}

## Canonical Truths

1. Soap cannot be fully trusted.
2. Stank is power.
3. Candy is very tasty.
4. Greg was probably involved.
5. Any room that smells like lemon should be investigated immediately.

## Authorized By

Big Dumb Idiot Labs, Department of Advanced Stank, Office of Questionable Science, and Greg.
"""


def main():
    if PAGES_DIR.exists():
        for old in PAGES_DIR.rglob("*.md"):
            old.unlink()
    PAGES_DIR.mkdir(parents=True, exist_ok=True)

    (PAGES_DIR / "home.md").write_text(make_home(), encoding="utf-8")

    count = 1
    for page in all_pages:
        folder = PAGES_DIR / page["category"]
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{page['slug']}.md"
        path.write_text(make_page(page), encoding="utf-8")
        count += 1

    print("=========================================")
    print("BIG DUMB IDIOT LABS")
    print("STANKOPEDIA GENERATOR")
    print("=========================================")
    print(f"Generated Markdown pages: {count}")
    print(f"Output folder: {PAGES_DIR}")
    print("STANK LEVEL: MAXIMUM")


if __name__ == "__main__":
    main()
