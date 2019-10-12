import csv

temp_data = set()
stand_data = []

with open('data_08.csv') as s:
    stc = csv.reader(s)

    for s in stc:
        temp_data.add(s.pop())

with open('stand_data.csv') as s:
    stc = csv.reader(s)

    for s in stc:
        stand_data.append(s.pop())

print("上传数据", temp_data)
print("必传数据", stand_data)
print(len(temp_data), len(stand_data))

true_data = []

for tt in temp_data:
    if tt in stand_data:
        true_data.append(tt)

print("符合数据个数", len(true_data))
print("符合数据", true_data)
