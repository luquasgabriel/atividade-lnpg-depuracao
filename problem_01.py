def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

def get_numbers():
    numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in numbers] # Não é verificado se a entrada é vazia ou se os valores são inteiros válidos.
    return numbers

def main():
    numbers = get_numbers()
    if not numbers: # Então, aqui verifica se 'numbers' é uma lista vazia para que não continue a execução se verdadeiro (Não havia a verificação)
        print("No numbers entered.")
        return
    print("Average:", calculate_average(numbers))
    print("Maximum:", find_max(numbers))

if __name__ == "__main__":
    main()