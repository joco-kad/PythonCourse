def print_line(role, text):
	print(role, "sagt:", text)

def handle_line(line):
	try:
		(role, text) = line.split(':', 1)
		print_line(role, text)
	except ValueError:
		pass



sketch = open("../loriot_badewanne.txt")

for line in sketch:
	handle_line(line)

sketch.close()
