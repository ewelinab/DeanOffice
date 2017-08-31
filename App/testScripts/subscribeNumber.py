import urllib.request
import time

start = time.perf_counter()
for i in range(320, 21, -1):
    print(urllib.request.urlopen("http://localhost:8000/deanOffice/reserveNumber/{}/".format(i)).read())
end = time.perf_counter()

print(end - start)