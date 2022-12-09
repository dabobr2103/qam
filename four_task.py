users_names = ["Alfa", "Beta", "Vita", "Delta", "Gamma", "Farsi"]
#print(users_names[2:5])
#print(users_names)
ages_for_users = [1, 2, 3, 5, 12, 77]

# for idx_user in range(len(users_names)):
#     print(users_names[idx_user], ages_for_users[idx_user])

age = input("your age is... ")
try:
    age = int(age)
except:
    age = 18
ages_for_users.append(age)
print(ages_for_users)
# поп з індексом видаляє індекс і повертає в змінну
last_input_age = ages_for_users.pop(0)
# поп БЕЗ індексу видаляє останній єл списку і повертає в змінну
last_input_age = ages_for_users.pop()
# ремув видаляє за значенням, 
ages_for_users.remove(2)
print(ages_for_users)
# тут буде помилка
try:
    last_input_age = ages_for_users.remove(0)
except ValueError:
    print("does not found, no need to removed")
