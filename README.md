# Password-Checker-Generator

## Description
This project is a command-line Password Checker & Generator developed in Python. It allows users to evaluate the strength of existing passwords based on multiple security rules and generate random strong passwords using a simple menu-driven interface.

The application demonstrates fundamental cybersecurity concepts such as password validation, strength evaluation, secure random password generation, and defensive input validation.

## Features
* **Interactive Menu System:** A straightforward, text-based terminal menu.
* **Password Strength Analysis:** Comprehensive algorithmic password evaluation.
* **Password Generation:** Instantly creates complex, randomly generated passwords.
* **Length & Character Validation:** Checks for required string length and valid input constraints.
* **Pattern Detection:** Identifies weak, predictable keyboard sequences (e.g., `qwe`, `asd`, `zxc`).
* **Scoring & Classification:** Rates password complexity into three clear tiers:
  * 🔴 Weak
  * 🟡 Medium
  * 🟢 Strong
* **Error Resilience:** Robust exception handling for invalid user inputs.

## Technologies Used
* **Language:** Python 3
* **Standard Modules:** `random`, `string`
* **Concepts:** Exception Handling, Conditional Statements, Loops, Custom Functions

## Project Structure
```text
Password-Checker-Generator/
├── password_checker.py     # Main application script
├── README.md               # Project documentation
└── screenshots/            # Application execution images
```

## Installation
1. Install Python 3 on your local machine.
2. Clone or download this repository.
3. Open your terminal or command prompt inside the project folder.

## Usage
Run the program using the following command:
```bash
python password_checker.py
```

### Main Menu Interface:
1. **Check Password**
2. **Generate Password**
3. **Quit**

### How the Password Checker Works
The system evaluates your input password using several strict criteria:
* Password length constraints
* Presence of uppercase letters
* Presence of lowercase letters
* Inclusion of numbers
* Inclusion of special characters
* Detection of weak common keyboard sequences
* Allowed character validation

A score is dynamically calculated, and the password is then classified as **Weak**, **Medium**, or **Strong**.

### How the Password Generator Works
Generates a random, secure **12-character** password containing a guaranteed balanced mixture of:
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters

## Learning Outcomes
Through this project I practiced:
• Python programming
• Function design
• Exception handling
• Password security principles
• String manipulation
• Randomized password generation
• Input validation
• Menu-driven application development

## Future Improvements
* [ ] Password history tracking to prevent recycling
* [ ] Secure password hashing implementations (SHA-256)
* [ ] Persistent password storage using a local database
* [ ] Password entropy calculation metrics
* [ ] Dictionary attack detection using weak-word datasets
* [ ] Exporting structural password strength reports
* [ ] Developing a Graphical User Interface (GUI)

## License
This project is intended for educational and portfolio purposes.

## Author
**Rishabh Bhaskar**
* Bachelor of Computer Science
* University of Wollongong in Dubai
