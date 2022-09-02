sonne_und_innere_planeten = ["Sonne",
		["Merkur", []],
		["Venus", []],
		["Erde", ["Mond"]],
		["Mars", ["Phobos", "Deimos"]]]

for element in sonne_und_innere_planeten:
	print(element)

venus = sonne_und_innere_planeten[2]
monde_der_venus = venus[1]
monde_der_venus.append("Trion")

for element in sonne_und_innere_planeten:
	print(element)

erde = sonne_und_innere_planeten[3]
erde[1].clear()

for element in sonne_und_innere_planeten:
	print(element)