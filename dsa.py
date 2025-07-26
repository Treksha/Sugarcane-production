# list=[1,2.3,'hello','ansh']
# print(list)
# #access the element through indexing
# print(list[0])
# print(list[-1])

# # modify values
# list[2]="neeta"
# print(list)

# #slicing
# print(list[1:4])

# #reverse  a slicing
# print(list)
# print(list[::-1])

# #appending
# print(list)
# list.remove("ansh")

# #length
# print(list)
# print(len(list))

# #sorting
# lst=[4,3,6,0,9,1]
# print(lst)
# print(sorted(lst))

# #find elment
# print(lst.index(6))
# print(max(lst))

# #iterating the list

# for i in lst:
#     print(i)
# for i in range((len(lst))-1): 
#     print(lst[::-1],end=' ')   
# multidimentional list
# lst=[[1,2,3],[4,5,6],[7,8,9],"\n"]
# for i in lst:
#     for j in i:
#         print(j)
# # append the list
# lst.append([2])  
# print(lst)
# print(len(lst))
# # exdending the list      
# list=[[1,2,3],[4,5],[6,7,9]]
# print(max(list))
# # list.extend(lst)
# # print(list)
# # # reverse the list
# #for i in list:
# list.reverse()
# print(list)
#accesing each element
# for i in list:
#     print(i,end='--')
#     print('\n')
# accesing each element of a 2D list
# for i in range(len(list)):
#     for j in range (len(list[i])):
#         print(list[i][j],end=" ")
#         # print(max(list))
# #replacing
# # print('\n')
# # list[1][1]=3
# # list[2]=['ansh',22]
# # print(list)
# # print('\n') 
# # print(list[::-1])
# #max value in 2D list
# def find_max_value(matrix):
#     max_value=float('-inf')
#     for row in matrix:
#         max_value= max(max_value,max(row))
#     return max_value
# matrix=[[3,7,1,2],[8,5,6,4],[2,1,7,9]] 
# max_value=find_max_value(matrix) 
# print("\nmaximux value:",max_value)  

# # list chompresive
# for i in range(1,11):
#     print(i**2)
# print([i for i in range (21) if i%2==0]) 
# print('-'*20)   
# print([i**2 for i in range(21) if i%2==0])
# lst=[[j for j in range (1,4)] for i in range(3)]
# print(lst)

# #dictionary 
# dct={1: 'ansh', 2:'avneet',3:'riya',2:'rani','meena' :4}
# print(dct)
# #accessing the element
# print(dct[2])
# print(dct.get(3))

# # adding and update
# dct[5]=" anayana"
# dct[6]='naina'
# print(dct)
# del dct[6]
# print(dct)
# # dct.clear()
# # print(dct)
# # #iterating through the dictionary
# print(dct.keys())
# print(dct.get('name'))
# print(dct)
# print(dct.values())
# print(dct)
# # multidimentional dictonary
# dct={ 1: {'name' : 'arav','phone': 23456754  , 'place' : { 'j':'nagpur' }} ,
#      2: {'name' : 'ansh','phone': 2145}  ,
#      3: {'name' : 'anuj','phone': 2325},
#      4: {'name' : 'ansh','phone': 2345}}
# print(dct)
# print(dct[1])
# del dct[3]
# print(dct)
# # going through the data
# for i in dct.keys():
#     print(i,dct[i]['name'])
# # ditionary chompress
# dct= {i: i**2 for i in range(1,6)}
# print(dct) 
 # dictionaries from list
# lst= ['apple','banana','grapes'] 
# dct= {item: len(item) for item in lst}
# print(dct)
# print('-'*20)
# # special keys with string
# dct = {'num' + str(i): i for i in range(1,11)}
# print(dct)
# dct= {k:v for k,v in dct.items() if v%3==0}
# print(dct)
# # 
# matrix =[[1,2,3],[4,5,6],[9,8,5]]
# final_dct= {(i,j): matrix[i][j] for i in range(2) for j in range(3)}
# print(final_dct)
# find  common element
def find_common_element(lists):
    common_element={element: min(lst.count(element) for lst in list) for element in set.intersection(*map(set,lists))}
    return common_element
list1= [1,2,3,1]
list2= [4,5,2,6]
list3= [7,5,8,9]
result= find_common_element([list1,list2,list3])
for element, frequency in result.items():
    print(f"Element:{element}, Frequency: {frequency}")

# set and tuple
set={1,2,3,4,5}
print(type(set))

#adding 
print(set)
set.add(8)
print(set)

#pop
popped_element= set.pop()
print(popped_element)

#remove
print(set)
set.discard(3)

#iterate
for i in set:
    print(i)

# set operation
set1={1,2,3,4,}
set2={5,6,7,8,4}
setu=set1.union(set2)    
seti=set1.intersection(set2)
setd=set1.difference(set2)
sets=set1.symmetric_difference(set2)      
print(setu) 
print(seti) 
print(setd) 
print(sets)  

#tuple
tpl1=(1,2,3,4,5)
tpl2=(9,8,7,6,5)
tpl=tpl1+tpl2
print(tpl)
for i in tpl2:
    print(i)
print(tpl1[1:4]) 
   