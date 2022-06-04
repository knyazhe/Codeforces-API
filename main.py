import requests


# 1. replace можно дёргать заранее, разделение через ',' останется:
# logins = input("Enter a comma-separated logins: ").replace(" ", "").split(',')
#
# 2. Ты не обрабатываешь невалидные логины и отсутствие ввода.
#
# 3. Либу requests пропишу в requirements.txt. Чтобы подтянуть либы оттуда,
#    нужно будет дёрнуть pip. Но это уже будут не твои проблемы:
#    pip install -r requirements.txt
#

def cfreq(argument):
    return requests.get(f"https://codeforces.com/api/{argument}").json()


logins = input("Logins: ").replace(" ", "").split(',')
for login in logins:
    response = cfreq(f"user.status?handle={login}")
    print(login, end=" : ")
    if response['status'] != "OK":
        print('Error')
    else:
        count = 0
        for i in response['result']:
            if i['verdict'] == "OK":
                count += 1
        print(count)
