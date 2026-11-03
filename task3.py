name = input("Name: ").strip().title()
email = input("Email: ").strip().lower()
phone = input("Phone: ").replace(" ", "")

# Validate name
name_valid = len(name) > 0

# Validate email
email_valid = (
    "@" in email and
    "." in email and
    not email.startswith("@")
)

# Validate phone
phone_valid = (
    phone.isdigit() and
    phone.startswith("05") and
    len(phone) == 10
)

# Display errors
if not name_valid:
    print("Error: Invalid name")

if not email_valid:
    print("Error: Invalid email")

if not phone_valid:
    print("Error: Invalid phone number")

# Display clean record
if name_valid and email_valid and phone_valid:
    print("\nClean Record:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")

    # Generate username using find and slicing
    space_index = name.find(" ")

    if space_index == -1:
        first_name = name
    else:
        first_name = name[:space_index]

    username = first_name.lower() + "." + phone[-2:]

    print("Suggested username:", username)