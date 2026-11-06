# Mavuno School: the domain behind every exercise

Every practice day is set at **Mavuno School**, a (fictional) school that needs a system to manage its students, teachers, parents, exams and reports. The exercises here are for **learning**. The full Mavuno School system is built later, in a separate repository, using what you learn here.

## Who and what is in the school

| Role / thing | What it does |
| --- | --- |
| **Student** | Learns in a class, attends lessons, does assignments, sits CATs and exams, has marks recorded |
| **Teacher** | Teaches lessons, gives assignments, sets CATs and exams, records marks, takes attendance |
| **Parent / guardian** | Onboards (registers) the student, pays the fees, and follows the student's progress |
| **Lesson** | A teaching session: subject, teacher, class, time |
| **Assignment** | Work given after a lesson, marked and recorded |
| **CAT** | Continuous Assessment Test (CAT 1, CAT 2) during the term |
| **Midsem exam** | The exam in the middle of the term |
| **Endsem exam** | The exam at the end of the term |
| **Marks** | The recorded results for assignments, CATs and exams |
| **Report card** | A termly summary of a student's marks, grades and remarks |
| **Fees** | Tuition, transport and other charges that parents pay |
| **Attendance tracking** | Records whether each student was present in each class |
| **Remedials tracking** | Extra lessons for students who are struggling, and whether they improve |
| **Students clinic** | Assessment reports on **academic**, **sport** and **general life skills** that guide the learner |

## House rules used in the exercises

These are the same in every exercise, so the tests can check your answers. (They are a teaching simplification, not the real school policy.)

- **School name:** `Mavuno School`. **School email domain:** `mavuno.ac.ke`. **Currency:** `KES`.
- **Pass mark:** `50` (a score of 50 or more is a pass).
- **Grades by score:** `A` 80-100 · `B` 70-79 · `C` 60-69 · `D` 50-59 · `F` 0-49.
- **Valid marks:** a mark is valid if it is between `0` and `100` inclusive.
- **Fee discount:** `5%` where a discount is asked for.
- **Example subjects:** Mathematics, English, Kiswahili, Biology, Chemistry, Physics, History, Geography.
- **Example people:** Alice Wanjiku, Brian Otieno, Fatuma Hassan, Kevin Kiprop, Grace Achieng, Peter Mwangi.

## Levels: basic to intermediate

| Level | Folder | Status |
| --- | --- | --- |
| **1. Beginner** (35 days) | [`level-1-beginner/`](level-1-beginner/) | Ready. Ends with a Mini School Management System kept in memory |
| **2. Intermediate** | [`level-2-intermediate/`](level-2-intermediate/) | Planned. Adds saving data to files, handling errors and using modules, so the Level 1 system can store data permanently |

Each level builds the same story further: at Level 1 you handle one report card, then a class, then a small student database; at higher levels the data lives on disk and the code is organised so it can grow into the real system.

## How this connects to the full project

- **This repository** teaches the Python, one small challenge per day, always in Mavuno School terms.
- **A separate repository** holds the full Mavuno School project (students, teachers, parents and fees, lessons, assignments, CATs and exams, report cards, attendance, remedials and the clinic).
- Nothing here is the full system: the Level 1 capstone is a deliberately small, in-memory version.
