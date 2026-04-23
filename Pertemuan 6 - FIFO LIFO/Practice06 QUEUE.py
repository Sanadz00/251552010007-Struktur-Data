from collections import deque

queue = deque()

queue.append('a')
queue.append('b')
queue.append('c')

front = queue[0]
keluar = queue.popleft()

print("Kosonggg??!! ASTAGFIRULLAHALADZIM", len(queue)==0)
print('Ukuran:', len(queue))
