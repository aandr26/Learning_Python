def banner(message, border = '-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

# Don't need to provide the border arguement because it is already defined.
banner("Norwegian Blue")

"""
In this case the message string is a called a 'positional' arguement 
and the border string is a 'keyword' arguement.
"""

banner("Hello, there", border="*")

"""
If we use keywords for both arguements, they can come in any order.
If using a mixture, the positional arguement must come first.
"""
banner(border = "+", message="General, Kenobi!")


import time

time.ctime()

def show_default(arg=time.ctime()):
    print(arg)

show_default()

# Does not progress becuase it is set as the default arguement?
show_default()

def add_spam(menu=[]):
    menu.append("spam")
    print(menu)
    return menu

breakfast = ['bacon', 'eggs']
add_spam(breakfast)
lunch = ['baked beans']
add_spam(lunch)
add_spam()
add_spam()
""" Always us imumtable objects as default values """

def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append('spam')
    print(menu)
    return menu

add_spam()
add_spam()
add_spam()
add_spam()