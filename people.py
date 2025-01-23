# algorithm
import json

# 1. ikka fileni oqib olishimiz kerak
f1 = open("people01.json")
f2 = open("people02.json")

p1 = json.loads(f1.read())
p2 = json.loads(f2.read())

# 2. unique personlarni aniqlash
p = []

for person in p1:
    if person not in p:
        p.append(person)

for person in p2:
    if person not in p:
        p.append(person)

# 3. people.json ga yozish
f = open('people.json', 'w')

json_data = json.dumps(p, indent=4)
f.write(json_data)

# close all files
f1.close()
f2.close()
f.close()
