## Assignment Part-1
Q1 - Q25 solutions in PythonAssignment-1.md

Q26. What is a string? How can we declare string in Python?
String is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation. Python has a built-in string class named str . Python strings are "immutable" which means they cannot be changed after they are created.

Q27. How can we access the string using its index?
String index start with zero. So if, a = 'charger', then `a[2] == 'a'`.

Q28. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "iNeuron"

a = "Big Data iNeuron"
print(a[-7:])
```

Q29. Write a code to get the desired output of the following
```
string = "Big Data iNeuron"
desired_output = "norueNi"

a = "Big Data iNeuron"
print(a[:-8:-1])
```
Q30. Reverse the string given in the above question.
`print(a[::-1])`

Q31. How can you delete entire string at once?
del a

Q32. What is escape sequence?
An escape sequence is a sequence of characters that, when used inside a character or string, does not represent itself but is converted into another character or series of characters.     

Q33. How can you print the below string?
```
'iNeuron's Big Data Course'

print("'iNeuron's Big Data Course'")
```

Q34. What is a list in Python?
Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Q35. How can you create a list in Python?
```
a = [1,2,3]
```

Q36. How can we access the elements in a list?
```
a[0]
a[-1]
```

Q37. Write a code to access the word "iNeuron" from the given list.
```
lst = [1,2,3,"Hi",[45,54, "iNeuron"], "Big Data"]
lst[-2][-1]
``` 

Q38. Take a list as an input from the user and find the length of the list.
```
a = input('Enter a list').split()
```

Q39. Add the word "Big" in the 3rd index of the given list.
```
lst = ["Welcome", "to", "Data", "course"]
lst.insert(3, 'Big')

```

Q40. What is a tuple? How is it different from list?
Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable.

Q41. How can you create a tuple in Python?
```
a = (1,2)
```

Q42. Create a tuple and try to add your name in the tuple. Are you able to do it? Support your answer with reason.
```
a = ('Ola','Amigos')
a[0] = 'Rolls'
```
TypeError: 'tuple' object does not support item assignment
Because, tuples are immutable.

Q43. Can two tuple be appended. If yes, write a code for it. If not, why?
No. Cause tuples cannot be modified.

Q44. Take a tuple as an input and print the count of elements in it.
```
a = tuple(input('Enter tuple: ').split())
print(len(a))
```
Q45. What are sets in Python?
Sets are used to store multiple items in a single variable. Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage. A set is a collection which is unordered, unchangeable*, and unindexed.

Q46. How can you create a set?
```
a = set([1,2,3])
```
Q47. Create a set and add "iNeuron" in your set.
```
a = set(['google','amazon'])
a.add('iNeuron')
```
Q48. Try to add multiple values using add() function.
```
Can't do.
```

Q49. How is update() different from add()?
We use add() method to add single value to a set. We use update() method to add sequence values to a set. Here Sequences are any iterables including list , tuple , string , dict etc.

Q50. What is clear() in sets?
Deletes the elements of the set.

Q51. What is frozen set?
Frozen set is just an immutable version of a Python set object. While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. Due to this, frozen sets can be used as keys in Dictionary or as elements of another set.

Q52. How is frozen set different from set?
It is immutable after creating.

Q53. What is union() in sets? Explain via code.
Union combines sets dropping duplicates.
```
a = set([1,2,3])
b = set([1,2,4,5,6])
print(a.union(b))
# {1, 2, 3, 4, 5, 6}
```

Q54. What is intersection() in sets? Explain via code.
Intersection keeps common element in sets.
```
a = set([1,2,3])
b = set([1,2,4,5,6])
print(a.intersection(b))
# {1, 2}
```

Q55. What is dictionary ibn Python?
Dictionaries are Python's implementation of a data structure that is more generally known as an associative array. A dictionary consists of a collection of key-value pairs. Each key-value pair maps the key to its associated value.

Q56. How is dictionary different from all other data structures.
It is a key-value map, and fetching a value is O(1).

Q57. How can we delare a dictionary in Python?
```
a = {'ha':1}
```

Q58. What will the output of the following?
```
var = {}
print(type(var))
```
dict

Q59. How can we add an element in a dictionary?
```
s = {}
s['no'] = 34
```

Q60. Create a dictionary and access all the values in that dictionary.
```
s = {'a':0,'e':1,'i':2,'o':3,'u':4}
s.values()
```

Q61. Create a nested dictionary and access all the element in the inner dictionary.
```
s = {'no': {'ra':'party'}}
s['no']['ra']
```

Q62. What is the use of get() function?
Retrieves value of a key, and can default to a value if no key is found.

Q63. What is the use of items() function?
The items() method returns a view object. The view object contains the key-value pairs of the dictionary, as tuples in a list.

Q64. What is the use of pop() function?
The pop() method removes the element at the specified position.

Q65. What is the use of popitems() function?
The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.

Q66. What is the use of keys() function?
The keys() method returns a view object. The view object contains the keys of the dictionary, as a list.

Q67. What is the use of values() function?
values() is an inbuilt method in Python programming language that returns a view object. The view object contains the values of the dictionary, as a list.

Q68. What are loops in Python?
Python programming language provides the following types of loops to handle looping requirements. 

Q69. How many type of loop are there in Python?
Two

Q70. What is the difference between for and while loops?
Both for loop and while loop is used to execute the statements repeatedly while the program runs. The major difference between for loop and the while loop is that for loop is used when the number of iterations is known, whereas execution is done in the while loop until the statement in the program is proved wrong.

Q71. What is the use of continue statement?
A continue statement ends the current iteration of a loop. Program control is passed from the continue statement to the end of the loop body. A continue statement can only appear within the body of an iterative statement, such as do , for , or while .

Q72. What is the use of break statement?
The break statement is frequently used to terminate the processing of a particular case within a switch statement. Lack of an enclosing iterative or switch statement generates an error.

Q73. What is the use of pass statement?
The pass statement is used as a placeholder for future code. When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed. Empty code is not allowed in loops, function definitions, class definitions, or in if statements.

Q74. What is the use of range() function?
The range() is an in-built function in Python. It returns a sequence of numbers starting from zero and increment by 1 by default and stops before the given number. It has three parameters, in which two are optional: start: It's an optional parameter used to define the starting point of the sequence.

Q75. How can you loop over a dictionary?
```
for i,j in a.items():
    print(i,j)
