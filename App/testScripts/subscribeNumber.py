import urllib.request
import time

def get_actual_number(office):
    return run_service('{}/getActualNumber'.format(office));

def get_available_number(office):
    return run_service('{}/getAvailableNumber'.format(office));

def reserv_number(office, num):
    return run_service("{}/reserveNumber/{}/".format(office, num));

def run_service(service_url):
     return send_http_request("http://localhost:8000/{}/".format(service_url));

def send_http_request(url):
    return urllib.request.urlopen(url).read()

start = time.perf_counter()
for i in range(50, 21, -1):
    print(urllib.request.urlopen("http://localhost:8000/deanOffice/reserveNumber/{}/".format(i)).read())
end = time.perf_counter()

#print(end - start)

print(get_actual_number('deanOffice'))
print(get_available_number('deanOffice'))

