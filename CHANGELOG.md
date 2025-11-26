# Changelog

All notable changes to this project will be documented in this file.
This project adheres to [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) principles.

---

## [0.1.3] - 2025-11-26

### Added

- Implemented GPS L1C/A signal simulator in `krypto_lib/prng/gps_l1ca.py`:
  - Functions to generate C/A codes for GPS satellites.
- Added test cases for GPS L1C/A simulator in `tests/test_gps_l1ca.py`.
- Added RSA algorithm support for decryption in `krypto_lib/asymmetric/factorization/rsa.py`:
  - Updated `rsa` function to handle both encryption and decryption based on a flag.
- Implemented test cases for RSA decryption in `tests/test_rsa.py`.

## Changes

- PRGA moved to `krypto_lib/prng/prga.py` for better modularity.

## [0.1.2] - 2025-11-21

### Added

- Added RC4 (ARC4) symmetric cipher in `krypto_lib/symmetric/arc4.py`:
  - Key scheduling algorithm (KSA) and pseudo-random generation algorithm (PRGA).
  - Encryption/decryption function.
- Implemented test cases for RC4 in `tests/test_arc4.py`.

### Changed

- Updated Vigenère cipher implementation to use uppercase alphabet by default.

## [0.1.1] - 2025-11-21

### Added

- Added utility functions in `krypto_lib/utils.py` for:
  - Resizing byte sequences.
- Implemented additional test cases for utility functions.
- Implemented **Vigenère cipher** in `krypto_lib/vigenere.py`:
  - Key setup and encryption/decryption functions.

### Fixed

- Fixed minor bugs in the ChaCha20 implementation related to type handling.

## [0.1.0] - 2025-11-20

### Added

- Initial release of **Kypto**, a Python framework for modern cryptography.
- Implemented **ChaCha20** symmetric cipher in `krypto_lib/chacha20.py`:
  - Key setup, nonce handling, counter support.
  - Block generation and encryption function.
- Utility functions for converting between bytes, integers, hex, and strings.
- Basic tests for ChaCha20 encryption correctness.

### Notes

- This is the first release; only ChaCha20 is implemented.
- Future releases will include additional symmetric and asymmetric ciphers, utilities, and enhanced testing.

<!-- markdownlint-configure-file { "MD022": false, "MD024": false, "MD030": false, "MD032": false} -->
