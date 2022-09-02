def normalise_time(time_string):
    if '-' in time_string:
        splitter = '-'
    elif '.' in time_string:
        splitter = '.'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)

    return(mins + ':' + secs)

class Jock:
    def __init__(self, name, club, times=[]):
        self.__name = name
        self.__club = club
        self.__times = times

    def desc(self) -> str:
        return f'Name: {self.__name} (Verein: {self.__club})'

    def best(self) -> str:
        return(sorted(set([normalise_time(t) for t in self.__times]))[0])

def eval_jock(line):
    split_line = line.strip().split(',')
    name = split_line.pop(0)
    club = split_line.pop(0)
    times = split_line
    return(Jock(name, club, times))

def read_time_file(filename):
    jocks = list()
    try:
        with open(filename) as f:
            for line in f:
                jocks.append(eval_jock(line))
        return(jocks)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)
    
jocks = read_time_file('../wettkampfzeiten_erweitert.txt')

for jock in jocks:
    print(f'{jock.desc()} schnellste Zeit: {jock.best()}s')
