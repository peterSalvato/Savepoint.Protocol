
from pathlib import Path
from datetime import datetime, timezone
import json

def run(args):
    source = Path(args.source) if args.source else Path("conversations.json")
    output_dir = Path(args.output) if args.output else Path("exports")
    prefix = args.prefix or ""

    try:
        with open(source, "r", encoding="utf-8") as f:
            conversations = json.load(f)
    except Exception as e:
        print(f"❌ Failed to read source file: {e}")
        return

    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for convo in conversations:
        title = convo.get("title", "").strip()
        if prefix and not title.startswith(prefix):
            continue

        safe_title = title.replace(" ", "").replace(":", "").replace("/", "-")
        filename = output_dir / f"{safe_title}.md"
        messages = []

        for msg_id, msg in convo.get("mapping", {}).items():
            message = msg.get("message")
            if not message:
                continue
            role = message.get("author", {}).get("role", "unknown")
            ts_raw = message.get("create_time")
            iso = human = "unknown-time"
            if ts_raw:
                dt = datetime.fromtimestamp(ts_raw, tz=timezone.utc)
                iso = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
                human = dt.strftime("%b %d, %Y – %-I:%M %p")
            parts = message.get("content", {}).get("parts", [])
            for part in parts:
                if isinstance(part, str):
                    messages.append(f"[{iso} | {human}] [{role}]\n{part.strip()}\n")
                else:
                    messages.append(f"[{iso} | {human}] [{role}]\n[Non-string content skipped]\n")

        with open(filename, "w", encoding="utf-8") as out:
            out.write("\n---\n\n".join(messages))

        count += 1

    print(f"✅ Exported {count} conversations to: {output_dir}")
