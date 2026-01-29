#Calculator source code
def my_len(text):
    length = 0
    for i in text:
        length = length + 1
    return length


def my_split(expression):
    number = ""
    array = []
    for i in range(my_len(expression)):
        if expression[i] in "0123456789":
            number += expression[i]
        elif expression[i] in "+-*":
            if number:
                array += [number]
                number = ""
            array += [expression[i]]
        elif expression[i] == "/":
            # this is done to check whether the next character is / or not
            if i + 1 < my_len(expression) and expression[i + 1] == "/":
                if number:
                    array += [number]
                    number = ""
                array += ["//"]
                expression = expression[:i+1] + " " + expression[i+2:]
            else:
                if number:
                    array += [number]
                    number = ""
                array += ["/"]

        elif expression[i] == " ":
            if number:
                array += [number]
                number = ""

    if number:
        array += [number]

    return array

print("You need to enter the expression in one input for instance: 5 + 7 - 3*2")
exp = input("Enter the expression you want to calculate: ")
exp = my_split(exp)
result = 0
exp1 = []
print(exp)
#In the first stage, we will calculate the operations that have higher priority(*/)
for i in range(my_len(exp)):
    if exp[i]=="*":
        exp[i-1] = float(exp[i-1])*float(exp[i+1])
        exp[i] = "#"
        exp[i+1] = "#"
    elif exp[i]=="/":
        try:
            exp[i-1] = float(exp[i-1])/float(exp[i+1]) 
            exp[i] = "#"
            exp[i+1] = "#"
        except ZeroDivisionError:
            raise ZeroDivisionError("You can not divide by zero")
    elif exp[i]=="//":
        try:
            exp[i-1] = int(exp[i-1])//int(exp[i+1])
            exp[i]="#"
            exp[i+1] = "#"
        except ZeroDivisionError:
            raise ZeroDivisionError("You can not divide by zero!")

clean = []
for i in exp:
    if i!="#":
        clean+=[i]
exp = clean
#second stage(+-)
result = float(exp[0])
for i in range(1,my_len(exp),2):
    if exp[i] == "+":
        result += float(exp[i+1])
    elif exp[i]== "-":
        result -= float(exp[i+1])

print(result)