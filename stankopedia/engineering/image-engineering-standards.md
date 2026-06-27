---
title: Image Engineering Standards
description: Canonical standards for STANK image engineering workflows, production assets, and engineering review.
published: true
date: 2026-06-27T00:00:00.000Z
tags: engineering, image-engineering, standards, eco, production-assets
editor: markdown
dateCreated: 2026-06-27T00:00:00.000Z
---

# Image Engineering Standards

| Field | Value |
|---|---|
| Document ID | IES-001 |
| Current Revision | Rev A |
| Status | Approved |
| Owner | STANK Engineering |
| Controlled Copy | Yes |
| Supersedes | None |
| Effective Date | 2026-06-27 |

## 1. Purpose

This standard defines the engineering controls governing AI-generated production imagery used by STANK projects.

The objective is controlled image engineering, not uncontrolled image creation. All production image work shall be executed through one of the approved workflows defined in this document.

## 2. Scope

This standard applies to all production-bound image assets, including interface components, panels, headers, footers, shells, frames, icons, status displays, decorative hardware, and supporting visual assets.

This standard applies to three canonical image workflows:

1. Restoration
2. Engineering Change Order
3. New Production Asset

## 3. Definitions

### 3.1 Production Master

An approved, immutable production image asset that defines the authoritative manufacturing specification for future revisions.

### 3.2 Candidate Revision

A temporary engineering output generated for review. A Candidate Revision is not authoritative unless promoted to Production Master.

### 3.3 Engineering Change Order

A controlled, single-scoped revision to an existing Production Master.

### 3.4 Restoration

A controlled process used to repair, clean, upscale, or prepare an existing asset without redesigning it.

### 3.5 New Production Asset

A newly created asset that does not yet have an approved Production Master.

### 3.6 Reference Hierarchy

The ordered authority structure used to resolve conflicts between supplied references, written requirements, and model assumptions.

## 4. Universal Engineering Principles

### Principle 0 — The Requirements Are Sacred

The written requirements constitute the engineering contract.

No requirement may be ignored, substituted, generalized, or creatively reinterpreted.

If requirements conflict, the conflict shall be resolved before production.

### Principle 1 — Engineering, Not Art

Image generation shall be treated as an engineering process.

The objective is controlled implementation. Creative interpretation is permitted only where explicitly authorized.

### Principle 2 — Minimal Necessary Change

Only the components identified by the engineering requirements may change.

Everything outside the approved scope is frozen.

### Principle 3 — Deterministic Output Intent

Outputs should be reproducible in structure, intent, and engineering behavior.

Incidental visual drift shall be minimized.

### Principle 4 — Preservation of Approved Work

Previously approved engineering work shall not regress.

Each revision inherits all approved improvements unless explicitly superseded.

### Principle 5 — Reference Hierarchy Controls the Output

References shall be ordered by authority.

When references conflict, the higher-authority reference shall control the output.

### Principle 6 — Localized Engineering

Every change shall be treated as replacing one physical hardware module on an existing manufactured system.

A localized change shall not trigger reconstruction of the entire asset.

### Principle 7 — Manufacturing Mindset

Every visible object is assumed to be a manufactured component.

Materials, geometry, fasteners, weathering, tolerances, labels, lighting, and wear shall remain physically believable.

### Principle 8 — Production Assets Are Immutable

Approved Production Masters shall never be modified in place.

Engineering work produces Candidate Revisions. Promotion occurs only after Engineering Review.

## 5. Engineering Asset Lifecycle

All production-bound image assets shall follow the controlled lifecycle below.

```text
Requirements
  ↓
Reference Collection
  ↓
Engineering Prompt
  ↓
Candidate Revision
  ↓
Engineering Review
  ↓
Approved Production Master
  ↓
Engineering Change Order, when future revision is required
```

Rejected candidates terminate at Engineering Review.

Rejected or unapproved AI generations shall not be used as future reference assets.

## 6. Canonical Image Workflows

Every image task shall use exactly one workflow.

### 6.1 Workflow A — Restoration

#### Purpose

Restore an existing production asset without redesign.

#### Authorized Uses

Restoration may be used for:

- damage repair
- resolution enhancement
- material fidelity improvement
- transparency correction
- artifact removal
- noise cleanup
- production preparation

#### Authority Model

The supplied production asset is the source of truth.

Supporting references may demonstrate quality targets, but they shall not override the production asset.

#### Output

The output is a production-equivalent restored asset.

No design changes are authorized.

### 6.2 Workflow B — Engineering Change Order

#### Purpose

Modify one approved Production Master through a tightly controlled engineering revision.

#### Required Characteristics

An ECO shall have:

