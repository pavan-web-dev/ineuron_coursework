## Assignment Part-1
Q1. Why do we call Python as a general purpose and high-level programming language?
Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn’t specialized for any specific problems. This versatility, along with its beginner-friendliness, has made it one of the most-used programming languages today.

Q2. Why is Python called a dynamically typed language?
Because, during run time Python allows to store values of different data types. For example, as the start if x = 5, then later in the code I can set x = 'Onion'.

Q3. List some pros and cons of Python programming language?
|           Pros          |                         Cons                        |
|:-----------------------:|:---------------------------------------------------:|
| Beginner-friendly       | Issues with design                                  |
| Large Community         | Slower than compiled languages                      |
| Flexible and Extensible | Security                                            |
| Extensive Libraries     | Work Environment                                    |
| Embeddable              | High memory consumption                             |
| Highly Scalable         | Dynamically-typed language                          |
| IoT Opportunities       | Complex multithreading                              |
| Portable                | Garbage collection leads to potential memory losses |

Q4. In what all domains can we use Python?
Python can be used in every domain, like, Healthcare, Financial Analysis, Stock Trading, Self driving Cars, Military, Research, etc.

Q5. What are variable and how can we declare them?
A Python variable is a symbolic name that is a reference or pointer to an object. To declare a variable state its name and add a value into it.        
Example,            
x = 5       
s = 'sandunes'     

Q6. How can we take an input from the user in Python?
Use the `input()` function.

Q7. What is the default datatype of the value that has been taken as an input using input() function?
The default datatype is a `str`.

Q8. What is type casting?
Type casting is converting a variable from one datatype to the other. For example,         
x = 5
x1 = str(x)

Q9. Can we take more than one input from the user using single input() function? If yes, how? If no, why?
Yes, you can take multiple inputs with the same input() function. You need to seperate them with a particular delimiter and use the `split()` function to split the single input into multiple values. But, whenever we call the `input()` function the input is just one block of string.

Q10. What are keywords?
Python keywords are special reserved words that have specific meanings and purposes and can't be used for anything but those specific purposes. These keywords are always available—you'll never have to import them into your code.

Q11. Can we use keywords as a variable? Support your answer with reason.
You can use keywords as a variable, but it is not a good practice and strongly adviced not to use keywords as your variable names. The reason is that these keywords carry special meaning and might confuse the interpreter.

Q12. What is indentation? What's the use of indentaion in Python?
Indentation refers to the spaces at the beginning of a code line. Where in other programming languages the indentation in code is for readability only, the indentation in Python is very important. It helps us group our code into logical blocks and is needed for the interpreter to differentiate between various code segments. 

Q13. How can we throw some output in Python?
Use the `print()` statement.

Q14. What are operators in Python?
In Python, operators are special symbols that designate that some sort of computation should be performed. The values that an operator acts on are called operands. Here is an example: >>> >>> a = 10 >>> b = 20 >>> a + b 30. In this case, the + operator adds the operands a and b together.

Q15. What is difference between / and // operators?
In Python programming, you can perform division in two ways. The first one is Float Division("/") and the second is Integer Division("//") or Floor Division. The first one is the one we have learned in school and is the normal division. The second one omits the values after decimal and just gives you the whole number.

Q16. Write a code that gives following as an output.
```
iNeuroniNeuroniNeuroniNeuron
```
`'iNeuron' * 4`

Q17. Write a code to take a number as an input from the user and check if the number is odd or even.
```
a = input('Input a number')
a = int(input('Input a number: '))
if a % 2 == 0:
    print('Even')
else:
    print('Odd')
```

Q18. What are boolean operator?
Boolean Operators are simple words (AND, OR, NOT or AND NOT) used as conjunctions to combine or exclude keywords in a search, resulting in more focused and productive results.

Q19. What will the output of the following?
```
1 or 0

0 and 0

True and False and True

1 or 0 or 0
```
1
0
False
1

Q20. What are conditional statements in Python?
A conditional statement as the name suggests itself, is used to handle conditions in your program. These statements guide the program while making decisions based on the conditions encountered by the program. Python has 3 key Conditional Statements that you should know: if statement. if-else statement.

Q21. What is use of 'if', 'elif' and 'else' keywords?
You use if for a single condition, elif to add more conditional statements, and else is to add a fall back mechanism in case a if condition fails. Note else is not always needed and depends on the logic you are writing.

Q22. Write a code to take the age of person as an input and if age >= 18 display "I can vote". If age is < 18 display "I can't vote".
```
age = int(input('Enter age: '))

if age >= 18:
    print('I can vote')
else:
    print('I can't vote')
```
Q23. Write a code that displays the sum of all the even numbers from the given list.
```
numbers = [12, 75, 150, 180, 145, 525, 50]
```
sum([i for i in numbers if i % 2 == 0])

Q24. Write a code to take 3 numbers as an input from the user and display the greatest no as output.
```
a = input('Enter Number 1')
b = input('Enter Number 2')
c = input('Enter Number 3')

print('Max is:',max(a,b,c))
```

Q25. Write a program to display only those numbers from a list that satisfy the following conditions

- The number must be divisible by five

- If the number is greater than 150, then skip it and move to the next number

- If the number is greater than 500, then stop the loop
```
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i > 150:
        continue

    # This will never because a number greater than 500 is always greater than 150.
    if i > 500:
        break

    if i % 5 == 0:
        print(i)
```