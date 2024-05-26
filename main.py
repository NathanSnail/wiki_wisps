from wisper.core import compute

text = open("src", "r").read()

t = ""
lifetime = False
i = 0
l = text.split("\n")
while i < len(l):
	line = l[i]
	i = i + 1
	if "style" in line or "File" in line:
		t = t + line
		lifetime = True
		continue
	if line == "|-":
		print(t)
		t = ""
		continue
	if lifetime:
		lifetime = False
		line = line[1:]
		print(line)

		parts = line.split("||")
		while len(parts) < 3:
			next = l[i]
			i = i + 1
			line = line + "|" + next
			parts = line.split("||")
		print(parts)
		if len([x for x in parts[0] if x != " "]) == 0:
			high, low = int(parts[2]), int(parts[2])
		else:
			low, high = int(parts[0]), int(parts[1])
		print(low, high)
		print("S:", compute(low, high, 100)[-1])
