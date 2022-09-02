sketch = open("../loriot_badewanne.txt")

for line in sketch:
	(role, text) = line.split(':', 1)
	print(role, end='')
	print(' sagt: ', end='')
	print(text)

sketch.close()
