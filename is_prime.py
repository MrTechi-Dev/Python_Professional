def is_prime(number:int) -> bool:
    result = [x for x in range (2, number) if number % x == 0]
    return len(result) == 0

def run():
    number = (int(input("escribe un numero")))
    #number: int = 4
    number_is_prime: bool = is_prime(number)
    print(f'Is {number} a prime number? {number_is_prime}')

if __name__=='__main__':
    run()