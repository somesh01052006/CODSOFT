user_input =  input("enter + , - , * / ")
num1 = float(input("enter 1st num : "))
num2 = float(input("enter 2nd num : "))
if user_input == '+':
    print(num1,"+",num2,"=",num1+num2)
elif user_input == '-':
    print(num1,"-",num2,"=",num1-num2)
elif user_input == '*':
    print(num1,"*",num2,"=",num1*num2)
elif user_input == '/':
    print(num1,"/",num2,"=",num1/num2)    
    