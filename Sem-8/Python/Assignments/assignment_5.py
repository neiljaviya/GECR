import sys

if len(sys.argv) < 3:
    print("Please enter valid input")
    exit()

k = int(sys.argv[1])
msg = sys.argv[2]
middle = []

for char in msg:
    if char == ' ':
        middle.append('*')
    else:
        middle.append(char)

while len(middle) % k != 0:
    middle.append('$')

l=len(middle)
array = []
for i in range(0, l, k):
    array.append(middle[i:i+k])

array.reverse()

result = []

for i in range(k):
    tmp = [x[i] for x in array]
    result.append(''.join(tmp))

result = ''.join(result)
print(result)