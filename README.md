Savepoint.Protocol v1.0 — Canonical Public Release (2025-04-08)
# Savepoint.Protocol

> Authored by Peter Salvato
> Protocol Version: 3.0  
> Repository Release: 1.0  
> © 2025 Peter Salvato. All rights reserved. All terminology, structure, and logic protected.

---

# Savepoint.Protocol

> **Canonical Public Release**: v1.0 (2025-04-08)  
> **Protocol Syntax Version**: 3.0  
> **Author**: Peter Salvato  
> © 2025 Peter Salvato. All rights reserved.  
> All terminology, structure, and logic protected under custom license.

---

## Trace your thinking. Don’t just remember—author.  
*Savepoint is the machete, not the map.*

**Savepoint.Protocol** is a semantic markup system for capturing **cognitive turning points**—the precise moments when realization clicks, phrasing locks in, or meaning shifts direction.

It’s not about memory. It’s **authorship infrastructure**.  
Built for thinkers in wild terrain.

---

## Semantic Cartography for the Mind

> Thought doesn’t arrive in order. It arrives like a jungle—dense, recursive, and overgrown.  
> Savepoint isn’t a vault. It’s a **trail-marker protocol**.

Each Savepoint is a semantic notch in your cognitive path:  
You were **here**. This **mattered**. Come back **if needed**.

---

## Why Savepoint Exists

As LLMs, systems, and apps build passive memory, the threat is no longer forgetting.  
It’s **losing authorship**.

- AI remembers facts.  
- **You** capture meaning.

Savepoints let you:
- Preserve phrases that *snapped things into place*  
- Mark realizations that *reframed your entire model*  
- Log internal versions of your thinking as it **actually evolved**

Savepoint is for writers, researchers, designers, developers—  
**anyone who thinks recursively and wants to leave a trail.**

---

## Canonical Syntax (v3.0)

Savepoints use a **self-closing tag** with strict symbolic rules:

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
Required Fields

    protocol_version: always declared (current = 3.0)

    category: the domain or focus area (design_note, model_shift, etc.)

    function: the role of this Savepoint (declaration, revision, drift_detected, etc.)

    timestamp: UTC ISO 8601 (2025-04-08T15:43:00Z)

    # content line: your actual semantic inflection

Optional Fields

    importance: high, medium, low

    confidence: self-assessed certainty

    influence: attributed origin (person, work, system)

→ Full syntax spec: /spec/savepoint-spec-v1.md
How It Works

Each Savepoint session is a plaintext .md log—
Lightweight. Versionable. Human-authored. Machine-readable.

Write Savepoints manually
OR extract them from AI logs, shell output, or analog tools.
Use Cases

    Writers capturing final phrasing breakthroughs

    Designers preserving spatial or system logic shifts

    Researchers logging conceptual pivots

    Developers marking architecture-level insight

    Philosophers tracing when internal logic evolved

CLI Tool

Savepoint CLI tool now available for ChatGPT export parsing.

git clone https://github.com/peterSalvato/savepoint-protocol.git
cd savepoint-protocol
python cli/savepoint_split.py conversations.json

    Converts conversations.json into individual Savepoint .md sessions

    Outputs timestamped, Git-ready files

    Requires Python 3.7+

Repo Structure

/spec/         → Canonical protocol format + syntax
/cli/          → Functional tools (e.g., log extractor)
/examples/     → Example Savepoint sessions
/.savepoints/  → Real-world authored logs
/docs/         → Extended doctrine + integrations

Philosophy

Savepoint.Protocol is intentionally:

    Low-tech

    High-trust

    Degradable across formats

    Stack-agnostic and offline-capable

It resists feature creep.
It honors inflection over information.
It assumes one thing: you’ll want to find your way back.

    When the forest regrows, the Savepoints remain.

→ Read the full philosophy
License

Licensed under a custom humanist license:
Use freely. Fork deeply. But preserve authorship and intent.

See: license.md
Author

Peter Salvato
Designer of authored infrastructure, symbolic tooling, and cognitive protocols.
Part of the broader system architecture behind Order of the Ætherwright.
