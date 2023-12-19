def calculate(first_num: int, second_num: int, operator: str) -> int | float:  
    match operator:
        case '+':
            result = first_num + second_num
        case '-':
            result = first_num - second_num
        case '*':
            result = first_num * second_num
        case '/':
            if second_num != 0:
                result = first_num / second_num
            else:
                raise ArithmeticError("Нельзя делить на 0!")
        case _:
            raise ValueError("Ошибка! Не известный оператор!")
    return result



def calculate_discount(purchase_amount: float, discount_amount: int) -> float:
    if discount_amount < 0:
        raise ArithmeticError("Скидка не может быть меньше нуля!")
    elif discount_amount > 100:
        raise ArithmeticError("Скидка не может быть больше 100!")
    return purchase_amount - (purchase_amount * discount_amount) / 100



if __name__ == "__main__":
    print(calculate(10, 25, '-'))
    print(calculate(20, 10, '*'))
    print(calculate(30, 10, '/'))
    print(calculate_discount(2150, 70))
    print(calculate_discount(4000, 20))