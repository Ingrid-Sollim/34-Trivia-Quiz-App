import requests
try:
    url = "https://opentdb.com/api.php"
    parameters = {"amount":10,"category":22,"type":"boolean"}
    response = requests.get(url=url,params=parameters)
    data = response.json()
    #print(data)
    question_data = data["results"]
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)

#print(question_data)



