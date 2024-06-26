import sys

pwd = sys.argv[1:][0]
if pwd == "1234":
    print("PWD successfully evaluated, encrypted and injected!")
else:
    print("Could not evaluate PWD!")