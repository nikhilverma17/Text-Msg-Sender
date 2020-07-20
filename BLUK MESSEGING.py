import requests

url = "https://www.fast2sms.com/dev/bulk"

payload = "sender_id=FSTSMS&message=This%20is%20a%20test%20message&language=english&route=p&numbers="
headers = {
'authorization': "9Nnqc7MSEbo6IwZtDaWipzgB84Qx2RTrukJlmhL5fUCVPAeOs0lNPrdpnFu6ZbAyOsJMkXxUCeHfmcKD",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
