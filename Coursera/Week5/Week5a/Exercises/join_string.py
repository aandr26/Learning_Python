# String list joining problem

###################################################
# Student should enter code below

def string_list_join(string_list):
    for strings in string_list:
        cac = ''.join(string_list)
        return cac
###################################################
# Test data

print (string_list_join([]))
print (string_list_join(["pig", "dog"]))
print (string_list_join(["spam", " and ", "eggs"]))
print (string_list_join(["a", "b", "c", "d"]))


###################################################
# Output

#
#pigdog
#spam and eggs
#abcd