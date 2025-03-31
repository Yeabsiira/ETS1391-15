text = "  Hello, world!  "
print(text.strip())        # Output: "Hello, world!" (removes leading and trailing spaces)

text2 = "---Hello---"
print(text2.strip("-"))    # Output: "Hello" (removes leading and trailing '-')

text3 = "xyzHelloxyz"
print(text3.strip("xyz"))  # Output: "Hello" (removes 'x', 'y', and 'z' from both ends)

text4 = "  Hello  "
print(text4.strip(" "))    # Output: "Hello" (explicitly removes spaces)
