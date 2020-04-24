def is_lunchtime(hour,is_am):
    """ Takes the perameter 'hour' and checks if it is am or pm 
    to determine if it is lunch time"""
    return (hour == 11 and is_am) or (hour == 12 and not is_am)

