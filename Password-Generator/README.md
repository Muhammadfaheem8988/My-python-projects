**Secure Password Generator (Cryptographically Secure)**

A robust Python utility designed to generate high-entropy, random passwords. Unlike standard generators, this tool uses the secrets module to ensure passwords are cryptographically strong and resistant to prediction.

**Enhanced Security**

This version of the script has been upgraded to use Python's secrets module, which is specifically designed for managing secrets such as passwords, account authentication, security tokens, and related secrets.

Why it matters: Standard random modules are pseudo-random and can be predicted if the "seed" is known. The secrets module provides access to the most secure source of randomness provided by your operating system.
----

**Features**

Cryptographically Secure: Uses secrets.choice for non-deterministic randomization.

Customizable Length: Define exactly how long your password should be.

Flexible Complexity: Toggle numbers and special characters on or off based on site requirements.

Input Validation: Ensures a minimum length (6 characters) for basic security hygiene.
----

**Installation & Requirements**

Python 3.6+: Required for the secrets module.

No external libraries needed.

How to Use

Download password_gen.py.

Run the script in your terminal:

Bash

python password_generator.py

Answer the prompts to generate your secure string:

Length: (e.g., 20)

Include numbers? (y/n)

Include special characters? (y/n)

**License**
This project is open-source and available under the MIT License.
----