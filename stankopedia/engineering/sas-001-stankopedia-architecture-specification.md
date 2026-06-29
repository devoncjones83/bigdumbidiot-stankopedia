---
title: SAS-001 — STANKOPEDIA Architecture Specification
description: Defines the information architecture, document taxonomy, and control boundaries for STANKOPEDIA.
published: true
date: 2026-06-29T02:19:40.074Z
tags: stankopedia, big-dumb-idiot-labs
editor: markdown
dateCreated: 2026-06-29T02:19:40.074Z
---

# SAS-001 — STANKOPEDIA Architecture Specification

## 1. Purpose

This specification defines the architecture of STANKOPEDIA.

STANKOPEDIA is not a single-purpose wiki. It is a combined engineering standard, project record system, publishing pipeline, and institutional knowledge base.

The purpose of this document is to separate controlled engineering material from reference material while preserving all existing Wombats, registries, lore, random pages, and generated knowledge-base collections.

## 2. Architecture Statement

STANKOPEDIA contains four major systems:

1. **Engineering Standard** — canonical STANK methodology and controlled project execution rules.
2. **Knowledge Base** — informational, fictional, reference, lore, Wombat, and exploratory pages.
3. **Project Records** — requirements, decisions, ECOs, production asset records, and current work products.
4. **Publishing System** — scripts, generated pages, WikiJS upload logic, backups, and rendering support.

These systems may live in the same repository, but they must be classified separately.

## 3. Canonical Source Rule

The engineering source of truth is the controlled Markdown source in the repository.

WikiJS is a published rendering target.

SQL exports are backups or migration artifacts. They are not the preferred editing source unless explicitly designated during recovery.

## 4. Document Classes

| Class | Name | Function |
|---|---|---|
| SAS | STANKOPEDIA Architecture Specification | Defines STANKOPEDIA structure and governance. |
| SEP | STANK Engineering Principle / Program Standard | Defines mandatory methodology and program-level principles. |
| STD | Standard | Defines enforceable rules for a domain. |
| WF | Workflow | Defines ordered process execution. |
| SR | Requirement | Defines approved project requirements. |
| ECO | Engineering Change Order | Authorizes one scoped production change. |
| DL | Decision Log | Records engineering decisions and rationale. |
| REG | Registry | Maintains controlled indexes and inventories. |
| TMP | Template | Provides approved artifact starting formats. |
| CHK | Checklist | Defines review or acceptance criteria. |
| REF | Reference | Provides non-mandatory explanatory material. |
| WOM | Wombat | Living knowledge, exploratory documentation, or institutional oddity. |

## 5. Mandatory Page Header

Every controlled engineering page should declare:

- Document ID
- Document Type
- Status
- Owner
- Source of Truth
- Last Reviewed

Example:

```text
Document ID: SEP-001
Document Type: Engineering Standard
Status: Draft / Active / Deprecated / Archived
Owner: Big Dumb Idiot Labs
Source of Truth: Repository Markdown
Last Reviewed: YYYY-MM-DD
```

## 6. Authority Levels

| Level | Meaning |
|---|---|
| Canonical | Binding STANK rule or production record. |
| Controlled | Reviewed and maintained, but not necessarily binding. |
| Reference | Informational support material. |
| Experimental | Useful but unstable. |
| Archive | Preserved, not current. |

## 7. Preservation Rule

Existing pages must not be deleted merely because they are weird, old, random, or generated.

During reorganization, every page receives one of these treatments:

1. Promote to engineering standard.
2. Register as reference.
3. Preserve in knowledge collection.
4. Preserve as Wombat.
5. Archive with explanation.

## 8. Visual Review Goal

The published STANKOPEDIA home page must make the system understandable in under thirty seconds.

A reader should be able to identify:

- where the engineering standard lives,
- where Wombats live,
- where registries live,
- where original knowledge collections live,
- which pages are binding,
- which pages are informational.

## 9. Related Pages

- [STANKOPEDIA Home](/stankopedia)
- [Engineering Standards](/stankopedia/engineering/standards)
- [Registries](/stankopedia/registries)
- [Wombats](/stankopedia/wombats)
