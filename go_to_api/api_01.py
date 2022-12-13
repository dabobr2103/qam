import requests
server = "https://qauto.forstudy.space/api"
endpoint = "/auth/signin"
# сервер та ендпоінт задають урл який ми тестимо
# далі данні що ми шлемо методом пост
example_value = {
  "email": "test@test.com",
  "password": "Qwerty12345",
  "remember": False
}
# викликаємо метод пост і json= вказує що ми шлем як ДЖСОН
r = requests.post(server+endpoint, json=example_value)
# сервер присилає нм теж ДЖСОН що ми перетворюємол в словник і записуєм у зм. 
server_says = r.json()
# використовуємо методи словника
#  Якщо ключ "status" у словнику то
if "status" in server_says:
    #  Якщо значення клюса статус == ок
    if server_says["status"] == "ok":
        print("all ok")
    #  інакше
    else:
        print(server_says['message'])