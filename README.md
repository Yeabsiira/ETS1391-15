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