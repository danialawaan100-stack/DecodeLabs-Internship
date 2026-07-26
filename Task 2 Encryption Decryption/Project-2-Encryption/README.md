# Project 2: Basic Encryption & Decryption

## Objective
The goal of this project is to implement a simple encryption and decryption technique to understand Data Confidentiality. It demonstrates how data in transit can be protected through mathematical transformation.

## Methodology
The project utilizes the Caesar Cipher, a substitution cipher that shifts characters by a specified number.
- **Encryption Algorithm:** `En(x) = (x + n) % 26`
- **Decryption Algorithm:** `Dn(x) = (x - n) % 26`

ASCII conversion functions `ord()` and `chr()` are used to transform text into integers, apply the shift logic, and convert the integers back into characters.

## Features
- Preserves uppercase and lowercase letters.
- Maintains punctuation, numbers, and whitespace without alteration.
- Handles character wrap-around using modulo arithmetic.

## Tools Used
- Python 3
- Visual Studio Code
- Git/GitHub