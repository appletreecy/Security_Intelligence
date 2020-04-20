import csv
import urllib.request
import time
import multiprocessing
import concurrent.futures

with open('/opt/splunk/etc/apps/Kaspersky_Threat_Feed_App_for_Splunk/lookups/Botnet_CnC_URL_Exact_Data_Feed_DOMAIN.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    ipList = ["apple", "banana"]
    for row in readCSV:
        print(row[0])
        try:
            url = "http://" + row[0]
            print(url)
            urlA = row[0]
            ipList.append(url)
            #print(ipList)
            #wp = urllib.request.urlopen(url)
            #print(wp)
        except:
            print("Something else went wrong!")
    print(ipList)
    listLength = len(ipList)
    print(listLength)
    print(ipList[100])
    print(round(listLength/10))

#    for y in range(0, 11):
#        for x in range(0*y, 136*y):
#            print(x)
#            print(ipList[x])

    start = time.perf_counter()

    def do_something(num1):
        length = round(listLength/10)
        for x in range(num1*length, length*(num1+1)):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url,timeout=5)
                print(wp)
            except:
                print("Somthing is not correct.")
    numList=[0,1,2,3,4,5,6,7,8,9]  

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(do_something, numList)

    

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
