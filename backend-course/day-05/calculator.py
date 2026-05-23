def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))

print("Сумма:", add(first_number, second_number))
print("Разность:", subtract(first_number, second_number))
print("Произведение:", multiply(first_number, second_number))