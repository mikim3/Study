import sys
input = sys.stdin.readline

n = int(input())
cmd = []
setVar = set()

for i in range(n):
    cmd= list(map(str, input().split()))
    if (cmd[0] == 'add'):
        setVar.add(cmd[1])
    elif (cmd[0] == 'remove'):
        if cmd[1] in setVar:
            setVar.remove(cmd[1])
    elif (cmd[0] == 'check'):
        if cmd[1] in setVar:
            print(1)
        else:
            print(0)
    elif (cmd[0] == 'toggle'):
        if cmd[1] in setVar:
            setVar.remove(cmd[1])
        else:
            setVar.add(cmd[1])
    elif (cmd[0] == 'all'):
        setVar.update(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17','18','19', '20'])
        # for j in range(1,21):
        #     if str(j) in setVar:
        #         continue
        #     else:
        #         setVar.add(str(j))
    elif (cmd[0] == 'empty'):
        setVar.clear()
    # print(setVar)
