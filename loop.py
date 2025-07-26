n = ["data","science","python"]
for i in n:
    print(i)
print("dictionary iteration")
d=dict()
d['key1']= "val1"
d['key2']= 234
for i in d:
    print(i,d[i])
word= "python"
for letter in word:
    print(letter)
for i in range (4):
    for j in range(3):
        print(f"({i},{j})")
list=["data","power"]
for index , subject in enumerate(list):
    print(f"index:{index}, sub:{subject}")
squares = [x**3 for x in range(5)]
print(squares)