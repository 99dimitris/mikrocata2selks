import requests
import os

ADDRESS_FILE = '/tmp/old_ip_address.txt'

def detect_ip_change():
    blnDelta = False
    currIp = requests.get('https://api.ipify.org').text

    if not os.path.isfile(ADDRESS_FILE):
        # trigger the script to send email for the first time
        persist_ip('127.0.0.1')

    oldIp = read_old_ip()

    if currIp != oldIp:
        blnDelta = True

    persist_ip(currIp)
    return (blnDelta, currIp)
# [detect_ip_change ends]


def persist_ip(ip):
    f = open(ADDRESS_FILE, 'w')
    f.write(ip)
    f.close()
# [persist_ip ends]


def read_old_ip():
    f = open(ADDRESS_FILE, 'r')
    oldIp = f.read()
    f.close()
    return oldIp
# [read_old_ip ends]


# [START main]
def main():
    deltaTuple = detect_ip_change()
    if deltaTuple[0] is True:
        print("WAN IP changed to " + deltaTuple[1])
    else:
        print ("No news is good news.")
# [END main]


if __name__ == '__main__':
    main()
