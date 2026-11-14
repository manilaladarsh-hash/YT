# Second Brain log

## 2026-11-14 - Atlas provider interruption recovery

- Objective: recover the interrupted STEM PhD Atlas 2027 work after an agent execution error.
- Diagnosis: the supplied failure occurred during Antigravity context summarization, when a request to its local model service at 127.0.0.1:8749 timed out. Windows inspection found no listening TCP socket on that port, although Antigravity processes were running. This is a provider runtime failure, not evidence of an Atlas application defect. The service itself has not been repaired or restarted.
- Recovery: the current Codex session executes project commands successfully without that endpoint. No provider configuration, TLS settings, proxies, or running applications were changed.
- Repository: branch claude/magical-dirac-6pfq3g; HEAD 4b86b7d9 (UTRGV addition), matching the tracked origin branch at inspection. Interrupted changes include a UWF entry in data/universities.json and untracked fetched-page caches; preserve these for review. No data was promoted during this recovery.
- Verified commands from business/phd-atlas: `python handoff/next.py` exited 0 and selected CARD 4, The University of West Florida; `python scripts/validate_data.py --dir data/ --require-cache` exited 0 with 376 universities, 3838 programs, 0 errors, 0 warnings; `python scripts/coverage.py` exited 0 with 8880/42218 Not stated values (21% rounded), across 18 fields.
- Status: command execution recovered; Antigravity service outage unresolved. Overall coverage still fails the under-15% release threshold. Full tests, staging validation, browser acceptance, PDF rendering and release checks were not rerun in this focused recovery.
- Next action: resume UWF using handoff/GEMINI_TASKS.md CARD 4; inspect existing fetched sources, stage and review new records before promotion. Keep the current working files intact. If Antigravity must be used again, restore its local provider service through the host application's supported controls, then retry; repeatedly changing model names does not repair an unavailable endpoint.
- Durable lesson: distinguish agent-provider transport/checkpoint failures from repository failures; verify the project's own resume command and validators before modifying application code.

## 2026-11-14 - UWF (CARD 4) completed

- Completed university: The University of West Florida (`uwf`, Florida, R2).
- Programs added (1): `uwf--datasci` (`Intelligent Systems & Robotics, Ph.D.`, CIP 11.0102, `also_fields: ["cs", "ece", "mech"]`). Excluded UWF's two online Ed.D. programs (Curriculum & Instruction, Instructional & Performance Technology).
- Source conflicts:
  1. `english_waiver` (`uwf`): `catalog.uwf.edu/graduate/admissions/internationaladmissions/` and `UWF/REG-3.042` (amended 2026-06-18) allow a prior degree from a university where English is the official language of instruction, whereas `uwf.edu/graduate/international/` requires a test unless native language is English, primary country language is English, or U.S. bachelor's degree; left `Not stated`.
  2. `gre_general` (`uwf--datasci`): `catalog.uwf.edu/graduate/phd/` states GRE submission is optional, whereas `uwf.edu/graduate/apply/test-requirements-for-admission/` lists `GRE` and `uwf.edu/programs/hmcse/intelligent-systems-robotics-phd/` omits "is optional"; left `Not stated`.
- Remaining unknowns: `uwf.gre_general` (per-program), `uwf.english_waiver` (conflicting sources), `uwf--datasci.gre_general` (conflicting sources), `uwf--datasci.supervisor` (personal statement asks for UWF/IHMC faculty names and committee interviews/matches participants, but prior contact/agreement requirement not stated).
- Validation results: staging `validate_data.py --dir data/staging --require-cache` (`1 universities, 1 programs, 0 errors, 0 warnings`, exit 0), staging `audit_quality.py --dir data/staging` (`0` flags, exit 0), promoted via `promote.py uwf` (exit 0), live `validate_data.py --dir data --require-cache` (`377 universities, 3839 programs, 0 errors, 0 warnings`, exit 0), `coverage.py` (`377 of 385 listed`, `3839 programs`, `8883/42229 = 21%` Not stated, exit 0).
- Next task: `CARD 4` — `University of Arkansas at Little Rock` (R2).

## 2026-11-14 - UA Little Rock (CARD 4) completed

- Completed university: University of Arkansas at Little Rock (`ualr`, Arkansas, R2).
- Programs added (8 records covering 12 STEM fields): `ualr--biology` (`Applied Science, Applied Biosciences Emphasis, Ph.D.`), `ualr--chemistry` (`Applied Science, Applied Chemistry Emphasis, Ph.D.`), `ualr--math` (`Applied Science, Applied Mathematics and Statistics, Ph.D.`, `also_fields: ["statistics"]`), `ualr--physics` (`Applied Science, Applied Physics Emphasis, Ph.D.`, `also_fields: ["materials", "earth", "astronomy"]`), `ualr--biomed` (`Bioinformatics, Ph.D.`, joint with UAMS, `also_fields: ["biology"]`), `ualr--cs` (`Computer and Information Sciences, Ph.D.`), `ualr--ece` (`Engineering, Electrical and Computer Engineering Track, Ph.D.`), and `ualr--mech` (`Engineering, Mechanical Engineering Track, Ph.D.`). Excluded Criminal Justice Ph.D. and Reading Ph.D. (non-STEM).
- Source discrepancies documented in `handoff/OWNER_REVIEW.md`:
  1. International Fall deadline: Policy LR 509.9 (revised 2026-04-10) and `gradschool/international-prospects/` state June 1 (used `2027-06-01` for Applied Science & CIS), whereas the 2026-2027 catalog (`navoid=2484`) also prints legacy July 1 and Feb 1 dates.
  2. Applied Science GRE minimums: `steps-to-apply/` states 300 combined + 4.5 AW vs catalog 155Q/138V/4.5AW (both allow waiver at >=3.5 last-60 GPA).
  3. Engineering Ph.D. master's GPA: `engineering-phd/` states 3.3 vs catalog 3.5; `poid=5576` (Mechanical) copies ECE thesis GRE waiver text.
  4. TOEFL scale: `international/english-requirements/` lists "Minimum score of 4 on TOEFL iBT" only in the Undergraduate column; Graduate Doctoral remains `79` (CIS expects > 79).
- Remaining unknowns: `ualr.gre_general` (set per program; all 8 programs require GRE General with waivers), `ualr--math.gre_subject` and `ualr--physics.gre_subject` (`Not stated` because ETS offers Mathematics/Physics Subject Tests and UALR states only GRE General).
- Validation & promotion results: staging `validate_data.py --dir data/staging --require-cache` (`1 universities, 8 programs, 0 errors, 0 warnings`, exit 0), staging `audit_quality.py --dir data/staging` (`0` flags, exit 0), promoted via `promote.py ualr` (exit 0), live `validate_data.py --dir data --require-cache` (`378 universities, 3847 programs, 0 errors, 0 warnings`, exit 0), `coverage.py` (`378 of 386 listed`, `3847 programs`, `8885/42317 = 21%` Not stated, exit 0).
