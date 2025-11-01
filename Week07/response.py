from validator_collection import validators, errors


try:
    email = validators.email(input("What's your email address: "))
    if email:
        print("Valid")
except errors.InvalidEmailError:
    print("Invalid")
