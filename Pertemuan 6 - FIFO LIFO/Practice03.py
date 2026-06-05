#membalik String (R3)

def balik_string(text):
    stack = []
    for char in text:
        stack.append(char)
    
    hasil = ''
    # Ambil kembali dari stack (LIFO) untuk membalikkan urutan
    while stack:
        hasil += stack.pop()
    return hasil

#Print
print(balik_string('Halo'))
print(balik_string("python"))
print(balik_string("racecar")) #dibalik juga tetep sama wkwk