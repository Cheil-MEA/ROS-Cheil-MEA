def greet(name):
    """
    Greets the user with a personalized message.
    
    Args:
        name (str): The name of the user.
    
    Returns:
        str: A personalized greeting message.
    """
    return f"Hello, {name}! Welcome to Visual Studio."

def main():
    """
    Main function to demonstrate the greet function.
    """
    name = input("Enter your name: ")
    message = greet(name)
    print(message)

if __name__ == "__main__":
    main()

