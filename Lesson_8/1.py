import re


def email_parse(email):
    match = re.search(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu|ru]{2,3}$', email)
    username = ''.join(re.findall('^[a-zA-Z0-9_.+-]+', email))
    domain = ''.join(re.findall('[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.*[com|org|edu|ru]{2,3}$', email))
    if match:
        return {'username': username, 'domain': domain}
    else:
        return f'wrong email: {email}'


print(email_parse('someone@geekbrains.com'))
print(email_parse('someone@geekbrains.org'))
print(email_parse('someone@geekbrains.ru'))
print(email_parse('someonegeekbrains.org'))
print(email_parse('someonegeekbrainsru'))
