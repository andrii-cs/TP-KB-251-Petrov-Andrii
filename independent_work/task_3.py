# ==========================================
# ЗАВДАННЯ 1: Калькулятор у циклі з виходом
# ==========================================
print("--- ЗАВДАННЯ 1: Калькулятор у циклі ---")

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

while True:
    cmd = input("Enter operator (+, -, *, /) or 'exit' to quit: ")
    if cmd.lower() == 'exit':
        print("Exiting calculator...\n")
        break

    if cmd not in ('+', '-', '*', '/'):
        print("Invalid operator")
        continue

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if cmd == '+':
        print("Result:", add(a, b))
    elif cmd == '-':
        print("Result:", subtract(a, b))
    elif cmd == '*':
        print("Result:", multiply(a, b))
    elif cmd == '/':
        print("Result:", divide(a, b))


# ==========================================
# ЗАВДАННЯ 2: Тестування методів списків
# ==========================================
print("--- ЗАВДАННЯ 2: Методи списків ---")
items = [1, 2, 3]
print("Initial:", items)

items.append(4)
print("append(4):", items)

items.extend([5, 6])
print("extend([5, 6]):", items)

items.insert(1, 99)
print("insert(1, 99):", items)

items.remove(99)
print("remove(99):", items)

items.sort()
print("sort():", items)

items.reverse()
print("reverse():", items)

copy_items = items.copy()
print("copy():", copy_items)

items.clear()
print("clear():", items)
print()


# ==========================================
# ЗАВДАННЯ 3: Тестування методів словників
# ==========================================
print("--- ЗАВДАННЯ 3: Методи словників ---")
data = {"a": 1, "b": 2, "c": 3}
print("Initial:", data)

data.update({"d": 4, "e": 5})
print("update:", data)

print("keys:", list(data.keys()))
print("values:", list(data.values()))
print("items:", list(data.items()))

del data["a"]
print("del data['a']:", data)

data.clear()
print("clear:", data)
print()


# ==========================================
# ЗАВДАННЯ 4: Пошук позиції для вставки елемента
# ==========================================
print("--- ЗАВДАННЯ 4: Пошук позиції для вставки ---")
def find_insert_position(sorted_list, val):
    for i in range(len(sorted_list)):
        if val <= sorted_list[i]:
            return i
    return len(sorted_list)

nums = [10, 20, 30, 40, 50]
val = 25
pos = find_insert_position(nums, val)

print("List:", nums)
print("Position to insert:", pos)
nums.insert(pos, val)
print("Updated list:", nums)