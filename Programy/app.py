from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage/index.html")

@app.route("/exercises")
def exercises():
    return render_template("exercises/index.html")

@app.route("/exercises/ip")
def ip():
    return render_template("ip/index.html")

@app.route("/calculator")
def calculator():
    return render_template("calculator/index.html")

@app.route("/calculator/result", methods = ['POST', 'GET'])
def result():
    

    #function defining a network address and the first host
    def networkAddress(networkMask, octet1, octet2, octet3, octet4, firstHost):
    
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
        #octetNetwork4 = str(int(octetNetwork4) + firstHost)
        firstHost = str(octetNetwork1) + "." + str(octetNetwork2) + "." + str(octetNetwork3) + "." + str(int(octetNetwork4) + 1)

        return networkAddr, firstHost

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

        lastHost = str(octetBroadcast1) + "." + str(octetBroadcast2) + "." + str(octetBroadcast3) + "." + str(int(octetBroadcast4) - 1)
        broadcast = str(octetBroadcast1) + "." + str(octetBroadcast2) + "." + str(octetBroadcast3) + "." + str(octetBroadcast4)

        return lastHost, broadcast

    #function defining a class of given IP address.
    def typeOfClass(octet1, octet2):

        if octet1 >= 1 and octet1 <= 127:
            addressClass = "A"
        elif octet1 >= 128 and octet1 <= 191 and octet2 <= 255:
            addressClass = "B"
        elif octet1 >= 192 and octet1 <= 223:
            addressClass = "C"
        elif octet1 >= 224 and octet1 <= 239:
            addressClass = "D"
        else:
            addressClass = "E"

        return addressClass
        

    def typeOfAddress(octet1, octet2):

        if octet1 == 10:
            addressType = "Private"
        elif octet1 == 172 and octet2 <= 31 and octet2 >= 16:
            addressType = "Private"
        elif octet1 == 192 and octet2 == 168:
            addressType = "Private"
        elif octet1 == 169 and octet2 == 254:
            addressType = "Private (APIPA)"
        elif octet1 == 127:
            addressType = "Private (Loopback)"
        else:
            addressType = "Public"

        return addressType

    #END OF FUNCTIONS SECTION

    output = request.form.to_dict()

    if output != None:
        ip_address = output["ip"]
        mask = int(output["mask"])
    
    
    octets = ip_address.split(".")

    try:
        octet1 = int(octets[0])
        octet2 = int(octets[1])
        octet3 = int(octets[2])
        octet4 = int(octets[3])
    except ValueError:
        exitStatement = "Invalid input"

    if octet1 > 255 or octet2 > 255 or octet3 > 255 or octet4 > 255:
        exitStatement = "IP address can not contain numbers higher than 255."
    elif octet1 < 0 or octet2 < 0 or octet3 < 0 or octet4 < 0:
        exitStatement = "IP address can not contain negative numbers."
    elif octet1 <= 0:
        exitStatement = "IP address must start with 0 or higher number from interval <1-255>"
        

    match mask:
        case 1:
            networkAddr, firstHost = networkAddress("128.0.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("127.255.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 2:
            networkAddr, firstHost = networkAddress("192.0.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("63.255.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 3:
            networkAddr, firstHost = networkAddress("224.0.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("31.255.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 4:
            networkAddr, firstHost = networkAddress("240.0.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("15.255.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 5:
            networkAddr, firstHost = networkAddress("248.0.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("7.255.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 6:
            networkAddr, firstHost = networkAddress("252.0.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("3.255.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 7:
            networkAddr, firstHost = networkAddress("254.0.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("1.255.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 8:
            networkAddr, firstHost = networkAddress("255.0.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.255.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 9:
            networkAddr, firstHost = networkAddress("255.128.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.127.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 10:
            networkAddr, firstHost = networkAddress("255.192.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.63.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 11:
            networkAddr, firstHost = networkAddress("255.224.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.31.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 12:
            networkAddr, firstHost = networkAddress("255.240.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.15.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 13:
            networkAddr, firstHost = networkAddress("255.248.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.7.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 14:
            networkAddr, firstHost = networkAddress("255.252.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.3.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 15:
            networkAddr, firstHost = networkAddress("255.254.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.1.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 16:
            networkAddr, firstHost = networkAddress("255.255.0.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.255.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 17:
            networkAddr, firstHost = networkAddress("255.255.128.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.127.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 18:
            networkAddr, firstHost = networkAddress("255.255.192.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.63.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 19:
            networkAddr, firstHost = networkAddress("255.255.224.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.31.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 20:
            networkAddr, firstHost = networkAddress("255.255.240.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.15.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 21:
            networkAddr, firstHost = networkAddress("255.255.248.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.7.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 22:
            networkAddr, firstHost = networkAddress("255.255.252.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.3.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 23:
            networkAddr, firstHost = networkAddress("255.255.254.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.1.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 24:
            
            networkAddr, firstHost = networkAddress("255.255.255.0", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.0.255", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 25:
            networkAddr, firstHost = networkAddress("255.255.255.128", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.0.127", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 26:
            networkAddr, firstHost = networkAddress("255.255.255.192", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.0.63", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 27:
            networkAddr, firstHost = networkAddress("255.255.255.224", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.0.31", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 28:
            networkAddr, firstHost = networkAddress("255.255.255.240", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.0.15", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 29:
            networkAddr, firstHost = networkAddress("255.255.255.248", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.0.7", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 30:
            networkAddr, firstHost = networkAddress("255.255.255.252", octet1, octet2, octet3, octet4, 1)
            lastHost, broadAddr = broadcastAddress("0.0.0.3", octet1, octet2, octet3, octet4, 1)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
            
        case 31:
            networkAddr, firstHost = networkAddress("255.255.255.254", octet1, octet2, octet3, octet4, 0)
            lastHost, broadAddr = broadcastAddress("0.0.0.1", octet1, octet2, octet3, octet4, 0)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
        case 32:
            networkAddr, firstHost = networkAddress("255.255.255.255", octet1, octet2, octet3, octet4, 0)
            lastHost, broadAddr = broadcastAddress("0.0.0.0", octet1, octet2, octet3, octet4, 0)
            addressClass = typeOfClass(octet1, octet2)
            addressType = typeOfAddress(octet1, octet2)
        case _:
            exitStatement = "Please, enter the mask as a number in decimal form from interval <1-32>."
    
    

    return render_template("result/index.html", fHost = firstHost, nAddr = networkAddr, bAddr = broadAddr, lHost = lastHost, aType = addressType, aClass = addressClass)

if __name__ == "_main":
    app.run(host='0.0.0.0', debug=True)
