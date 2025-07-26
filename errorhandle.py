try:
    print(1)
    x=10
    print(x/0)
    print(2)
except:
    print('error occured')   

# exception with specific error
try:
    num=0
    print(num*'0.5')
except ZeroDivisionError:
    print('zero is  in the division')
except:
    print('unknown error')


#final exception with specific error
try:
    num1, num2 =6,5
    print(num1/num2)
    # print(int('3,12'))# error
except Exception as e:
    print(e)
else:
    print('everything is fine!')
finally:
    print('program end!')            