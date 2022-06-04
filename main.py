import requests


def cfreq(argument):
    return requests.get(f"https://codeforces.com/api/{argument}").json()


logins = input("Логины через запятую: ").split(',')
for login in logins:
    login = login.replace(" ", "")
    response = cfreq(f"user.status?handle={login}")
    print(login, end=" : ")
    count = 0
    for i in response['result']:
        if i['verdict'] == "OK":
            count += 1
    print(count)