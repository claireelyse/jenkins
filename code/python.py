def greet(name):
    return f"Hello, {name}!"

def add_numbers(a, b):
    return a + b

#def unsafe_code(user_input):
#    # This is an example of unsafe code that may trigger a warning in a security scan.
#    exec(user_input)  # Avoid using exec with user input in real code!

if __name__ == "__main__":
    print(greet("World"))
    result = add_numbers(5, 7)
    print(f"Result of addition: {result}")

#    # Simulate unsafe input
#    unsafe_code("print('This is unsafe!')")