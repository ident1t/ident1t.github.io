import random

octet1 = random.randrange(0, 255)
octet2 = random.randrange(0, 255)
octet3 = random.randrange(0, 255)
octet4 = random.randrange(0, 255)
prefix = random.randrange(1, 32)

print(str(octet1) + "." + str(octet2) + "." + str(octet3) + "." + str(octet4) + "/" + str(prefix))

#function calculating a network address and a first host
def networkAddress(networkMask, octet1, octet2, octet3, octet4, firstHost: int):

    octetsMask = networkMask.split(".")

    octetOfMask1 = int(octetsMask[0])
    octetOfMask2 = int(octetsMask[1])
    octetOfMask3 = int(octetsMask[2])
    octetOfMask4 = int(octetsMask[3])

    octetNetwork1 = str(octetOfMask1 & octet1)
    octetNetwork2 = str(octetOfMask2 & octet2)
    octetNetwork3 = str(octetOfMask3 & octet3)
    octetNetwork4 = str(octetOfMask4 & octet4)

    
    networkAddr = str(octetNetwork1) + "." + str(octetNetwork2) + "." + str(octetNetwork3) + "." + str(octetNetwork4)
    octetNetwork4 = str(int(octetNetwork4) + firstHost)
    firstHost = str(octetNetwork1) + "." + str(octetNetwork2) + "." + str(octetNetwork3) + "." + str(octetNetwork4)
    

    return networkAddr, firstHost

#function calculating a broadcast address and the last host
def broadcastAddress(networkMask, octet1, octet2, octet3, octet4, lastHost):

    octetsMask = networkMask.split(".")

    octetOfMask1 = int(octetsMask[0])
    octetOfMask2 = int(octetsMask[1])
    octetOfMask3 = int(octetsMask[2])
    octetOfMask4 = int(octetsMask[3])

    octetBroadcast1 = str(octetOfMask1 | octet1)
    octetBroadcast2 = str(octetOfMask2 | octet2)
    octetBroadcast3 = str(octetOfMask3 | octet3)
    octetBroadcast4 = str(octetOfMask4 | octet4)
    
    lastHost = str(octetBroadcast1) + "." + str(octetBroadcast2) + "." + str(octetBroadcast3) + "." + str(int(octetBroadcast4) - lastHost)
    broadAddr = str(octetBroadcast1) + "." + str(octetBroadcast2) + "." + str(octetBroadcast3) + "." + str(octetBroadcast4)

    return lastHost, broadAddr
    

match prefix:
    case 1:
        networkAdder, firstHost = networkAddress("128.0.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("127.255.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 2:
        networkAdder, firstHost = networkAddress("192.0.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("63.255.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 3:
        networkAdder, firstHost = networkAddress("224.0.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("31.255.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 4:
        networkAdder, firstHost = networkAddress("240.0.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("15.255.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 5:
        networkAdder, firstHost = networkAddress("248.0.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("7.255.255.255", octet1, octet2, octet3, octet4, 1)
    
    case 6:
        networkAdder, firstHost = networkAddress("252.0.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("3.255.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 7:
        networkAdder, firstHost = networkAddress("254.0.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("1.255.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 8:
        networkAdder, firstHost = networkAddress("255.0.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.255.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 9:
        networkAdder, firstHost = networkAddress("255.128.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.127.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 10:
        networkAdder, firstHost = networkAddress("255.192.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.63.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 11:
        networkAdder, firstHost = networkAddress("255.224.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.31.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 12:
        networkAdder, firstHost = networkAddress("255.240.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.15.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 13:
        networkAdder, firstHost = networkAddress("255.248.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.7.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 14:
        networkAdder, firstHost = networkAddress("255.252.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.3.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 15:
        networkAdder, firstHost = networkAddress("255.254.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.1.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 16:
        networkAdder, firstHost = networkAddress("255.255.0.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.255.255", octet1, octet2, octet3, octet4, 1)
        
    case 17:
        networkAdder, firstHost = networkAddress("255.255.128.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.127.255", octet1, octet2, octet3, octet4, 1)
        
    case 18:
        networkAdder, firstHost = networkAddress("255.255.192.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.63.255", octet1, octet2, octet3, octet4, 1)
        
    case 19:
        networkAdder, firstHost = networkAddress("255.255.224.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.31.255", octet1, octet2, octet3, octet4, 1)
        
    case 20:
        networkAdder, firstHost = networkAddress("255.255.240.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.15.255", octet1, octet2, octet3, octet4, 1)
        
    case 21:
        networkAdder, firstHost = networkAddress("255.255.248.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.7.255", octet1, octet2, octet3, octet4, 1)
    
    case 22:
        networkAdder, firstHost = networkAddress("255.255.252.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.3.255", octet1, octet2, octet3, octet4, 1)
        
    case 23:
        networkAdder, firstHost = networkAddress("255.255.254.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.1.255", octet1, octet2, octet3, octet4, 1)
        
    case 24:
        networkAdder, firstHost = networkAddress("255.255.255.0", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.0.255", octet1, octet2, octet3, octet4, 1)
        
    case 25:
        networkAdder, firstHost = networkAddress("255.255.255.128", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.0.127", octet1, octet2, octet3, octet4, 1)
        
    case 26:
        networkAdder, firstHost = networkAddress("255.255.255.192", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.0.63", octet1, octet2, octet3, octet4, 1)
        
    case 27:
        networkAdder, firstHost = networkAddress("255.255.255.224", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.0.31", octet1, octet2, octet3, octet4, 1)
        
    case 28:
        networkAdder, firstHost = networkAddress("255.255.255.240", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.0.15", octet1, octet2, octet3, octet4, 1)
        
    case 29:
        networkAdder, firstHost = networkAddress("255.255.255.248", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.0.7", octet1, octet2, octet3, octet4, 1)
        
    case 30:
        networkAdder, firstHost = networkAddress("255.255.255.252", octet1, octet2, octet3, octet4, 1)
        lastHost, broadAddr = broadcastAddress("0.0.0.3", octet1, octet2, octet3, octet4, 1)
        
    case 31:
        networkAdder, firstHost = networkAddress("255.255.255.254", octet1, octet2, octet3, octet4, 0)
        lastHost, broadAddr = broadcastAddress("0.0.0.1", octet1, octet2, octet3, octet4, 0)
    
    case 32:
        networkAdder, firstHost = networkAddress("255.255.255.255", octet1, octet2, octet3, octet4, 0)
        lastHost, broadAddr = broadcastAddress("0.0.0.0", octet1, octet2, octet3, octet4, 0) 


userNet = input()
userFirst = input()
userLast = input()
userBroad = input()

if userNet == networkAdder:
    print("True")
else:
    print("False")

if userFirst == firstHost:
    print("True")
else:
    print("False")

if userLast == lastHost:
    print("True")
else:
    print("False")

if userBroad == broadAddr:
    print("True")
else:
    print("False")
