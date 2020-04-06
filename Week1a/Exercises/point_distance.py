import math

# Calculate the distance between two points
# taking four parameters and using the math.sqrt module
def point_distance(x0,y0,x1,y1):
    total_distance = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
    print (total_distance)
    return total_distance

point_distance(2,2,5,6)
point_distance(1,1,2,2)
point_distance(0,0,3,4)