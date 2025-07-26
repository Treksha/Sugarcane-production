# n = 30
# i=1
# s=0
# while(n>s):
#     print(s)
#     i+=1
#     s= s+i
# c=1
# while c<=3 :
#     n =1
#     while n<=2:
#         print(f"{c},{n}")
#         c+=1
#         n+=1
# while True:
#     age = int(input("enter your age:"))
#     if age>=0 :
#         break
#     else:
#         print("please enter a valid age:")
numbers=[]
while True:
    user_input= input("enter a positive number(enter a non positive number to stop):")
if user_input.replace('.',"",1).isdigit()and float(user_input)>0:
    numbers.appebd(float(user_input))
elif user_input.replace('-',"",1).isdigit()and float(user_input)<=0:
  none 
else:
    print("invalid input.please enter a valid positive number")
if numbers:
    print(f"you entered the following positive numbers:{numbers}")
else:
    print("no positive numbers were entered")        
