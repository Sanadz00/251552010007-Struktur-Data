import heapq

pq = []

heapq.heappush(pq, (3, 'TASK C - RENDAH'))
heapq.heappush(pq, (1, 'TASK A - DARURAT'))
heapq.heappush(pq, (2, 'TASK B - BIASA AJA'))

print('Priotity Queue: ', pq)

while pq:
    Prioritas, task = heapq.heappop(pq)
    print(f'[Priotitas {Prioritas}] Proses: {task}')