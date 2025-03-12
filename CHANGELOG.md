# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
and adheres to [Semantic Versioning](https://semver.org/).

---

## [Unreleased] - 2025-03-07
### Added
- CHANGELOG.md
- Modified by argument in quoteset aggregate functions to accept a function to
	both get and group by dict key.
- Implemented PriceTest class, allowing for price testing implementations
- ModuleFile now checks MD5 hash of source file (if provided) and raises an 
	___ error if not equal.

## [0.1.0] - 2025-02-24
### Added
- Initial alpha release of the pricing framework.
- Implemented standardized data structures.
- Added logging and audit trail features.