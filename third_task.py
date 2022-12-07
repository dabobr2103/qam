name_a = "jonny"
name_b = "bob"
age_a = 18
age_b = 13
name_c = "j"
name_d = "bob"
age_c = 8
age_d = 43

def age_calc(age_1: int, age_2: int):
    if age_1 > age_2:
        result = f"Вік більше {age_1}"
    else:
        result = f"Вік більше {age_2}"
    return result

def name_calc(name_1: str , name_2: str):
    if len(name_1) > len(name_2):
        result = "Ім'я довше у " + name_1
    else:
        result = "Ім'я довше у " + name_2
    return result


print(age_calc(age_a, age_b))
# print(age_calc(age_c, age_d))
# print(name_calc(name_a, name_b))
# print(name_calc(name_c, name_d))

print(age_calc(5, 7))
print(name_calc("", "234"))