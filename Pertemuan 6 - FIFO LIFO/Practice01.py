stack = [] #Data Kosongan dulu sebelum di input pakai append
stack.append('5')
stack.append('3')
stack.append('4')
stack.append("3")

top = stack[-1] #top(nama buat liat atasnya) stack[-1]:Function buat ngepeek

popped = stack.pop()

print("KOSONG?", len(stack)==0) 
#Misalnya cuma ada 1 terus di pop, nilai nya kan kosong. makanya True. tpi kalau adaan isinya jadinya false
print("ukuran:", len(stack))
print(top)
print(stack)
