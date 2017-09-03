import urllib.request
import time
import hashlib

def check_login(login, password):
    return run_service('checkLogin/{}/{}'.format(login, password))

def get_actual_number(office):
    return run_service('{}/getActualNumber'.format(office))

def get_available_number(office):
    return run_service('{}/getAvailableNumber'.format(office))

def reserve_number(office, login, password):
    return run_service("{}/reserveNumber/{}/{}".format(office, login, password))

def reserve_number_without_password(office, login):
    return run_service("{}/reserveNumber/{}/".format(office, login))

def run_service(service_url):
     return send_http_request("http://localhost:8000/{}/".format(service_url))

def send_http_request(url):
    print(url)
    return urllib.request.urlopen(url).read()

def encode_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# start = time.perf_counter()
# for i in range(50, 21, -1):
#     print(urllib.request.urlopen("http://localhost:8000/deanOffice/reserveNumber/{}/".format(i)).read())
# end = time.perf_counter()

#print(end - start)

print(get_actual_number('deanOffice'))



print(check_login(1, encode_password('password')))
print(check_login(1, encode_password('password1')))

print(get_available_number('deanOffice'))
print(reserve_number('deanOffice', 2, encode_password('password1')))
print(get_available_number('deanOffice'))
print(reserve_number('deanOffice', 2, encode_password('password')))
print(get_available_number('deanOffice'))

