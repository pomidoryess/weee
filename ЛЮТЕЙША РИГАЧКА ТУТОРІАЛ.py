result = []

def divider(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("не той тип даних")
        if a < b:
            raise ValueError("a повинно бути більше або рівне b")
        if b > 100:
            raise IndexError("b не може бути більше 100 лмао")
        return a / b
    except Exception as e:
        print(f"помілка: {e}")
        return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key, value in data.items():
    try:
        res = divider(key, value)
        if res is not None:
            result.append(res)
    except Exception as e:
        print(f"помилка обробки {key}: {e}")
print(result)