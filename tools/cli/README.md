
# Savepoint Protocol CLI

A semantic CLI toolkit for extracting, indexing, and managing cognitive artifacts from exported ChatGPT conversations.

This CLI is part of the larger [Savepoint Protocol](https://github.com/peterSalvato/Savepoint.Protocol) system, and is designed to enable clean, author-level control over archived thought, recursive journaling, and LM-based workflows.

---

## ✅ Installation

From inside the `tools/cli/` directory of the repo:

```bash
pip install -e .
```

This will install the CLI globally as the `sp` command.

---

## 📦 Usage

### Extract conversations into individual `.md` files

```bash
sp extract --prefix AE
```

- Filters only conversations whose title starts with `AE`
- Outputs one `.md` file per conversation in `./exports/`
- Each message includes a dual timestamp:
  ```
  [2025-04-01T14:03:12Z | Apr 1, 2025 – 2:03 PM] [user]
  ```

### Extract Savepoints (in progress)

```bash
sp savepoint extract --prefix AE --suffix journal --dates 2025-04-01:2025-04-15
```

---

## 🔮 Roadmap

### Phase 1: Extraction & Structure
- [x] Per-conversation `.md` file creation
- [x] Prefix filtering
- [x] Dual timestamp per message
- [ ] Frontmatter metadata
- [ ] `.meta.md` export manifest

### Phase 2: Savepoint-Awareness
- [x] Savepoint extraction from messages
- [ ] Savepoint validation
- [ ] Savepoint timeline tracing
- [ ] Savepoint grafting

### Phase 3: LM Optimization
- [ ] NotebookLM-friendly exports
- [ ] Constraint-aware headers
- [ ] Manifest tagging

---

## 🧠 Philosophy

This tool is designed not for casual users, but for thinkers, authors, and recursive systems architects who want to track the evolution of their ideas with surgical fidelity.

It is non-destructive by default and structured to grow with your thought systems.

> Clarity is recursive. So is authorship.

---

Maintained by [Peter Salvato](https://github.com/peterSalvato)
