def sum_numbers(numbers):
    return sum(numbers)

def avg_numbers(numbers):
    return sum_numbers(numbers)/len(numbers)

def multiply_numbers(numbers):
    acum = 1
    for number in numbers:
        acum *= number
    return acum

def get_square_pow(numbers):
    return [number ** 2 for number in numbers]

def get_factorial(number):
    return number * get_factorial(number-1) if number > 0 else 1

def get_factorials(numbers):
    return [get_factorial(number) for number in numbers]

def print_value(operation, value):
    [print(f'El resultado de {operation} en el numero {index + 1} es: {val}') for index, val in enumerate(value)] if isinstance(value, list) else print(f'El resultado de {operation} es: {value}')

def main():
    numbers = [int(number) for number in input('Numeros: ').replace(' ', '').split(',')]
    print_value('suma', sum_numbers(numbers))
    print_value('promedio', avg_numbers(numbers))
    print_value('multiplicacion', multiply_numbers(numbers))
    print_value('elevar al cuadrado', get_square_pow(numbers))
    print_value('calcular factorial', get_factorials(numbers))

main()