import sys

k = int(sys.argv[1])
lst = [int(x) for x in sys.argv[2:]]
lst.sort()

l = len(lst)
if l % 2 == 0:
    median = (lst[int(l/2)-1] + lst[int(l/2)]) / 2
else:
    median = lst[int(l/2)]

less = [int(x) for x in lst if x < median]
less.reverse()
great =  [int(x) for x in lst if x > median]

result = []

for i in range(k):
    if l%2 != 0 and i == 0:
        result.append(median)
        continue
    if len(less) != 0 and len(great) != 0:
        if abs(less[0]-median) <= abs(great[0]-median):
            result.append(less[0])
            less.pop(0)
        elif abs(less[0]-median) > abs(great[0]-median):
            result.append(great[0])
            great.pop(0)
    elif len(less) != 0:
        result.append(less[0])
        less.pop(0)
    else:
        result.append(great[0])
        great.pop(0)
result.sort()
print(*(x for x in result))