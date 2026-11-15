# SETUP — from zero to your first `/today` (≈ 45 minutes, once)

Everything below is free, needs no card and no trial. Commands are for macOS (Apple Silicon).

## 1. Base tools
```bash
# Homebrew (skip if installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

brew install git gh uv gitleaks
brew install --cask temurin@17      # Java 17 for local PySpark (needed from Week 5)
brew install ollama                 # local LLMs (needed from Week 19 — install now, it's small)
```
Check: `git --version && uv --version && java -version`

## 2. Put the scaffold in place and make it a repo
```bash
mkdir -p ~/code && cd ~/code
unzip ~/Downloads/project-pulse.zip       # creates ~/code/project-pulse
cd project-pulse
cp .env.example .env                      # local only, git-ignored
make setup                                # uv sync + pre-commit hooks
make check                                # lint + types + tests → all green
```

## 3. GitHub (public repo = free CI minutes and a portfolio)
```bash
gh auth login                             # browser login, HTTPS
git init -b main
git add -A
git commit -m "chore: scaffold Project Pulse 2.0"
gh repo create project-pulse --public --source=. --push
```
Then on GitHub → Settings → Branches: protect `main`, require the `ci` check to pass.
Use a **personal** GitHub account — never push employer code or data here.

## 4. Databricks Free Edition (needed from Week 6; sign up now so it's ready)
1. Sign up at databricks.com/learn/free-edition (email or Microsoft login, no card).
2. Optional: verify with LinkedIn in the account settings — this unlocks outbound internet and
   higher limits. Without it, ingestion stays local and files are uploaded to a Volume.
3. Install the CLI: `brew tap databricks/tap && brew install databricks`
4. `databricks auth login --host https://<your-workspace-url>` (stores a profile in
   `~/.databrickscfg`, outside the repo).
5. Log in at least once a week — inactive Free Edition accounts can be deleted.

## 5. Make Claude your tutor
**Claude Code (recommended)** — open a terminal in the repo and run `claude`, or open the
folder in the Claude desktop app's Code tab. It loads `CLAUDE.md`, the `pulse-tutor` skill and
the slash commands automatically because they live in `.claude/`.

**Claude desktop chat (no terminal)** — zip `.claude/skills/pulse-tutor/`, upload it as a
custom skill in Claude's settings, and connect the repo folder so Claude can read `PROGRESS.md`
and the journal. Claude Code is better here because it can run your tests.

## 6. The daily ritual (60 minutes)
```
cd ~/code/project-pulse && git pull && claude
/today          → read the mission, answer the design questions
  …build…       → /check to get reviewed, /hint when stuck (one rung at a time)
/wrap           → journal + PROGRESS update + commit message
git add -A && git commit -m "<message from /wrap>" && git push
```
Saturday: `/chaos` · Sunday: `/today` runs the weekly quiz, challenge and retro.
Anytime: `/status`, `/quiz`, `/challenge`.

## 7. Rules you agreed to
- Attempt before answers. Hints come in rungs.
- No secrets in git. Ever. (pre-commit + gitleaks will catch you — that's the point.)
- One commit minimum per day. The streak lives in `PROGRESS.md` and in your GitHub graph.
- Don't read `.claude/skills/pulse-tutor/references/chaos-*.md` or the Chaos Mart server code.
