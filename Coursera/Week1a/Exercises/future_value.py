

# Calculate the future value of a present value
def future_value(present_value,annual_rate,years):
    total_value = present_value * (1 + 0.01 * annual_rate) ** years
    print (total_value)
    return total_value

future_value(1000,5,25)

