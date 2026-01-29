This README will explain how the code written works. 

I tried to avoid using built-in Python functions and instead use my own functions.

Let's start analyzing the code:
#Calculator source code
def my_len(text):
    length = 0
    for i in text:
        length = length + 1
    return length
This function just takes a text, and iterates through it, and in every iteration, a variable called length is incremented by 1, so at the end this length variable will be equal to the length of the text,

and after that we simply return this variable as the result. 
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

  Now lets start explaining this my_split function, I did not want to use the built-in split function and in order to solve the conflict with the split function, I named my function my-split.


  def my_split(expression):
    number = ""
    array = []
    for i in range(my_len(expression)):
        if expression[i] in "0123456789":
            number += expression[i] 

This part of the function ensures that the numbers are selected until something special, such as an operator or a space is seen, as we are trying to divide the expression into tokens


 elif expression[i] in "+-*":
       if number:
         array += [number]
          number = ""
        array += [expression[i]]

  Note that this part of the function is used to add the number variable to the array when "*+-" are met. I did not include / and // here because they will be handled in another part of this function.



  elif expression[i] == "/":
            # this is done to check whether the next character is / or not
            if i + 1 < my_len(expression) and expression[i + 1] == "/":
                if number:
                    array += [number]
                    number = ""
                array += ["//"]
                expression = expression[:i+1] + " " + expression[i+2:]

This part is ensured that the left operators are handled properly, the first if is used for the case when there is //, not just one /.


     else:
                if number:
                    array += [number]
                    number = ""
                array += ["/"] 

      
And in this part, we consider the case when there is one /.



        elif expression[i] == " ":
            if number:
                array += [number]
                number = ""

    if number:
        array += [number]

    return array 
This part is to ensure we do not add when we see a space and the number until that space, if exists, is added to the array. and then we simply return the array.

This function simply divided the expression into tokens.

So if you give it something like 5+3-7, it will convert this string into an array ["5","+","3","-","7"]


The following part of the code is actually very simple

print("You need to enter the expression in one input for instance: 5 + 7 - 3*2")
exp = input("Enter the expression you want to calculate: ")
exp = my_split(exp)
result = 0
exp1 = []
print(exp)
#In the first stage, we will calculate the operations that have higher priority(*,/,//)
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

Firstly, we prompt the user to enter the expression they want. Firslt, we are considering the case for *,/,// because in mathematics we firstly do these operations and then +,-

One thing I want to explain here is the usage of exp[i] = "#", this is a placeholder for the number so that in our next loops, this number is not calculated again

If I did not replace the actual number witht this, there is a strong possibility this number will be calculated twice or three times in our calculation which will make our result false.


There is simple try/except to raise error when divided by zero since we cant do it mathematically.
After this, the next part of the code is written to do +, -, since they have lower priority.


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


the clean variable is used to ensure that we remove the placeholders from our list, as they represent the numbers that were calculated previously.

We then take the first element of the array and we start from the second alament till the last element with a step of two because we will have the operators between the numbers.
After this loop ends, we will have the result variable ready. (Note that in this readme file, there might be indentation isssues, but there is not in the actual code)
