"""1. What are the key features of Python?"""
"""Answer :
           1. Easy to use
           2. Open source and free
           3. Simple syntax
           4. Dynamic language 
           5. Platform independent

"""

""" 2. What are the Data Types in Python?
 Answer:
        1.string: text
        2. int:integer data type e.g 12
           float: floating point value e.g 12.3
           complex: real + imaginary e.g 2+3j
           boolean: True,False or 0,1
        3. list:[],mutable
           tuple:(),immutable 
           set: {},unique item , mutable
           dict:key-value pair ,{} ,mutable

"""
"""3. What are local variables and global variables in Python?
  Answer:
         local_veriables : variables defined inside a funtion can be accessed within function only.
         global_veriable : variables defined outside a funtion can be accessed everywhere
         
"""
"""4. How do you write comments in python? And Why Comments are important?
  Answer:
        Single-line comment: '#'
        Multi-line comment: """  """
        Comments plays important role in coding, sometimes we have use text to explain code in textual format,or for defining purpose
        which helps user to understand the code
        and it make code readable for others also

"""
"""5. How to comment on multiple lines in python?
  Answer:
        Using 3 opening and closing doulbe quote :   """  """
"""
"""6. What do you mean by Python literals?
  Answer: literals are value which is assigned to variable in int,float,text,boolean which can be used throughout program and it is permanent        
"""
"""7. What are different ways to assign value to variables?
  Answer:
         using '=' operator
         multiple values : x,y = 100

"""
"""8. What are the Escape Characters in python?
  Answer:
         \n: new line
         \t: new tab
         \b: backspace
"""
"""9. Which are the different ways to perform string formatting? Explain with
example.
  Answer:
         
"""
"""10. Write a program to print every character of a string entered by the user in a
new line using a loop
  Answer: 

a = input("Enter a string: ")
for i in a:
    print(i)
"""
"""12. Write a program to check if the word 'orange' is present in the "This is orange
juice".
  Answer:
b = "This is orange juice" 
if "orange" in b:
    print('present')
else:
    print("not present")
"""
"""13. Write a program to find the number of vowels, consonants, digits, and white
space characters in a string.
  Answer: 
in_string = input("Enter a string: ")
def count(in_string):
    a = 'aeiouAEIOU' 
    vowel_c = 0
    consonent = 0
    white_space = 0
    digit = 0
    character = 0

    for i in in_string:
        if i.isalpha():
            if i in a:
                vowel_c+=1
            else:
                consonent+=1
        elif i.isnumeric():
            digit+=1
        elif i.isspace():
            white_space+=1
       

    print("Vowel : ",vowel_c)
    print("consonent: ",consonent)
    print("digit: ",digit)
    print("white_space: ",white_space)

count1 = count(in_string)
"""
"""14. Write a Python program to count Uppercase, Lowercase, special character,
and numeric values in a given string.
  Answer:

input_string = input("Enter a string: ")
def count(input_string):
    upper_case = 0
    lower_case = 0
    digit = 0

    s_character=0

    for i in input_string:
        if i.isalpha():
            if i.isupper():
                upper_case+=1
            else:
                lower_case+=1
        elif i.isnumeric():
            digit+=1
        elif i in ascii(input_string):
            if i in range(32,48) or range(58,65) or range(91,97) or range(123,127):
                s_character+=1
       

    print("Upper case : ",upper_case)
    print("Lower case: ",lower_case)
    print("digit: ",digit)
    print("Special Character: ",s_character)

count1 = count(input_string)
"""
"""15. Write a program to make a new string with all the consonants deleted from the
string "Hello, have a good day".
  Answer:

a = "Hello, have a good day"
b = 'aeiouAEIOU'
new_string = ''
for i in a:
   if i in b:
     pass
   else:
      new_string+=i

print(new_string.replace(" ",""))
"""  
"""16. Write a Python program to remove the nth index character from a non-empty
string.
  Answer:

a =  input("Enter a string: ")
b = len(a)
print(a.replace(a[b-1],''))
"""        
       
"""7. Write a Python program to change a given string to a new string where the
first and last characters have been exchanged.
  Answer:
    
given_s = input("enter a string: ")
res = ''.join((given_s[-1],given_s[1:-1],given_s[0]))

print(res)
"""
"""18. Write a Python program to count the occurrences of each word in a given
sentence.
  Answer:


st = input("Enter a string: ")

for i in st:
    count = st.count(i)
    print(f"count of {i} is {count}")

"""   
"""19. How do you count the occurrence of a given character in a string?
  Answer: using count() funtion"""
    
"""20. Write a program to find last 10 characters of a string?
  Answer:


a = input("Enter a string:")
n = 10

last_ch = a[-10:]
print(last_ch)"
"""

"""21. WAP to convert a given string to all uppercase if it contains at least 2
uppercase characters in the first 4 characters.


"""