from util import clearScr
from Option import Option

def do_calculation():
    clearScr()
    import calculations
    calculations.show_calculations()

def exit_app():
    print("Good bye!")
    exit()

_options=[
    Option(
        "Do a calculation",
        do_calculation
    ),
    Option(
        "Exit",
        exit_app
    )
]

def show_home():
    clearScr()
    print("Welcome to gravity solver!")
    show_options()
    

def show_options():

    Option.show_options(_options)

    optionNum=int(input("Choose option: "))

    if 1 <= optionNum <= len(_options):
        _options[optionNum-1].fun()

    else:
        clearScr()
        print("Error!!")
        print("Enter the number of an option.")
        show_options()
