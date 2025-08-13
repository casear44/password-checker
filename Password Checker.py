import re

def check_password(password):
    errors = []
    
    # Length check
    if len(password) < 8:
        errors.append("❌ Must be at least 8 characters")
    
    # Complexity checks
    if not re.search(r"[A-Z]", password):
        errors.append("❌ Missing uppercase letter")
    if not re.search(r"[a-z]", password):
        errors.append("❌ Missing lowercase letter")
    if not re.search(r"[0-9]", password):
        errors.append("❌ Missing number")
    if not re.search(r"[!@#$%^&*()_+]", password):
        errors.append("❌ Missing special character (!@#$...)")
    
    # Common password check
    common_passwords = ["password", "123456", "qwerty"]
    if password.lower() in common_passwords:
        errors.append("❌ Extremely common password")
    
    return errors if errors else ["✅ Strong password!"]

# Test it
password = input("Enter password: ")
results = check_password(password)
print("\n".join(results))