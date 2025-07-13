# Check password strength without using re
def check_password_strength(password):
    strength_points = 0
    suggestions = []

    # Flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()_+-=[]{}|;:'\",.<>?/\\"

    if len(password) >= 8:
        strength_points += 1
    else:
        suggestions.append("❗ Password should be at least 8 characters.")

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    if has_upper:
        strength_points += 1
    else:
        suggestions.append("❗ Add at least one uppercase letter.")

    if has_lower:
        strength_points += 1
    else:
        suggestions.append("❗ Add at least one lowercase letter.")

    if has_digit:
        strength_points += 1
    else:
        suggestions.append("❗ Add at least one digit (0–9).")

    if has_special:
        strength_points += 1
    else:
        suggestions.append("❗ Add at least one special character (!@#$...).")

    # Final rating
    if strength_points == 5:
        status = "🟢 Strong"
    elif strength_points >= 3:
        status = "🟡 Medium"
    else:
        status = "🔴 Weak"

    return status, suggestions

# Menu
def main():
    while True:
        print("\n=== Password Strength Checker ===")
        print("1. Check Password Strength")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            password = input("Enter your password: ")
            strength, tips = check_password_strength(password)

            print(f"\n🔐 Password Strength: {strength}")
            if tips:
                print("🔧 Suggestions:")
                for tip in tips:
                    print(f"   - {tip}")
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

