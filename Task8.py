def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60

    return "%d:%02d:%02d" % 

print(convert(133)) 
