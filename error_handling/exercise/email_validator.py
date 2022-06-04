from custom_exceptions import MustContainAtSymbolError, NameTooShortError, InvalidDomainError


def check_at_symbol_validity(email):
    email = email.split("@")

    if len(email) != 2:
        raise MustContainAtSymbolError("Email must contain @")

    return True


def check_name_length_validity(email, at):
    name = email

    if at:
        email = email.split("@")
        name = email[0]
    elif "." in email:
        email = email.split(".")
        name = email[0]

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    return True


def check_domain_validity(email):
    valid_domains = [".com", ".bg", ".net", ".org"]
    current_domain = "." + email.split(".")[-1]

    if current_domain not in valid_domains:
        valid_domains = ", ".join(valid_domains)
        raise InvalidDomainError(f"Domain must be one of the following: {valid_domains}")

    return True


while True:
    current_email = input()
    if current_email == "End":
        break

    at_is_valid = check_at_symbol_validity(current_email)
    length_is_valid = check_name_length_validity(current_email, at_is_valid)
    domain_is_valid = check_domain_validity(current_email)

    if at_is_valid and length_is_valid and domain_is_valid:
        print("Email is valid")