```

### Coding problems
Q76. Write a Python program to find the factorial of a given number.
```
num = int(input("Enter a number: "))
facts = 1

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       facts = facts*i
   print("The factorial of",num,"is",facts)
```

Q77. Write a Python program to calculate the simple interest. Formula to calculate simple interest is SI = (P*R*T)/100
```
p = input('P')
r = input('R')
t = input('T')

print('SI = ',(p*r*t)/100)
```

Q78. Write a Python program to calculate the compound interest. Formula of compound interest is A = P(1+ R/100)^t.
```
p = input('P')
r = input('R')
t = input('T')

print('A = ', p*((1+(r/100))**t))
```

Q79. Write a Python program to check if a number is prime or not.
```
num = int(input("Enter a number: "))
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")
```
Q80. Write a Python program to check Armstrong Number.
```
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
```

Q81. Write a Python program to find the n-th Fibonacci Number.
```
def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(20))
```

Q82. Write a Python program to interchange the first and last element in a list.
```
def changer_list(a):
    a[0], a[-1] = a[-1], a[0]
    return a
```
Q83. Write a Python program to swap two elements in a list.
```
def swapPositions(li, pos1, pos2):
     
    li[pos1], li[pos2] = li[pos2], li[pos1]
    return li
```
Q84. Write a Python program to find N largest element from a list.
```
def Nmaxelements(list1, N):
    final_list = []
    for i in range(0, N):
        max1 = 0
        for j in range(len(list1)):    
            if list1[j] > max1:
                max1 = list1[j]; 
        list1.remove(max1);
        final_list.append(max1)
         
    print(final_list)
```

Q85. Write a Python program to find cumulative sum of a list.
```
def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]
```

Q86. Write a Python program to check if a string is palindrome or not.
```
def isPalindrome(s):
    return s == s[::-1]
```

Q87. Write a Python program to remove i'th element from a string.
```
def remove(string, i): 
    a = string[ : i] 
    b = string[i + 1: ]
    return a + b
```

Q88. Write a Python program to check if a substring is present in a given string.
```
if substring in s:
    print("yes")
else:
    print("no")
```

Q89. Write a Python program to find words which are greater than given length k.
```
def string_k(k, str):
    string = []
    text = str.split(" ")
    for x in text:
        if len(x) > k:
            string.append(x)
    return string
```

<!-- Q90. Write a Python program to extract unquire dictionary values. -->

Q91. Write a Python program to merge two dictionary.
```
def add_dict(a,b):
    for i,j in a.items():
        b[i] = j
    return b
```

Q92. Write a Python program to convert a list of tuples into dictionary.
```
Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}

dict([('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)])
```

Q93. Write a Python program to create a list of tuples from given list having number and its cube in each tuple.
```
Input: list = [9, 5, 6]
Output: [(9, 729), (5, 125), (6, 216)]

[(i, i**3) for i in list]
```

Q94. Write a Python program to get all combinations of 2 tuples.
```
Input : test_tuple1 = (7, 2), test_tuple2 = (7, 8)
Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]

a = [*itertools.product((7,2),(7,8))] 
b = [(j,i) for i,j in a]
result = a + b
```

Q95. Write a Python program to sort a list of tuples by second item.
```
Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

sorted(a, key=lambda x: x[1])
```

Q96. Write a python program to print below pattern.
```
* 
* * 
* * * 
* * * * 
* * * * * 

for i in range(1,6):
    print('* '*i)
```
Q97. Write a python program to print below pattern.
```
    *
   **
  ***
 ****
*****

for i in range(1,6):
    print(' '*(5-i)+'*'*i)
```

Q98. Write a python program to print below pattern.
```
    * 
   * * 
  * * * 
 * * * * 
* * * * * 

```

Q99. Write a python program to print below pattern.
```
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

for i in range(1,6):
    for j in range(1,i+1):
        print(str(j), end=' ')
    print('\n')
```

Q100. Write a python program to print below pattern.
```
A 
B B 
C C C 
D D D D 
E E E E E 

for i in range(1,6):
    for j in range(0,i):
        print(chr(64+i), end=' ')
    print('\n')
```


