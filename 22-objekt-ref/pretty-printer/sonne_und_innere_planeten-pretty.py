sonne_und_innere_planeten = ["Sonne",
		["Merkur", []],
		["Venus", ["Trion"]],
		["Erde", []],
		["Mars", ["Phobos", "Deimos"]]]

for elem in sonne_und_innere_planeten:
        if isinstance(elem, list): 
                for inner_elem in elem:
                        if isinstance(inner_elem, list):
                                for inner_inner_elem in inner_elem:                                     
                                        print("\t\t" + inner_inner_elem) 
                        else:
                                print("\t" + inner_elem)
        else:
                print(elem)










