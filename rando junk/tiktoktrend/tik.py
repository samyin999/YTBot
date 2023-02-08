import http.client

conn = http.client.HTTPSConnection("tiktok-trending-data.p.rapidapi.com")

headers = {
    'X-RapidAPI-Key': "f4e78f2d5emshd0942916265cb2cp1474ccjsne654d24f0d80",
    'X-RapidAPI-Host': "tiktok-trending-data.p.rapidapi.com"
    }

conn.request("GET", "/t", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))