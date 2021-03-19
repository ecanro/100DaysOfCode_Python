age: int
name: str
height: float
is_human: bool

# Type Hint in python


def police_check(age: int) -> bool:
    # we said that function police_check have a parameter age with type int
    # and the func will return a boolean
    if age > 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


if police_check(12):
    print("You may pass")
else:
    print("Pay a fine.")
