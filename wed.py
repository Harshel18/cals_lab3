import requests
import json

url ="https://michaelgathara.com/api/python-challenge"

response = requests.get(url)
challenges = response.json()
print(challenges)
print("Name : Harshel Srivatsava Alahari")
print("Blazerid : Halahari")
i=0
for i in challenges:
      outputResult = i["problem"]
      outputResult = outputResult.replace("?","")
      print("Problem : " + outputResult)
      outputResult = eval(outputResult)
      print("Output:" + str(outputResult))