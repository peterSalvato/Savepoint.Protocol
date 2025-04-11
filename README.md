Savepoint.Protocol v1.0 — Canonical Public Release (2025-04-08)
# Savepoint.Protocol

> Canonical Public Release: v1.0 (2025-04-08)  
> Protocol Syntax Version: 3.0  
> Author: Peter Salvato  
> © 2025 Peter Salvato. All rights reserved.  
> All terminology, structure, and logic protected under custom license.

---

## Trace your thinking. Don’t just remember—author.  
*Savepoint is the machete, not the map.*

Savepoint.Protocol™ is a symbolic markup system for capturing cognitive turning points—moments when realization clicks, phrasing locks in, or meaning shifts direction.

It’s not memory. It’s authorship infrastructure.  
Built for thinkers in wild terrain.

---

## Semantic Cartography for the Mind

Thought doesn’t arrive in order. It arrives like a jungle—dense, recursive, and overgrown.  
Savepoint isn’t a vault. It’s a trail-marker protocol.

Each Savepoint is a deliberate semantic notch in your cognitive path:  
You were here. This mattered. Come back if needed.

---

## Why Savepoint Exists

As LLMs and systems adopt passive memory, the threat is no longer forgetting—  
It’s losing authorship.

- AI remembers facts  
- You remember meaning

Savepoints let you:
- Preserve phrasing that snapped things into place
- Mark realizations that reframed your model
- Log internal versions of your thinking as it evolved

Use it if you write, design, code, research, reflect, or resist.

---


## Use Cases

- Writers capturing final phrasing breakthroughs  
- Designers preserving layout metaphors or system shifts  
- Researchers logging conceptual pivots  
- Developers marking architecture-level insights  
- Philosophers noting directional changes in internal logic

---


## Canonical Syntax (v3.0)

Savepoints are declared using a self-closing tag:

```plaintext
<Savepoint
  protocol_version:3.0
  category:system_logic
  function:declaration
  timestamp:2025-04-08T15:43:00Z
  importance:high
  influence:Order of the Ætherwright
  # Recursive structures should replace version snapshots wherever drift is likely.
/>
```
## Required Fields:
```
    protocol_version: always declared (current = 3.0)
    category: domain of reflection (e.g. design_note, model_shift)
    function: purpose of the Savepoint (declaration, revision, drift_detected)
    timestamp: ISO 8601 UTC (e.g. 2025-04-08T15:43:00Z)
    #: final line, the semantic content
```
## Optional Fields:
```
    importance: high, medium, low
    confidence: self-assessed certainty
    influence: sources, systems, or individuals
```
See the full specification: /spec/savepoint-spec-v1.md


## CLI Tool

Savepoint CLI tool available for extracting ChatGPT exports into Savepoint sessions:

git clone https://github.com/peterSalvato/savepoint-protocol.git
cd savepoint-protocol
python cli/savepoint_split.py conversations.json

 - Converts conversations.json into timestamped Savepoint .md files
 - Produces Git-ready plaintext logs
 - Requires Python 3.7+

Tool location: /cli/savepoint_split.py


## Repository Structure

/spec/         → Canonical protocol syntax and rules  
/cli/          → CLI tools (e.g., log parser)  
/examples/     → Sample Savepoint sessions  
/.savepoints/  → Real-world authored Savepoints  
/docs/         → Extended philosophy and integration


## Philosophy

Savepoint is:
 - Low-tech
 - High-trust
 - Format-agnostic
 - Offline-compatible
 - Degradable across AI, shell, and analog workflows

It resists feature creep.
It honors inflection over information.
It assumes one thing: you’ll want to find your way back.

When the forest regrows, the Savepoints remain.

Read the full philosophy: /docs/philosophy.md


## License
Savepoint.Protocol is licensed under a custom humanist license.
Use freely. Fork deeply. But preserve authorship and intent.

See: /license.md


#### Author

Peter Salvato
Designer of authored infrastructure, symbolic tooling, and cognitive protocols.
Part of the broader system: Order of the Ætherwright
