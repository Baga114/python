from ast import operator


first_num = (input("entre first number: "));
operator = input(" entre operators (+,-,/,*,%) : ")
second_num = (input("entre first number: "));

first_num = int(first_num)
second_num = int(second_num)

if operator == "+":
    print("calculation of two is " + str(first_num + second_num));
elif operator == "-":
    print("calculation of two is " + str(first_num - second_num));
elif operator == "*":
    print("calculation of two is " + str(first_num * second_num));
elif operator == "/":
    print("calculation of two is " + str(first_num / second_num));
elif operator == "%":
    print("calculation of two is " + str(first_num % second_num));
else:
    print("error");
    