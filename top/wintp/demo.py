import sys

a = [x for x in dir(sys) if not x.endswith("_")]
print(a)

print(sys.api_version)
print(isinstance(sys.argv[0], str))

