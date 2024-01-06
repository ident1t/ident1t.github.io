#function defining a network address and the first host
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

    print()
    print("Network address: " + str(octetNetwork1) + "." + str(octetNetwork2) + "." + str(octetNetwork3) + "." + str(octetNetwork4))
    octetNetwork4 = str(int(octetNetwork4) + firstHost)
    print("The first host address: " + str(octetNetwork1) + "." + str(octetNetwork2) + "." + str(octetNetwork3) + "." + str(octetNetwork4))

#function defining a broadcast address and the last host
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

    print("The last host address: " + str(octetBroadcast1) + "." + str(octetBroadcast2) + "." + str(octetBroadcast3) + "." + str(int(octetBroadcast4) - lastHost))
    print("Broadcast address: " + str(octetBroadcast1) + "." + str(octetBroadcast2) + "." + str(octetBroadcast3) + "." + str(octetBroadcast4))

#function defining a class of given IP address.
def typeOfClass(octet1, octet2):

    if octet1 >= 1 and octet1 <= 127:
        print("Class: A")
    elif octet1 >= 128 and octet1 <= 191 and octet2 <= 255:
        print("Class: B")
    elif octet1 >= 192 and octet1 <= 223:
        print("Class: C")
    elif octet1 >= 224 and octet1 <= 239:
        print("Class: D")
    else:
        print("Class: E")
    

def typeOfAddress(octet1, octet2):

    if octet1 == 10:
        print("Address type: Private")
    elif octet1 == 172 and octet2 <= 31 and octet2 >= 16:
        print("Address type: Private")
    elif octet1 == 192 and octet2 == 168:
        print("Address type: Private")
    elif octet1 == 169 and octet2 == 254:
        print("Address type: Private (APIPA)")
    elif octet1 == 127:
        print("Address type: Private (Loopback)")
    else:
        print("Address type: public")


print("Please, insert input in this format: X.X.X.X/Y")
print("X - Octet entered in decimal form.")
print("Y - Network mask in decimal form from the interval <1-32>.")
print("----------------------------------------------------------")
print()

mainInput = input()

mainInputList = []

if mainInput != None:
    mainInputList = mainInput.split("/")

networkMask = 0

try:
    if len(mainInputList) >= 2:
        networkMask = int(mainInputList[1])
except ValueError:
    exit("Invalid input")

inputOfIpAddress = mainInputList[0]

octets = []
octets = inputOfIpAddress.split(".")

try:
    octet1 = int(octets[0])
    octet2 = int(octets[1])
    octet3 = int(octets[2])
    octet4 = int(octets[3])
except ValueError:
    exit("Invalid input")

if octet1 > 255 or octet2 > 255 or octet3 > 255 or octet4 > 255:
    exit("IP address can not contain numbers higher than 255.")
elif octet1 < 0 or octet2 < 0 or octet3 < 0 or octet4 < 0:
    exit("IP address can not contain negative numbers.")
elif octet1 <= 0:
    exit("IP address must start with 0 or higher number from interval <1-255>")
else:
    print()
    

match networkMask:
    case 1:
        networkAddress("128.0.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("127.255.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 2:
        networkAddress("192.0.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("63.255.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 3:
        networkAddress("224.0.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("31.255.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 4:
        networkAddress("240.0.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("15.255.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 5:
        networkAddress("248.0.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("7.255.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 6:
        networkAddress("252.0.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("3.255.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 7:
        networkAddress("254.0.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("1.255.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 8:
        networkAddress("255.0.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.255.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 9:
        networkAddress("255.128.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.127.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 10:
        networkAddress("255.192.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.63.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 11:
        networkAddress("255.224.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.31.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 12:
        networkAddress("255.240.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.15.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 13:
        networkAddress("255.248.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.7.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 14:
        networkAddress("255.252.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.3.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 15:
        networkAddress("255.254.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.1.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 16:
        networkAddress("255.255.0.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.255.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 17:
        networkAddress("255.255.128.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.127.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 18:
        networkAddress("255.255.192.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.63.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 19:
        networkAddress("255.255.224.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.31.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 20:
        networkAddress("255.255.240.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.15.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 21:
        networkAddress("255.255.248.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.7.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 22:
        networkAddress("255.255.252.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.3.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 23:
        networkAddress("255.255.254.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.1.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 24:
        
        networkAddress("255.255.255.0", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.0.255", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 25:
        networkAddress("255.255.255.128", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.0.127", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 26:
        networkAddress("255.255.255.192", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.0.63", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 27:
        networkAddress("255.255.255.224", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.0.31", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 28:
        networkAddress("255.255.255.240", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.0.15", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 29:
        networkAddress("255.255.255.248", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.0.7", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 30:
        networkAddress("255.255.255.252", octet1, octet2, octet3, octet4, 1)
        broadcastAddress("0.0.0.3", octet1, octet2, octet3, octet4, 1)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
        
    case 31:
        networkAddress("255.255.255.254", octet1, octet2, octet3, octet4, 0)
        broadcastAddress("0.0.0.1", octet1, octet2, octet3, octet4, 0)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
    case 32:
        networkAddress("255.255.255.255", octet1, octet2, octet3, octet4, 0)
        broadcastAddress("0.0.0.0", octet1, octet2, octet3, octet4, 0)
        typeOfClass(octet1, octet2)
        typeOfAddress(octet1, octet2)
    case _:
        print("Please, enter the mask as a number in decimal form from interval <1-32>.")
        