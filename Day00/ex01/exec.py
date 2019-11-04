import sys

del sys.argv[0]
sys.argv.reverse()
if len(sys.argv) >= 2:
    for string in sys.argv:
        print(string[::-1])
else:
    pass
