#author: RED 1/31/23

grades = {'Mid Year Project Presentation': 100, "Mid Year Project Proposal":90,"Mid Year Project Code":97, "Mid Year Project Reflection":93}

print(grades.values())

for k in grades:
    print(k)
for v in grades:
    if grades[v]>70:
        print(v)
    else:
        True
for v in grades:
    if grades[v] <50:
        print(v)
    else:
        True