# GPT Terminal

![GPT Terminal banner](GPT_Terminal@4x.png)

A **command-line AI assistant** with customizable preheaders for style and formatting — talk to GPT from the terminal, tweak mode / tokens / rate, keep the vibe yours.

Part of the [Initial Visuals](https://github.com/initialvisuals) toolkit / game lab.

### Status

**Archive / inspiration.** Last maintained around mid-2024. Left up as a reference for later CLI tools. It may still run against a modern OpenAI client with small fixes; treat it as a starting point, not production.

Demo: [YouTube](https://www.youtube.com/watch?v=FRTy8jV2FTo)

### Quick start

```bash
git clone https://github.com/initialvisuals/GPT_Terminal.git
cd GPT_Terminal
pip install -r requirements.txt
```

Set your key (never commit it):

```bash
# Linux / macOS
export OPENAI_API_KEY=your_api_key

# Windows (cmd)
set OPENAI_API_KEY=your_api_key
```

```bash
python ai.py
```

Optional alias (Linux / macOS) — add to your shell profile:

```bash
alias ai="python /path/to/GPT_Terminal/ai.py"
```

Inside the session, type `help` for settings (mode, preheader, rate, tokens, …).

### Related

Minimal chat sketch: [`gpt4_boilerplate`](https://github.com/initialvisuals/gpt4_boilerplate).

### License

MIT — see [LICENSE](LICENSE).

---

**Initial Visuals** — tools, sims, games, and experiments.
