def safe_calc(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            return f"помилка кароче: {e}"
    return wrapper

@safe_calc
def calculate(expression):
    return eval(expression)

while True:
    expr = input("напши шось хзз: ")
    if expr.lower() == "вийди звідси ля лмао":
        break
    print(calculate(expr))