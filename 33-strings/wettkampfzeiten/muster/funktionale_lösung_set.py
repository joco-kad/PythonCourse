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
    clean_times = set([normalise_time(t) for t in times])
    print(sorted(clean_times))
    
print_times("../wettkampfzeiten.txt")
