class Option():
    def __init__(self,value:str,fun):
        self.value=value
        self.fun=fun

    @staticmethod
    def show_options(options:list):
        for i,op in enumerate(options):
            print((i+1),"-",op.value)