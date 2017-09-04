import urllib.request
import time
import hashlib
from multiprocessing import Pool, Process, Array, Queue

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
    #print(url)
    return urllib.request.urlopen(url).read()

def encode_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# start = time.perf_counter()
# for i in range(50, 21, -1):
#     print(urllib.request.urlopen("http://localhost:8000/deanOffice/reserveNumber/{}/".format(i)).read())
# end = time.perf_counter()

#print(end - start)

# print(get_actual_number('deanOffice'))



# print(check_login(1, encode_password('password')))
# print(check_login(1, encode_password('password1')))

# print(get_available_number('deanOffice'))
# print(reserve_number('deanOffice', 2, encode_password('password1')))
# print(get_available_number('deanOffice'))
# print(reserve_number('deanOffice', 2, encode_password('password')))
# print(get_available_number('deanOffice'))

def actualNumberAndAvaiableNumber_test(timeQueue, noRequest):
    start = time.perf_counter()
    for i in range(noRequest):
        actualNo = get_actual_number('deanOffice')
        availableNo = get_available_number('deanOffice')
    end = time.perf_counter()
    timeQueue.put(end-start)

def availableNumber_test(timeQueue, noRequest):
    start = time.perf_counter()
    for i in range(noRequest):
        try:
            availableNo = get_available_number('deanOffice')
        except ValueError:
            pass
    end = time.perf_counter()
    timeQueue.put(end-start)

def checkLogin_test(timeQueue, noRequest):
    start = time.perf_counter()
    for i in range(noRequest):
        try:
            check_login(2, encode_password('password'))
        except ValueError:
            pass
    end = time.perf_counter()
    timeQueue.put(end-start)

def reserveNumber_test(timeQueue, noRequest):
    start = time.perf_counter()
    for i in range(noRequest):
        try:
            reserve_number('deanOffice', 5, encode_password('password'))
        except ValueError:
            pass
    end = time.perf_counter()
    timeQueue.put(end-start)

def calculateStatsFromQueue(timeQueue, noClients, noRequest):
    timeSum = 0
    maxTime = 0
    #print('------------------')
    while not timeQueue.empty():
        singleTime = timeQueue.get();
        #print(singleTime)
        timeSum += singleTime
        if(maxTime < singleTime):
            maxTime = singleTime
    average = timeSum / noClients;
    #print('NC={}, NR={}, AVG={}, MAX={}'.format(noClients, noRequest, average, maxTime))
    print('{}, {}, {}, {}'.format(noClients, noRequest, average, maxTime))
    #print('------------------')
    return timeSum

def performance_test(noClients, specificTestMethod, noRequest):
    timeQueue = Queue()
    workers = [Process(target=specificTestMethod, args = (timeQueue, noRequest)) for i in range(noClients)]
    for p in workers:
        p.start()
    for p in workers:
        p.join()
    calculateStatsFromQueue(timeQueue, noClients, noRequest)


requestNoSeq = [1, 5, 20, 50, 100]
clientNoSeq = [1, 5, 20, 50, 100]

print("reserveNumber_test-----------------------------")
for clientNo in clientNoSeq:
    for requestNo in requestNoSeq:
        performance_test(clientNo, reserveNumber_test, requestNo)

print("checkLogin_test-----------------------------")
for clientNo in clientNoSeq:
    for requestNo in requestNoSeq:
        performance_test(clientNo, checkLogin_test, requestNo)
        
print("availableNumber_test-----------------------------")
for clientNo in clientNoSeq:
    for requestNo in requestNoSeq:
        performance_test(clientNo, availableNumber_test, requestNo)














# def get_actual_number_by_one_client1(noRequest):
#     #print(noRequest)
#     start = time.perf_counter()
#     for i in range(noRequest):
#         actualNo = get_actual_number('deanOffice')
#         availableNo = get_available_number('deanOffice')
#         #print('{}-{}-{}'.format(noClient, actualNo, availableNo))
#     end = time.perf_counter()
#     print('a{}'.format(end-start))

# def do_nothing(test):
#     pass

# def cost_of_creating_threads(noClients):
#     pool = Pool(noClients)
#     start = time.perf_counter()
#     results = pool.map(do_nothing, range(noClients))
#     pool.close()
#     pool.join()
#     end = time.perf_counter()
#     return (end - start)


# def performance_test__requestForActualAndAvailableNumer1(noClients, noRequest):
#     cost_of_threads = cost_of_creating_threads(noClients);
#     pool = Pool(noRequest)
#     start = time.perf_counter()
#     results = pool.map(get_actual_number_by_one_client1, [noRequest] * noClients)
#     pool.close()
#     pool.join()
#     end = time.perf_counter()
#     print('b{}'.format(end-start))
#     print('bx{}'.format(end-start-cost_of_threads))