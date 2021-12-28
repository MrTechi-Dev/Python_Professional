def difficulty_level(func):
    def wrapper( *args, **kwargs):
        n_lenghts = len(args)
        if n_lenghts == 1:
            print("it\'s an easy function")
        elif n_lenghts == 2:
            print ("it\'s a medium hard function")
        
        else:
            ("Is a hard function")
    return wrapper



@difficulty_level
def division( a:int, b: int)-> int:
    return a/b

division(2, 2, 4)