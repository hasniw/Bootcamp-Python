import sys

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
no_punct = ""
tab = []
final = [][]
i = 0
if len(sys.argv) == 3 and sys.argv[2].isdigit() == True:
	min = int(sys.argv[2])
	for char in sys.argv[1]:
		if char not in punctuations:
			no_punct = no_punct + char
	tab = no_punct.split()
	for test in tab:
		print(test)
	print("<------------------------->")
	for str in tab:
		if len(str) > min:
			final[i] = str
		else:
			pass
		i += 1
	print("['" + '\', \''.join(tab) + "']")
else:
	print("ERROR")
