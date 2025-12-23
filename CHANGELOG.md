# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),  
and this project adheres to **Semantic Versioning**.

---

## [Unreleased]
- Additional STEM topics
- Gamified Learning Framework (GLF)
- Progress tracking and analytics
- Multi-language JSON content
- UI redesign with XP, badges, and levels

---

## [1.0.0] – 2025-12-23
### Added
- **Complete Adaptive Learning Engine (`engine.py`)**
  - Modular architecture
  - AdaptiveLearner state machine (diagnosis → drill → integration)
  - Automatic phase transitions
  - JSON-driven problem loading
- **Bilingual Streamlit UI (`alf_app.py`)**
  - English and Dutch interface
  - Automatic learner initialization per topic
  - Clean separation between UI and engine
- **JSON Problem Bank**
  - `kinetic_energy.json`
  - `chemistry_moles.json`
  - Additional topics added and validated
- **Project Structure Overhaul**
  - Clear separation of engine, UI, and content
  - `FotoDocs/` folder documenting project evolution
- **Documentation**
  - New English README.md
  - Visual evolution section
  - Clear project overview and roadmap

### Changed
- Refactored old prototype code into modular engine
- Replaced legacy ALFFramework class with clean engine + learner model
- Improved error handling for JSON loading
- Standardized JSON schema across all topics

### Fixed
- Duplicate Streamlit keys
- Topic initialization issues
- JSON loading errors for empty or malformed files
- Language switching bugs in UI

---

## [0.1.0] – 2025-12-15
### Added
- First working prototype of ALF
- Basic Streamlit interface
- Early JSON problem structure
- Initial diagnosis → drill → integration loop

---

