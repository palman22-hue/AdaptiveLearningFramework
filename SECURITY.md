# Security Policy

## Supported versions

AdaptiveLearningFramework is currently an experimental/prototype project and only the `main` branch is actively maintained.  
Other branches or forks are not covered by security support.

## Deployment model

AdaptiveLearningFramework is designed for local use (e.g. VS Code / Codespaces / local Python environment).  
This repository does **not** provide a public, maintainer-operated API or hosted service; any external exposure (for example, via a custom-built web service) is the responsibility of the deploying party.

## Data & privacy

- Input data (questions, answers, learner profiles, JSON configuration) is processed locally in your environment.  
- Any logs, progress records, or result files are stored locally on the user’s system.  
- The maintainer does not receive automatic telemetry or user data.

Users are responsible for:
- Protecting any sensitive learner or assessment data they process with AdaptiveLearningFramework.  
- Securing their own host system, operating system, and runtime (Python environment, editor, containers, etc.).

## Reporting a vulnerability

If you discover a potential vulnerability or a serious misuse risk in AdaptiveLearningFramework, please use **responsible disclosure**.

If Private Vulnerability Reporting is enabled for this repository:
1. Use the **“Report a vulnerability”** button on the repository’s GitHub page to submit a private report.

If Private Vulnerability Reporting is not available:
1. Open a minimal public issue that:
   - Only states that you have found a potential vulnerability.
   - Does **not** include technical details or exploit code.
2. Wait for the maintainer to respond with an appropriate private channel for sharing details.

Where possible, include:
- A description of the vulnerability or misuse scenario.  
- Reproduction steps or a proof-of-concept (shared only through a private channel).  
- Relevant environment details (OS, Python version, editor/IDE, container configuration).

The goal is to provide an initial response within 14 days, including an indication of next steps.

## Scope

In scope:
- The code in this repository (`main` branch), including:
  - Core adaptive learning logic (state machines, scoring, progression rules).  
  - JSON configuration / curriculum definitions shipped with the project.  
  - CLI tools, notebooks, and scripts referenced in the README.

Out of scope:
- External tools and runtimes (editors, containers, Python installations, LLMs or other services you optionally connect to).  
- Third-party services, wrappers, or deployments that expose AdaptiveLearningFramework to the internet.  
- Hardware- and OS-specific issues that do not directly originate from the code in this repository.

## Responsible use

AdaptiveLearningFramework is intended as a transparent, supportive framework for learning and assessment.  
Users are strongly discouraged from using the system for:

- Harmful or punitive profiling of learners.  
- Unethical data collection, surveillance, or manipulation of learners’ behavior.

If you observe misuse of AdaptiveLearningFramework in the wild, you may report it using the same contact path as above.
