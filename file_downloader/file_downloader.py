import request

url = "https://assets.tryhackme.com/img/THMlogo.png"
r = request.get(url, allow_redirects = True)
open('THMlogo.png', 'wb').write(r.content)