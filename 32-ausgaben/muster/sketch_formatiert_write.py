try:
        with open("loriot_badewanne.txt") as sketch, \
             open("loriot_badewanne2", "w") as sketch_mod:
                for line in sketch:
                        try:
                                print(line)
                                sketch_mod.write(line)
                        except ValueError:
                                pass
                sketch_mod.write("Loriot sagt Danke für alles")
except IOError as err:
        print("Ein Fehler ist aufgetreten: " + str(err))
