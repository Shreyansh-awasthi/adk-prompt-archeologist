# Prompt Archeologist

An AI agent that reverse-engineers AI outputs. Paste in a response from any chatbot, and the agent works backwards to uncover the prompt that likely produced it.

Built with [Google ADK](https://google.github.io/adk-docs/), [LiteLLM](https://docs.litellm.ai/), and a Qwen model hosted on [Groq](https://console.groq.com/).

## Features

- **Likely system prompt**: a reconstructed persona and instruction blueprint
- **Constraints**: the explicit and implicit rules the model appears to follow
- **Variables & syntax**: placeholders and formatting patterns found in the output
- **Ready-to-use template**: a copy-paste prompt you can use to reproduce the behavior
- **Fast responses**: runs on Groq's low-latency inference
- **Easy to customize**: change the agent's behavior by editing a single instruction string

## Project structure

```
Google_ADK_Proj/
├── __init__.py
├── agent.py
├── requirements.txt
├── README.md
└── .env
```

## Getting started

**1. Create and activate a virtual environment**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**2. Install dependencies**

```powershell
pip install -r requirements.txt
```

**3. Add your Groq API key**

Create a key at https://console.groq.com/keys and save it in `.env`:

```
GROQ_API_KEY=your-key-here
```

**4. Create `__init__.py`**

```powershell
Set-Content -Path __init__.py -Value "from . import agent"
```

**5. Start the app**

Run this from the folder that contains `Google_ADK_Proj`:

```powershell
adk web
```

Open http://127.0.0.1:8000, select `Google_ADK_Proj`, click **+ New Session**, and start chatting.

## Usage

Paste any AI-generated text and ask the agent to analyze it:

```
Reverse-engineer the prompt behind this AI output:

"""
Great question! Here's a quick breakdown:

**What it is:** A REST API lets two programs talk over HTTP.

**Key points:**
- Uses GET, POST, PUT, DELETE
- Returns JSON
- Stateless

**TL;DR:** It's a standard way for apps to exchange data.

Want me to show a code example?
"""
```

The agent responds with the three sections above, plus a prompt template you can reuse.

### Tips for great results

- Use longer samples (4 to 10 lines) so the agent can see structure and tone.
- Add context, such as the question the user asked or formatting rules you noticed.
- Ask for a single section, for example: "Give me only the CONSTRAINTS section."

## Customization

**Change the model**: edit the `model=` line in `agent.py`:

```python
model="groq/qwen/qwen3.8-27b"
```

**Change the behavior**: edit `archeologist_instructions` in `agent.py` to add new sections, change the tone, or focus on a specific output type.

## Tech stack

| Component | Purpose |
|---|---|
| Google ADK | Agent framework and dev UI |
| LiteLLM | Unified model connector |
| Groq | Fast model hosting |
| Qwen | Language model |
| python-dotenv | Environment variable loading |

## Security

Keep your `.env` file private and out of version control. If you use Git, add this to `.gitignore`:

```
.env
.venv/
__pycache__/
```