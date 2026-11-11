import math

# ==========================================
# БЛОК ФУНКЦІЙ
# ==========================================

# Функції для Завдання 1 (Квадратне рівняння)
def calc_discriminant(a, b, c):
    return b**2 - 4*a*c

def solve_quadratic(a, b, c):
    if a == 0:
        if b != 0:
            return -c / b
        return None

    d = calc_discriminant(a, b, c)

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    elif d == 0:
        return -b / (2 * a)
    else:
        return None

# Функції для Завдань 2 та 3 (Калькулятор)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


# ==========================================
# БЛОК ВИКОНАННЯ ПРОГРАМИ (ВВІД ТА ВИВІД)
# ==========================================

# --- Завдання 1 ---
print("\n--- Завдання 1: Квадратне рівняння ---")
a_quad = float(input("Enter a: "))
b_quad = float(input("Enter b: "))
c_quad = float(input("Enter c: "))

res = solve_quadratic(a_quad, b_quad, c_quad)
print("Result:", res)


# --- Завдання 2 ---
print("\n--- Завдання 2: Калькулятор (if-else) ---")
num1_if = float(input("Enter first number: "))
num2_if = float(input("Enter second number: "))
op_if = input("Enter operator (+, -, *, /): ")

if op_if == '+':
    print("Result:", add(num1_if, num2_if))
elif op_if == '-':
    print("Result:", subtract(num1_if, num2_if))
elif op_if == '*':
    print("Result:", multiply(num1_if, num2_if))
elif op_if == '/':
    print("Result:", divide(num1_if, num2_if))
else:
    print("Invalid operator")


# --- Завдання 3 ---
print("\n--- Завдання 3: Калькулятор (match-case) ---")
num1_match = float(input("Enter first number: "))
num2_match = float(input("Enter second number: "))
op_match = input("Enter operator (+, -, *, /): ")

match op_match:
    case '+':
        print("Result:", add(num1_match, num2_match))
    case '-':
        print("Result:", subtract(num1_match, num2_match))
    case '*':
        print("Result:", multiply(num1_match, num2_match))
    case '/':
        print("Result:", divide(num1_match, num2_match))
    case _:
        print("Invalid operator")

print("\nРобота програми завершена.")