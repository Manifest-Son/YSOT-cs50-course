# YSOT CS50-Style Course

The main repository for YSOT's CS50-style learning programme. Each topic we learn
and teach lives in its own self-contained module (a folder at the top level), so
modules can grow, be set up, and be tested independently.

## Modules

| Module | Topic | Stack | Status |
| --- | --- | --- | --- |
| [`ai-for-beginners/`](ai-for-beginners/) | Introduction to Artificial Intelligence: a 6-session, hands-on course with a "Game Night" tic-tac-toe capstone | Python 3.10+ | In progress |

> More modules will be added here as new concepts are introduced.

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

## Adding a new module

1. Create a top-level folder with a short, lowercase, hyphenated name
   (e.g. `web-basics/`).
2. Add a `README.md` explaining the topic and how to run things, plus a
   `.env.example` if it needs configuration.
3. Add a row to the **Modules** table above.
4. Commit on a branch and open a pull request into `main`.

## Getting started

```bash
git clone git@github.com:Manifest-Son/YSOT-cs50-course.git
cd YSOT-cs50-course/<module>
# then follow that module's README / SETUP.md
```
