from collections import deque

queue = deque()

queue.append('Asep')
queue.append('Junaedi')
queue.append('yusuf')
queue.append('LORD MIE AYAM SESEPUH KING MAHARAJA SESEPUH PENEMU')

deque(['Asep', 'Junaedi', 'yusuf', 'LORD MIE AYAM SESEPUH KING MAHARAJA SESEPUH PENEMU'])

print("ANTRIAN AWAL: ", list(queue))
print('_________MULAI MENGHAKIMI_________')

nomor = 1
while queue:
    pelanggan = queue.popleft()
    print(f'[{nomor}], Menghakimi: {pelanggan}')
    if queue:
        print(f'        ANTRIAN:{list(queue)}')
    nomor +=1

    print("____SEMUA PELANGGAN SUDAH DIHAKIMI____")