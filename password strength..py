import re

def check_password_strength(password):
    # Regex Parts:
    # ^ (?=.*[a-z]) : Lowercase hona chahiye
    # (?=.*[A-Z])   : Uppercase hona chahiye
    # (?=.*\d)      : Ek digit hona chahiye
    # (?=.*[@$!%*?&]): Ek special character hona chahiye
    # [A-Za-z\d@$!%*?&]{8,} : Minimum 8 length honi chahiye
    
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    
    # Compile pattern
    pattern = re.compile(regex)
    
    # Match check karein
    if re.fullmatch(pattern, password):
        return "Strong Password"
    else:
        # Check karein ki kami kahan hai
        if len(password) < 8:
            return "Weak: Minimum 8 characters zaroori hain."
        elif not re.search(r"[A-Z]", password):
            return "Weak: Kam se kam ek Uppercase letter chahiye."
        elif not re.search(r"[a-z]", password):
            return "Weak: Kam se kam ek Lowercase letter chahiye."
        elif not re.search(r"\d", password):
            return "Weak: Kam se kam ek Number (0-9) chahiye."
        elif not re.search(r"[@$!%*?&]", password):
            return "Weak: Kam se kam ek Special Character (@, $, !, etc.) chahiye."
        return "Weak Password"

# Test cases
passwords = ["12345", "Abcde123", "Strong@Pass123", "password"]

for p in passwords:
    print(f"Password: {p} -> Result: {check_password_strength(p)}")