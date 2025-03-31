text = "Hello, world! Welcome to Python."

# Splitting by space (default behavior)
print(text.split())  # Output: ['Hello,', 'world!', 'Welcome', 'to', 'Python.']

# Splitting by a specific character
print(text.split(","))  # Output: ['Hello', ' world! Welcome to Python.']

# Splitting with maxsplit
print(text.split(" ", 2))  # Output: ['Hello,', 'world!', 'Welcome to Python.']