- one scoped change or one explicitly bounded change set
- a named Production Master
- a clear Reference Hierarchy
- explicit frozen components
- a Candidate Revision output
- Engineering Review before promotion

#### Authority Model

The latest approved Production Master is the highest-authority visual reference.

Supporting candidate images may demonstrate approved improvements, but they shall not become the source of truth unless promoted.

#### Output

The output is a Candidate Revision.

A Candidate Revision becomes a Production Master only after passing Engineering Review.

### 6.3 Workflow C — New Production Asset

#### Purpose

Create a new production asset when no Production Master exists.

#### Required Characteristics

A New Production Asset workflow shall include:

- complete dimensional requirements
- intended use
- visual system requirements
- material requirements
- transparency requirements
- integration requirements
- acceptance criteria

#### Authority Model

Written requirements and approved design references establish the initial manufacturing specification.

#### Output

The output becomes the initial Production Master only after Engineering Review and Production Acceptance.

## 7. Universal Prompt Contract

Every production image prompt shall contain the following sections.

### 7.1 Asset Identification

The prompt shall identify:

- asset name
- workflow type
- revision identifier
- target output filename
- production status

### 7.2 Objective

The prompt shall define exactly what is being produced.

### 7.3 Reference Hierarchy

The prompt shall identify each reference and its authority level.

### 7.4 Engineering Scope

The prompt shall define exactly what may change.

### 7.5 Frozen Components

The prompt shall explicitly define what shall remain unchanged.

### 7.6 Manufacturing Requirements

The prompt shall define required handling of:

- materials
- lighting
- geometry
- fasteners
- weathering
- typography
- physical realism
- transparency
- resolution
- aspect ratio

### 7.7 Acceptance Criteria

The prompt shall define objective pass/fail conditions.

### 7.8 Deliverables

The prompt shall define output files, format, dimensions, and transparency behavior.

## 8. Engineering Prompt Invariants

The following invariant clauses shall be included in every production-bound image prompt unless explicitly superseded by a later revision of this standard.

### 8.1 Requirements Clause

```text
Principle 0 applies: The requirements are sacred.
Do not ignore, reinterpret, generalize, or substitute any requirement.
```

### 8.2 Engineering Clause

```text
This is an engineering task, not concept art, not redesign, and not creative exploration.
Execute the specified workflow only.
```

### 8.3 Scope Control Clause

```text
Only modify the components explicitly authorized in the Engineering Scope.
Everything else is frozen.
```

### 8.4 Reference Authority Clause

```text
If any reference conflicts with a higher-authority reference, the higher-authority reference wins.
If a written requirement conflicts with the Production Master outside the approved change scope, preserve the Production Master.
```

### 8.5 Production Master Clause

```text
The Production Master is immutable.
Do not create future revisions from rejected or unapproved candidates.
Use the latest approved Production Master as the only source of truth for preserved visual details.
```

### 8.6 Localized Engineering Clause

```text
Treat the requested change as replacing one hardware module on an existing industrial control console.
Do not rebuild the entire asset.
```

### 8.7 Regression Prevention Clause

```text
Preserve all previously approved engineering improvements unless explicitly superseded by this task.
```

### 8.8 Transparency Clause

```text
Transparent regions shall remain fully transparent.
Do not add a background canvas, matte, halo, glow field, or unintended opaque pixels outside the physical asset.
```

## 9. Production Master Standard

A Production Master defines the authoritative manufacturing specification for an approved image asset.

A Production Master controls:

- geometry
- dimensions
- aspect ratio
- panel proportions
- spacing
- module placement
- rivet placement
- screw placement
- handle placement
- bolt placement
- typography
- lighting
- steel construction
- coloring
- weathering
- transparency behavior
- display appearance
- approved prior ECOs

Production Masters shall be immutable.

Future revisions shall use the latest approved Production Master as the highest-authority visual reference.

## 10. Candidate Revision Standard

Candidate Revisions are temporary engineering artifacts.

A Candidate Revision may be:

- approved
- approved with required corrections
- rejected

Rejected Candidate Revisions shall not be used as future reference assets.

Approved Candidate Revisions shall not become authoritative until promoted to Production Master.

## 11. Engineering Review

Every Candidate Revision shall undergo Engineering Review before promotion.

Engineering Review shall verify:

- requirement compliance
- scope compliance
- unintended visual drift
- manufacturing consistency
- typography integrity
- transparency correctness
- dimensional accuracy
- regression against the Production Master
- preservation of approved prior ECOs

## 12. Engineering Review Checklist

Each review item shall be marked Pass, Fail, or Not Applicable.

### 12.1 Scope

- Only approved components changed
- No unauthorized redesign introduced
- Engineering scope fully satisfied
- No model-invented elements added

### 12.2 Geometry

