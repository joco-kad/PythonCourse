try:
        with open("loriot_badewanne.txt") as sketch:
                for line in sketch:
                        try:
                                (role, text) = line.split(':', 1)
                                print(role, end='')
                                print(' sagt: ', end='')
                                print(text)
                        except ValueError:
                                pass
except IOError as err:
        print("Ein Fehler ist aufgetreten: " + str(err))
