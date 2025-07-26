#zip

lst1=['ansh','Ankush','Roma','Jagat']
lst2=[23,45,21,88]
print(list(zip(lst1,lst2)))
print('-'*30)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])
print([list(row) for row in zip(*[list(row) for row in zip(*matrix)])])
print('-'*30)

lst_1=[2,4,6]
lst_2=[81,3,5]
print(sum([i*j for i,j in zip(lst_1,lst_2)]))
print('*'*50)

lst=[1,2,3,4,5,6,7]
def is_even(n):
    return n%2==0
print(list(filter(is_even,lst)))
print('*'*50)

#Lambda
add_num=lambda x,y:x*y
print(add_num(5,10))
print('*'*50)

num=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2==0,num)))
print('*'*50)

# Map
num=[1,2,3,4,5,6]
def sqr(x):
    return x**2
print(list(map(sqr,num)))
print('*'*50)

#ASCII code(ord)
print('A')
print(ord('A'))
print(ord(' '))

#chr
print(chr(48))
print(chr(78))

for i in range(32,127):
    print(i,chr(i))

text='Treksha'
for char in text:
    ascii_code=ord(char)
    print(f"The ASCII code of '{char}' is {ascii_code}")
