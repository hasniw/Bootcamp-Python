import sys

if len(sys.argv) == 3 and sys.argv[1].isdigit() == True and sys.argv[2].isdigit() == True:
	Fnumber = int(sys.argv[1])
	Snumber = int(sys.argv[2])

	print(Fnumber + Snumber)
	print(Fnumber - Snumber)
	print(Fnumber * Snumber)
	print(Fnumber / Snumber)
	print(Fnumber % Snumber)
