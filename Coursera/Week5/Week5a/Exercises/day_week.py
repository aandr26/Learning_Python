# Day to number problem

###################################################
# Student should enter code below

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_to_number(day):
    if day in day_list:
        # This was originally a print statement, 
        # but that caused the output to include 'None'
        return (day_list.index(day))
    else:
        return day + ": That is not a valid day"
###################################################
# Test data

print (day_to_number("Sunday"))
print (day_to_number("Monday"))
print (day_to_number("Tuesday"))
print (day_to_number("Wednesday"))
print (day_to_number("Thursday"))
print (day_to_number("Friday"))
print (day_to_number("Saturday"))
print (day_to_number("Saturda"))
###################################################
# Sample output

#0
#1
#2
#3
#4
#5
#6
