# password-checker
basic password checker yo........
```markdown
# 🔒 Password Checker

A lightweight tool to validate password strength and check against known breaches.

## Features
✅ Password strength scoring (Weak/Medium/Strong)  
✅ Common pattern detection (e.g., "123456", "password")  
✅ Optional breach checking via HaveIBeenPwned API  
✅ Customizable rules (length, special chars, etc.)  
✅ CLI and Python module support  

## Installation
```bash
git clone https://github.com/your-username/password-checker.git
cd password-checker
pip install -r requirements.txt
```

## Usage
### Command Line
```bash
python check.py "Your_P@ssw0rd"
```

### Python Module
```python
from password_checker import PasswordChecker

checker = PasswordChecker()
result = checker.check("password123")
print(f"Strength: {result.strength}, Breached: {result.breached}")
```

## Configuration
Edit `config.json` to:
- Set minimum password length
- Enable/disable breach checking
- Adjust strength requirements

## Requirements
- Python 3.6+
- `requests` package (for API checks).
