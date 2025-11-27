# Kypto

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=LuisChineaRangel_krypto&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=LuisChineaRangel_krypto)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=LuisChineaRangel_krypto&metric=coverage)](https://sonarcloud.io/summary/new_code?id=LuisChineaRangel_krypto)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=LuisChineaRangel_krypto&metric=bugs)](https://sonarcloud.io/summary/new_code?id=LuisChineaRangel_krypto)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=LuisChineaRangel_krypto&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=LuisChineaRangel_krypto)

---

**Kypto** is a modular Python framework for modern cryptography.
It aims to provide tools for encryption, hashing, key management, and secure data handling in a structured and extensible way.

---

## Table of Contents

- [Current Status](#current-status)
- [Project Structure](#project-structure)

---

## Current Status

- Project just started (v0.1.2)
- Initial project structure in place
- Core modules and basic setup planned
- RSA, Vigenère, ARC4, and ChaCha20 ciphers implemented
- GPS L1C/A signal simulator implemented
- Basic unit tests for implemented ciphers

---

## Project Structure

The project is organized into the following main directories:

- `krypto_lib/`: Core library code for cryptographic operations.
- `krypto_lib/asymmetric/`: Asymmetric cryptography algorithms (e.g., RSA, ECC).
- `krypto_lib/symmetric/`: Symmetric cryptography algorithms (e.g., AES, ChaCha20).
- `krypto_lib/prng/`: Pseudorandom number generators (e.g., ARC4).
- `tests/`: Unit and integration tests for the library.
- `cli/`: Command-line interface tools for interacting with the library.
- `api/`: RESTful API endpoints for remote cryptographic services.
- `requirements.txt`: List of dependencies required for the project.
- `pyproject.toml`: Project metadata and configuration.

Each module is designed to be independent, allowing for easy maintenance and future expansion.

---
