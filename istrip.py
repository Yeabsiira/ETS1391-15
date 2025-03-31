text = "  Hello, world!  "
print(text.lstrip())        # Output: "Hello, world!  " (removes leading spaces)

text2 = "---Hello---"
print(text2.lstrip("-"))    # Output: "Hello---" (removes leading '-')

text3 = "xyzHelloxyz"
print(text3.lstrip("xyz"))  # Output: "Helloxyz" (removes 'x', 'y', and 'z' from the start)

text4 = "  Hello  "
print(text4.lstrip(" "))    # Output: "Hello  " (explicitly removes spaces from the start)
