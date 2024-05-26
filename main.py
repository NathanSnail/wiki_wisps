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
		t += "\n" + line
		lifetime = True
		continue
	if line == "|-":
		print(t[1:] + "\n|-")
		t = ""
		continue
	if lifetime:
		lifetime = False
		line = line[1:]

		parts = line.split("||")
		while len(parts) < 3:
			next = l[i]
			i += 1
			line = line + "|" + next
			parts = line.split("||")
		if len([x for x in parts[0] if x != " "]) == 0:
			high, low = int(parts[2]), int(parts[2])
		else:
			low, high = int(parts[0]), int(parts[1])
		best = compute(low, high, 100)[-1]
		print(best)
		while line != "|":
			i += 1
			line = l[i]
		continue
	t += "\n" + line
