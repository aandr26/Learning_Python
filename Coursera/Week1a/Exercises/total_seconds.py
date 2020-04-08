# Total number of seconds from three parameters
def total_seconds(hours,minutes,seconds):
    total = ((hours * 60)*60 + (minutes * 60)) + seconds
    return total

print (total_seconds(5,0,0))

# Test
def test(hours,minutes,seconds):
    print (str(hours) + " hours, " + str(minutes) + " minutes, and",) 
    print (str(seconds) + " seconds totals to",)
    print (str(total_seconds(hours,minutes,seconds)) + " seconds.")

test(7,21,37)
test(10,1,7)
test(1,0,1)