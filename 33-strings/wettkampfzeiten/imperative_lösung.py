def normalise_time(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)

    return(mins + ':' + secs)

def print_times(filename):
    with open(filename) as timefile:
        line = timefile.readline()
    times = line.strip().split(',')
    clean_times = []
    for each_t in times:
        clean_times.append(normalise_time(each_t))
    print(clean_times)
    print(sorted(clean_times))
    
print_times("wettkampfzeiten.txt")
