""" Testdaten """
sonne_und_innere_planeten = ["Sonne",
		["Merkur", []],
		["Venus", ["Trion"]],
		["Erde", []],
		["Mars", ["Phobos", "Deimos"]]]

""" Funktion zur passend eingerückten Auflistung einer Liste mit Listen mit Listen """
def print_pretty(entity, cnt_tabs=0):
        if isinstance(entity, list):
                for elem in entity:
                        print_pretty(elem, cnt_tabs + 1)
        else:
                for i in range(cnt_tabs):
                        print("\t", end="")
                print(entity)

print_pretty(sonne_und_innere_planeten)
