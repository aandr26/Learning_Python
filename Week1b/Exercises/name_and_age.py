def name_and_age(name, age):
    """ This function outputs the values 'name' and 'age' into one concatonated string"""
    if age < 0:
        return "Error: Invalid age."
    else:
        return str(name) + " is " + str(age) + " years old."
