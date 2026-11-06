# Setup

## Windows
1. Install Python 3.10+ from python.org (check "Add to PATH").
2. Open PowerShell in the repo folder.
3. `python -m venv .venv`
4. `.venv\Scripts\activate`
5. `pip install -r requirements.txt`
6. `copy .env.example .env` and edit keys.
7. `python check_setup.py`

## macOS
1. `brew install python`
2. `python3 -m venv .venv`
3. `source .venv/bin/activate`
4. `pip install -r requirements.txt`
5. `cp .env.example .env`
6. `python check_setup.py`

## Linux
Same as macOS with apt-get install python3 python3-venv.

## cs50.dev / Codespaces
Open repo in Codespaces; devcontainer installs deps automatically.

## OpenRouter (recommended for class)
Get a key at https://openrouter.ai/keys and put it in .env as OPENAI_API_KEY with base_url https://openrouter.ai/api/v1.

## Ollama fallback (optional)
Install Ollama, `ollama serve`, `ollama pull llama3.2`.
