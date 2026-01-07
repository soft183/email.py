def validate_email(email):
    if "@" not in email:
        return "Invalid Email"

    parts = email.split("@")
    if len(parts) != 2:
        return "Invalid Email"
    username = parts[0]
    domain = parts[1]

    if username == "" or domain == "":
        return "Invalid Email"

    if "." not in domain:
        return "Invalid Email"

    if domain.startswith(".") or domain.endswith("."):
        return "Invalid Email"

    return "Valid Email"

email_input = input("Enter an email address: ")
result = validate_email(email_input)
print(result)