- Dimensions preserved or intentionally revised
- Aspect ratio preserved
- Alignment preserved
- Spacing preserved
- Panel geometry preserved

### 12.3 Manufacturing

- Materials remain consistent
- Hardware remains consistent
- Rivets preserved
- Fasteners preserved
- Handles preserved
- Bolts preserved
- Weathering remains physically believable

### 12.4 Visual Integrity

- Typography preserved unless explicitly revised
- Lighting preserved
- Colors preserved
- CRT/display appearance preserved where applicable
- Approved prior improvements preserved

### 12.5 Transparency

- Required transparent regions verified
- No unintended background pixels
- No opaque canvas outside physical hardware
- No unwanted matte or halo

### 12.6 Regression

- No approved feature lost
- No rejected candidate details introduced
- Latest Production Master faithfully maintained
- Prior ECOs preserved unless superseded

## 13. Production Promotion

Promotion requires successful Engineering Review.

The promotion lifecycle is:

```text
Production Master
  ↓
Engineering Change Order
  ↓
Candidate Revision
  ↓
Engineering Review
  ↓
New Production Master
```

Previous Production Masters shall remain archived for historical traceability.

## 14. Prohibited Practices

The following practices are prohibited:

- rebuilding an asset from memory
- creative redesign during Restoration
- global changes during localized ECO work
- using rejected candidates as references
- using unapproved AI generations as future reference assets
- mixing multiple candidate revisions into a single source of truth
- allowing model interpretation to override requirements
- changing components outside the approved scope
- omitting the Production Master from Restoration or ECO workflows unless no Production Master exists
- treating an ECO as a new image generation task

## 15. Workflow Templates

### 15.1 Restoration Prompt Template

```text
# STANK IMAGE ENGINEERING TASK

Workflow: Restoration
Asset: [asset name]
Production Master: [filename]
Target Output: [filename]

Principle 0 applies: The requirements are sacred.
This is an engineering task, not concept art, not redesign, and not creative exploration.

Objective:
[Define restoration objective.]

Reference Hierarchy:
1. Reference A — Production Master — authoritative for all geometry, proportions, typography, hardware, weathering, lighting, and transparency behavior.
2. Reference B — Supporting quality reference, if provided — non-authoritative.

Engineering Scope:
[Define restoration-only changes.]

Frozen Components:
Everything not explicitly listed in Engineering Scope is frozen.

Manufacturing Requirements:
[Define material, lighting, transparency, and production constraints.]

Acceptance Criteria:
[Define pass/fail review criteria.]

Deliverable:
[filename, dimensions, format]
```

### 15.2 Engineering Change Order Prompt Template

```text
# STANK IMAGE ENGINEERING CHANGE ORDER

Workflow: Engineering Change Order
ECO ID: [ECO-###]
Production Master: [filename]
Candidate Output: [filename]

Principle 0 applies: The requirements are sacred.
This is an engineering task, not concept art, not redesign, and not creative exploration.
Treat the requested change as replacing one hardware module on an existing industrial control console.

Reference Hierarchy:
1. Reference A — Production Master — authoritative for all preserved details.
2. Reference B — Approved improvement reference, if provided — authoritative only for explicitly approved changes.

Engineering Scope:
[Define the single scoped change.]

Frozen Components:
All components outside Engineering Scope are frozen.
Preserve every rivet, screw, fastener, panel, module, label, display, weathering pattern, and spacing unless explicitly listed in Engineering Scope.

Regression Controls:
Preserve all previously approved engineering improvements unless explicitly superseded.
Rejected or unapproved candidates shall not be used as references.

Acceptance Criteria:
[Define pass/fail review criteria.]

Deliverable:
[filename, dimensions, format]
```

### 15.3 New Production Asset Prompt Template

```text
# STANK NEW PRODUCTION ASSET TASK

Workflow: New Production Asset
Asset: [asset name]
Target Output: [filename]

Principle 0 applies: The requirements are sacred.
This is an engineering task, not concept art, not redesign, and not creative exploration.

Objective:
[Define new asset purpose.]

Requirements:
[Define dimensions, use case, design system, material requirements, transparency behavior, and integration constraints.]

Reference Hierarchy:
[Define authority of supplied references.]

Manufacturing Requirements:
[Define material, typography, hardware, weathering, lighting, and physical realism requirements.]

Acceptance Criteria:
[Define pass/fail review criteria.]

Deliverable:
[filename, dimensions, format]
```

## 16. Revision History

| Revision | Date | Description | Approval |
|---|---:|---|---|
| Rev A | 2026-06-27 | Initial release. Formalized Restoration, Engineering Change Order, New Production Asset workflows, universal engineering principles, prompt invariants, lifecycle controls, review checklist, and production promotion standard. | Approved |
