import math
def smaller_root(a, b, c):
    """ Computes the solution to the quadratic formula"""
    discriminant = (b ** 2) - (4*a*c)
    if discriminant < 0 or discriminant == 0:
        print ("Error: No real solutions.")
    else:
        discriminant_sqrt = math.sqrt(discriminant)
        if a > 0:
            smaller = - discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-b + smaller) / (2 * a)
   


    
