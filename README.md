# YSOT CS50-Style Course

The main repository for YSOT's CS50-style learning programme. Each topic we learn
and teach lives in its own self-contained module (a folder at the top level), so
modules can grow, be set up, and be tested independently.

## Modules

| Module | Topic | Stack | Status |
| --- | --- | --- | --- |
| [`ai-for-beginners/`](ai-for-beginners/) | Introduction to Artificial Intelligence: a 6-session, hands-on course with a "Game Night" tic-tac-toe capstone | Python 3.10+ | In progress |
| [`python-daily-practice/`](python-daily-practice/) | A small Python exercise every day: one `Day N` folder each, with a README that explains how to do the task, starter code and tests | Python 3.10+ | In progress |

> More modules will be added here as new concepts are introduced.

## For students: how to contribute

New assignments are added to this repository regularly (for the daily Python
practice, a new `Day N` folder appears every day). You do your work on **your own
branch**, push it, and your instructor reviews it and gives you feedback.

### One-time setup

1. **Get push access.** Ask your instructor to add your GitHub account to this
   repository. If your push is rejected with "permission denied", this is why.
2. **Clone the repository** and go into it:
   ```bash
   git clone git@github.com:Manifest-Son/YSOT-cs50-course.git
   cd YSOT-cs50-course
   ```
3. **Create your own branch**, named after you (your first name, lowercase). The
   example below is for a student called Lennox: use your own name instead.
   ```bash
   git switch -c lennox
   ```
4. **Set up the module** you are working in by following its README, for example
   [`python-daily-practice/README.md`](python-daily-practice/README.md).

### Every day

1. **Pull the latest assignment.** Switch to your branch and pull the new work
   from `main` into it:
   ```bash
   git switch lennox
   git pull --no-rebase --no-edit origin main
   ```
   The new `Day N` folder now appears in your copy, and your own earlier work
   stays. Use this exact command: the two flags tell Git to simply merge. A plain
   `git pull` can stop with `Need to specify how to reconcile divergent branches`
   once you have your own commits.
2. **Read the instructions.** Open the day's folder inside the module, for example
   `python-daily-practice/Day 3/`, and read its `README.md` from top to bottom.
   It explains the task and exactly how to do it.
3. **Do the task** in the files in that day's folder, following the README's
   **How to do it** and **Run and test** sections.
4. **Save your work and push it** to your branch:
   ```bash
   git status                         # check you only changed what you meant to
   git add .
   git commit -m "Day 3: finished"
   git push -u origin lennox          # the first time; afterwards just: git push
   ```
5. **Wait for feedback.** Your instructor will review the work on your branch on
   GitHub and give you feedback. Fix anything they point out, then commit and
   `git push` again.

### Rules

- **Work only on your own branch.** Never commit or push to `main`: it holds the
  assignments that everyone pulls.
- **Keep your branch name.** Do not rename it or reuse someone else's.
- **Change only your day's folder.** Do not edit other days, other modules, or
  the shared files at the top of the repository.
- **Never commit secrets.** Files such as `.env` are ignored on purpose. Do not
  force-add them with `git add -f`.
- **If the pull reports a merge conflict, stop and ask** your instructor before
  changing anything.

## Repository layout

```
YSOT-cs50-course/
├── README.md          <- you are here
├── .gitignore         <- shared ignore rules (secrets, venvs, caches, ...)
├── .gitattributes     <- line-ending normalisation (LF)
└── <module>/          <- one self-contained folder per course/concept
    ├── README.md      <- what it is and how to run it
    ├── SETUP.md       <- environment setup (if needed)
    └── ...
```

## Conventions

- **One module = one folder**, fully self-contained: its own README, dependencies
  (`requirements.txt`, `package.json`, ...), tests and setup instructions. A module
  must work without touching any other module.
- **No secrets in git.** Each module ships a `.env.example`; copy it to `.env`
  locally. `.env` is ignored repo-wide.
- **No nested git repositories.** Everything is tracked by this single repo.
  Do not run `git init` inside a module.
- **Virtual environments and build output are never committed** (`.venv/`,
  `node_modules/`, `__pycache__/`, ...).

## For instructors: adding a new module

1. Create a top-level folder with a short, lowercase, hyphenated name
   (e.g. `web-basics/`).
2. Add a `README.md` explaining the topic and how to run things, plus a
   `.env.example` if it needs configuration.
3. Add a row to the **Modules** table above.
4. Commit and push to `main` so students can pull it.
