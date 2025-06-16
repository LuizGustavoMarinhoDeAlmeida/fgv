def divisao(a: float, b:float) -> float:
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

if __name__ == "__main__":
	print("5 / 2 = ", divisao(5, 2))