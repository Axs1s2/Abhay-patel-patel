import re

def validate_email(email):
    # Regex Breakdown:
    # ^[a-zA-Z0-9._%+-]+ : Shuruat mein letters, numbers ya symbols jaise . _ % + -
    # @[a-zA-Z0-9.-]+     : @ ke baad domain ka naam
    # \.[a-zA-Z]{2,}$    : Dot (.) ke baad kam se kam 2 alphabets (com, in, org, etc.)
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    if re.match(email_regex, email):
        return True
    return False

def validate_phone(phone):
    # Regex Breakdown:
    # ^[6-9]    : Indian numbers aam taur par 6, 7, 8, ya 9 se shuru hote hain
    # \d{9}$    : Uske baad barabar 9 digits hone chahiye (Total 10)
    phone_regex = r"^[6-9]\d{9}$"
    
    if re.match(phone_regex, phone):
        return True
    return False

# --- Testing the Program ---
test_email = "example.user@gmail.com"
test_phone = "9876543210"

print("--- Email Validation ---")
if validate_email(test_email):
    print(f"'{test_email}' is a Valid Email.")
else:
    print(f"'{test_email}' is an Invalid Email.")

print("\n--- Phone Number Validation ---")
if validate_phone(test_phone):
    print(f"'{test_phone}' is a Valid Phone Number.")
else:
    print(f"'{test_phone}' is an Invalid Phone Number.")