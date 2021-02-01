from sympy import pi,sin,cos,acos,sqrt,oo
from os import system

class Solver():
    G=6.67428e-11

    def __input_mass(self):
        return float(input("Enter the mass of the palnet (M) in meters: "))

    def __input_init_r(self):
        return float(input("Enter inintial distance (r0) in meters: "))

    def __input_t(self):
        return float(input("Enter time (t) in seconds: "))
    
    def __input_r(self):
        return float(input("Enter (r) in meters: "))

    def __input_mass_and_init_r(self):
        M=self.__input_mass()
        r0=self.__input_init_r()
        return M,r0
    
    def calculate_alpha_of_t(self):
        M,r0=self.__input_mass_and_init_r()
        t=self.__input_t()
        omega=self.__omega_of_mass_and_init_r(M,r0)
        alpha=float(self.__alpha_of_t(t,omega))
        return r0,t,alpha

    def calculate_r_of_t(self):
        r0,t,alpha=self.calculate_alpha_of_t()
        r=float(r0*cos(alpha)**2)
        return r0,t,alpha,r

    def calculate_t_of_r(self):
        M,r0=self.__input_mass_and_init_r()
        r=self.__input_r()
        alpha=float(acos(sqrt(r/r0)))
        t_times_omega=self.__t_times_omega_of_alpha(alpha)
        omega=self.__omega_of_mass_and_init_r(M,r0)
        t=t_times_omega/omega
        return t,r

    def calculate_capital_t(self):
        M,r0=self.__input_mass_and_init_r()
        omega=self.__omega_of_mass_and_init_r(M,r0)
        capital_t=float(2*pi/omega)
        return capital_t


    def __alpha_of_t(self,t:float,omega:float):
        tOmega=t*omega

        if tOmega>pi/2:
            print("Can't solve currently.")
            return oo

        alphaLow=0
        alphaHigh=pi/2

        while(alphaLow<alphaHigh):
            alphaMid=(alphaLow+alphaHigh)/2
            tOmegaMid=self.__t_times_omega_of_alpha(alphaMid)

            if tOmegaMid>tOmega:
                if self.__t_times_omega_of_alpha(alphaLow)==tOmega:
                    return alphaLow
                alphaHigh=alphaMid

            if tOmegaMid<tOmega:
                if self.__t_times_omega_of_alpha(alphaHigh)==tOmega:
                    return alphaHigh
                alphaLow=alphaMid

            if tOmegaMid==tOmega:
                return alphaMid

        return -oo

    def __t_times_omega_of_alpha(self,alpha:float):
        return float(sin(2*alpha)/2+alpha)

    def __omega_of_mass_and_init_r(self,M,r0):
        return sqrt(2*Solver.G*M/r0**3)