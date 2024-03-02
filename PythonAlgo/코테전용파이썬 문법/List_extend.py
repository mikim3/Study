x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.append(y) # x: ['Tick', 'Tock', 'Song', ['Ping', 'Pong']]
print('x:', x)

x = ['Tick', 'Tock', 'Song']
y = ['Ping', 'Pong']
x.extend(y) # x: ['Tick', 'Tock', 'Song', 'Ping', 'Pong']  
print('x:', x)


x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.append(y)
print('x:', x)

x = ['Tick', 'Tock', 'Song']
y = [['Ping', 'Pong']]
x.extend(y)
print('x:', x)


x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.append(y)
print('x:', x)

x = ['Tick', 'Tock', 'Song']
y = 'Ping'
x.extend(y)
print('x:', x)