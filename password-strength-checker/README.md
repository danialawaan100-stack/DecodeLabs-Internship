# Project 1: Password Strength Checker

**Internship Domain:** Cyber Security
**Batch:** 2026
**Organization:** DecodeLabs

## Objective
This project is a defensive cybersecurity utility designed to evaluate password strength using strict length verification and pattern recognition. It acts as a logic skeleton to filter out weak credentials before encryption phases.

## Features
- **Zero Point Policy:** Enforces an immediate failure for passwords under 8 characters to mitigate exponential brute-force risks.
- **Computational Efficiency:** Avoids verbose manual loops by utilizing Python's C-optimized `any()` function for short-circuit execution, ensuring O(n) time complexity.
- **Entropy Evaluation:** Validates the presence of uppercase characters, numerical digits, and symbols across the expanded Unicode entropy space.

## Files Included
- `main.py`: The primary Python script containing the password evaluation logic and terminal interface.
- `Project_Report.pdf`: Comprehensive documentation detailing the methodology, system logic, testing cases, and visual evidence of the working script.

## How to Run
1. Ensure Python 3 is installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory containing this project.
4. Execute the script using the following command:
   ```bash
   python main.py