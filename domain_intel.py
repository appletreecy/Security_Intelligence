import csv
import urllib.request

with open('/opt/splunk/etc/apps/Kaspersky_Threat_Feed_App_for_Splunk/lookups/Botnet_CnC_URL_Exact_Data_Feed_DOMAIN.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row[0])
        try:
            url = "http://" + row[0]
            print(url)
            wp = urllib.request.urlopen(url)
            print(wp)
        except:
            print("Something else went wrong!")
