# string methods

1. String Method upper()

The upper() method in Python is a built-in string method that converts all lowercase letters in a string to uppercase.


## Syntax

string.upper()


## Returns:
     A new string with all lowercase letters converted to uppercase.
     
     Non-alphabetic characters remain unchanged.

2 # String Method lower()

The lower() method in Python is a built-in string method that converts all uppercase letters in a string to lowercase.


## Syntax

string.lower()


## Returns:
     A new string with all uppercase letters converted to lowercase.
     
     Non-alphabetic characters remain unchanged.

3 # String Method title()

The title() method in Python is a built-in string method that converts the first letter of each word in a string to uppercase and the rest to lowercase.


## Syntax

string.title()


## Returns:
     A new string where the first letter of each word is capitalized, and the remaining letters are lowercase.
     
     Words are identified as sequences of alphanumeric characters separated by non-alphabetic characters (like spaces, dashes, etc.).

4 # String Method capitalize()

The capitalize() method in Python is a built-in string method that converts the first character of a string to uppercase and makes all other alphabetic characters lowercase.


## Syntax

string.capitalize()


## Returns:
     A new string where the first character is uppercase and the rest are lowercase.
     
     If the string starts with a non-alphabetic character, only the case of alphabetic characters is adjusted.

5. # String Method find()

The find() method in Python is a built-in string method that searches for a substring within a string and returns the index of the first occurrence. If the substring is not found, it returns -1.

## Syntax

string.find(substring, start, end)

## Parameters:
     substring → The string to search for.

     start (optional) → The index where the search begins. Default is 0.

     end (optional) → The index where the search ends. Default is the length of the string.


## Returns:
     The index of the first occurrence of the substring.
     
     -1 if the substring is not found.    

  6 # String Method index()

The index() method in Python is a built-in string method that searches for a substring within a string and returns the index of the first occurrence. If the substring is not found, it raises a ValueError.


## Syntax

string.index(substring, start, end)

## Parameters:

     substring → The string to search for.

     start (optional) → The index where the search begins. Default is 0.

     end (optional) → The index where the search ends. Default is the length of the string.




## Returns:
     The index of the first occurrence of the substring.
     
     Raises ValueError if the substring is not found.   

 7 ## `str.isalnum()`

Purpose: Checks if all characters in the string are alphanumeric (letters or numbers) and the string is not empty.

Return Value: True if all characters are alphanumeric and the string is not empty; False otherwise.

Example:


```

pro = "python3"
result = pro.isalnum()
print(result) # Output: True

pro2 = "python 3" #has a space between the words
result = pro2.isalnum()
print(result) #output: False

```   

8 ##  `str.count(substring)`

Purpose: Returns the number of non-overlapping occurrences of a substring within the string.

Return Value: An integer representing the number of occurrences.

Example:


```
text = "hello world hello"
count_of_hello = text.count("hello")
print(count_of_hello) # Output: 2

count_of_o = text.count("o")
print(count_of_o) # Output: 3
```

9  ##  `str.endswith(suffix)`

Purpose: Checks if the string ends with the specified suffix.

Return Value: True if the string ends with the suffix; False otherwise.

Example:


```
text = "Hello world"
ends_with_world = text.endswith("world")
print(ends_with_world) # Output: True

ends_with_hello = text.endswith("hello")
print(ends_with_hello) # Output: False

```