import pyfiglet

def print_name(func):
    def wrapper():
        name = func.__name__
        ascii_banner = pyfiglet.figlet_format(name)
        print(ascii_banner)
        func()
    return wrapper

@print_name
def Andres():
    print("Running function...")

Andres()