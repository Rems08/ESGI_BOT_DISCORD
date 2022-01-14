import requests


url_trombinoscope = "https://myges.fr/student/student-teacher-directory"
with requests.Session() as s:
    url_login = "https://ges-cas.kordis.fr/login?service=https%3A%2F%2Fmyges.fr%2Fj_spring_cas_security_check"
    user = ""
    password = ""
    s.get(url_login)
    login_data = {
        'username': user,
        'password': password,
        'lt': "LT-468165-iGc1ermfYosr5VfbINbFDREjIJavEx-cas",
        'execution': 'e2s1',
        '_eventId': 'submit',
        'submit': 'CONNEXION'
    }
    s.post(url_login, data=login_data)
    r = s.get(url_trombinoscope)
    print(r.text)