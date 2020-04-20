import csv
import urllib.request
import time
import multiprocessing

with open('/opt/splunk/etc/apps/Kaspersky_Threat_Feed_App_for_Splunk/lookups/IP_Reputation_Data_Feed.csv') as csvfile:
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

    def do_something():
        length = round(listLength/10)
        for x in range(0*length, length*1):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url,timeout=5)
                print(wp)
            except:
                print("Somthing is not correct.")

    def do_somethingA():
        length = round(listLength/10)
        print(length)
        for x in range(int(length)*1, int(length)*2):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url,timeout=5)
                print(wp)
            except:
                print("Somthing is not correct A.")

    def do_somethingB():
        length = round(listLength/10)
        for x in range(length*2, length*3):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url, timeout=5)
                print(wp)
            except:
                print("Somthing is not correct B.")
   
    def do_somethingC():
        length = round(listLength/10)
        for x in range(length*3, length*4):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url, timeout=5)
                print(wp)
            except:
                print("Somthing is not correct C.")

    def do_somethingD():
        length = round(listLength/10)
        for x in range(length*4, length*5):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url, timeout=5)
                print(wp)
            except:
                print("Somthing is not correct D.")

    def do_somethingE():
        length = round(listLength/10)
        for x in range(length*5, length*6):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url, timeout=5)
                print(wp)
            except:
                print("Somthing is not correct E.")

    def do_somethingF():
        length = round(listLength/10)
        for x in range(length*6, length*7):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url, timeout=5)
                print(wp)
            except:
                print("Somthing is not correct F.")

    def do_somethingG():
        length = round(listLength/10)
        for x in range(length*7, length*8):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url, timeout=5)
                print(wp)
            except:
                print("Somthing is not correct G.")

    def do_somethingH():
        length = round(listLength/10)
        for x in range(length*8, length*9):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url, timeout=5)
                print(wp)
            except:
                print("Somthing is not correct H.")

    def do_somethingI():
        length = round(listLength/10)
        for x in range(length*9, length*10):
            try:
                print(ipList[x])
                time.sleep(0.1)
                print(x)
                url = ipList[x]
                wp = urllib.request.urlopen(url, timeout=5)
                print(wp)
            except:
                print("Somthing is not correct I.")

    p1 = multiprocessing.Process(target=do_something)
    p2 = multiprocessing.Process(target=do_somethingA)
    p3 = multiprocessing.Process(target=do_somethingB)
    p4 = multiprocessing.Process(target=do_somethingC)
    p5 = multiprocessing.Process(target=do_somethingD)
    p6 = multiprocessing.Process(target=do_somethingE)
    p7 = multiprocessing.Process(target=do_somethingF)
    p8 = multiprocessing.Process(target=do_somethingG)
    p9 = multiprocessing.Process(target=do_somethingH)
    p10 = multiprocessing.Process(target=do_somethingI)

    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()   


    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
