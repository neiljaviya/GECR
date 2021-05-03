import sys

l = len(sys.argv)
if l < 1:
    print("Missing required inputs")
    exit()

branch = sys.argv[1]
file = open("accounts.txt")

balances = []

for line in file:
    info = line.split()
    if info[1] == branch:
        formatted = float(info[2])
        balances.append(formatted)

if len(balances) == 0:
    print("No such branch")
    exit()

print("Total Accounts: %d\nAverage Balance: %.2f Rs\nHighest Balance: %.2f Rs\nLowest Balance: %.2f Rs"%(len(balances), sum(balances)/len(balances), max(balances), min(balances)))