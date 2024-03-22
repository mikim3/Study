q_num = 0
x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.append(y) # x: ['Tick', 'Tock', 'Song', ['Ping', 'Pong']]
print(q_num, 'x:', x)
q_num += 1

x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y) # x: ['Tick', 'Tock', 'Song', 'Ping', 'Pong']  
print(q_num, 'x:', x)
q_num += 1


x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.append(y)
print(q_num, 'x:', x)
q_num += 1

x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.extend(y)
print(q_num, 'x:', x)
q_num += 1


x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.append(y)
print(q_num, 'x:', x)
q_num += 1

x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.extend(y)
print(q_num, 'x:', x)
q_num += 1