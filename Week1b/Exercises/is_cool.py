def is_cool(name):
    """ Determines whether the parameter 'name' is cool or not """
    if (name == "Joe"):
        return True
    elif (name == "John"):
        return True
    elif (name == "Stephen"):
        return True
    else:
        return False

name = "Joe"

cool_name = is_cool(name)

if cool_name:
    print ("That is a very cool name!")
else:
    print ("This name stinks")

