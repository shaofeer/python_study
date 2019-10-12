import  json

from src.Person import Person

p = Person("shaofei",10)

print(p.tostring())

# num=[1,2,3,4]
with open("json.json",'a') as jf:
    json.dump(p.tostring(),jf)
    # json.dump(p,jf)
    # number = json.load(jf)

# print(number)

