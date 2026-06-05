class DOBException(Exception):
    pass


try:
    age = 35

    if not (20 <= age <= 30):
        raise DOBException(
            "Age must be between 20 and 30"
        )

except DOBException as e:
    print(e)