from Option import Option
from util import clearScr
from Solver import Solver

def calculate_alpha_of_t():
    _,t,alpha=Solver().calculate_alpha_of_t()
    print("α( t =",t,") = ",alpha,"rad")

def calculate_r_of_t():
    r0,t,_,r=Solver().calculate_r_of_t()
    print("r( t =",t,") = ",r,"m")
    print("Δr( t =",t,") = ",r0-r,"m")

def calculate_t_of_r():
    t,r=Solver().calculate_t_of_r()
    t_in_days=__time_in_days(t)
    print("t( r =",r,") = ",t,"= s",t_in_days,"days")

def calculate_capital_t():
    capital_t=Solver().calculate_capital_t()
    capital_t_in_days=__time_in_days(capital_t)
    print("T = ",capital_t,"= s",capital_t_in_days,"days")
    print("T(one fall) = ",capital_t/4,"= s",capital_t_in_days/4,"days")

def __time_in_days(t:float):
    return t/60/60/24

def back():
    import home
    home.show_home()

_calculations=[
    Option("Calculate α(t)",calculate_alpha_of_t),
    Option("Calcualte r(t)",calculate_r_of_t),
    Option("Calculate t(r)",calculate_t_of_r),
    Option("Calculate T",calculate_capital_t),
    Option("Back",back)
]

def show_calculations():
    Option.show_options(_calculations)

    calcNum=int(input("Choose calculation: "))

    clearScr()

    if 1 <= calcNum < len(_calculations):
        _calculations[calcNum-1].fun()
        print("---------------------------------------")
        back()
    elif calcNum == len(_calculations):
        back()
    else:
        print("Error!!")
        print("Enter the number of a calculation.")
        show_calculations()
