import random

def missiles(number):
    print (str(number) + " missiles launched!")
    print (str(random.randrange(0,number)) + " missiles hit their target!")

if __name__ == '__main__':
    missiles(random.randrange(0,101))