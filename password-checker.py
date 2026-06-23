password = input("Enter a password: ")

has_letter = False
has_digit = False

for ch in password:
    if ch.isalpha():
        has_letter = True
    if ch.isdigit():
        has_digit = True

if len(password) < 8:
    print("Weak password")
elif has_letter and has_digit:
    print("Strong password")
else:
    print("Medium password")
