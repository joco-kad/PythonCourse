def normalise_time(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)

    return("%d:%02d" % (mins,secs))
