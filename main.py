import requests


#    pip install -r requirements.txt

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
