# CHANGELOG

## [0.1.0] - 2026-08-31

### Added

- Implement translation-only motion adaptation and stationary duration self-report.
- Distinguish cessation, no apparent motion and censored/missing reports.
- Retain failed movie feasibility attempts; select shared procedural Gabor runtime subject to actual rendering/timing validation.

### Changed

- Use elapsed-deadline phase drift, retaining last submitted phase for static test.

### Fixed

- Exclude invalid presentation timing from valid duration-report summaries.
