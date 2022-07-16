import re
try:
    cells = int(input("Number of Cells: "))
except Exception as e: 
    print(e)
    raise SystemExit()
text = "text"
text = text.lower()
text = re.sub(r'\W+', ' ', text)
array = text.split(" ")
first = []
ing = []
s = []
filtered = []

for i in array:
    if (len(i)==cells):
        first.append(i)
    elif (len(i) == cells + 3 and i[-3:] == "ing"):
        ing.append(i[0:-3])
    elif (len(i) == cells +1 and i[-1]=="s"):
        s.append(i[0:-1])
results = first + ing + s
#for i in results:
#    if (i[1]=="o" and i[-1]=="n" and "c" not in i and "i" not in i and "h" not in i and "d" not in i and "l" not in i):
#        filtered.append(i)
unique = list(set(results))
print(unique)
