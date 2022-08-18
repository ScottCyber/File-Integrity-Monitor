import hashlib
import datetime

#What file do you want to monitor? Note: The file has to be on a drive that does not have strict file access permissions.

filelocation = input("What file do you want to monitor for activity? \n (include the whole file path in your selection): ")

#Hashing Function that creates the baseline

def gethash(filelocation):
    md5 = hashlib.md5()
    with open(filelocation,'rb') as file:
        hash = file.read()
        md5.update(hash)
        return md5.hexdigest()

baseline = gethash(filelocation)
print('\nThe file is currently being monitored for activity!')


#Loop of comparing the hash to the collected baseline


def Monitoringhash(filelocation):
    md5 = hashlib.md5()
    with open(filelocation,'rb') as file:
        LoopHash = file.read()
        md5.update(LoopHash)
        return md5.hexdigest()

while True:
    MonitoringLoop = Monitoringhash(filelocation)
    if MonitoringLoop != baseline:
        print(f'\nThe file at: {filelocation}, has been modified at {str(datetime.datetime.now())} ')
        choice = input(f'\nWould you like to keep monitoring with an updated baseline? (y , n)   ')
        if choice == 'y':
            gethash(filelocation)
            baseline = gethash(filelocation)
            Monitoringhash(filelocation)
            print('\nMonitoring of the selected file has resumed.')
        else:
            break
