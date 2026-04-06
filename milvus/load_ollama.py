import requests
import sys
import json


def ensure_ollama_model(model: str, base_url: str) -> None:
    tags_url = f"{base_url}/api/tags"
    pull_url = f"{base_url}/api/pull"
    try:
        resp = requests.get(tags_url, timeout=5)
        resp.raise_for_status()
        installed = {m["name"] for m in resp.json().get("models", [])}
    except requests.exceptions.ConnectionError:
        print(f"[FATAL] Cannot reach Ollama at {base_url}.")
        sys.exit(1)
    except Exception as exc:
        print(f"[FATAL] Ollama check failed: {exc}")
        sys.exit(1)

    if model in installed or f"{model}:latest" in installed:
        print(f"  Model '{model}' already installed.")
        return

    print(f"  Pulling '{model}' (~958 MB) ...")
    try:
        with requests.post(pull_url, json={"name": model, "stream": True},
                           stream=True, timeout=600) as r:
            r.raise_for_status()
            for raw in r.iter_lines():
                if not raw:
                    continue
                try:
                    ev = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                total = ev.get("total", 0)
                done  = ev.get("completed", 0)
                if total and done:
                    pct   = done / total * 100
                    bar   = "█" * int(30 * done / total) + "░" * (30 - int(30 * done / total))
                    print(f"\r  [{bar}] {pct:5.1f}%", end="", flush=True)
                elif ev.get("status"):
                    print(f"\r  {ev['status']:<50}", end="", flush=True)
        print(f"\n  '{model}' ready.\n")
    except Exception as exc:
        print(f"\n[FATAL] Pull failed: {exc}")
        sys.exit(1)

