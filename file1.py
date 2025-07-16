def maskEmail(email: str) -> str:
    username = email.split("@")[0]
    domain = email.split("@")[1]

    first = username[0]
    last = username[-1]
    middle = "*" * (len(username) - 2)

    masked_username = first + middle + last
    return masked_username + "@" + domain

print(maskEmail("peter.rapcsak@gmail.com"))
