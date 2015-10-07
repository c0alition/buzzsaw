def createNetworkMap():
    
    #local host
    localHostAddressD=netifaces.ifaddresses('en0')
    localHostDLookup=localHostAddressD[netifaces.AF_INET]
    localHostAddress=localHostDLookup[0]['addr']
    
    #all hosts on network
    localHostAddressSplit=localHostAddress.split('.')
    basicSubnet=localHostAddressSplit[0]+'.'+localHostAddressSplit[1]+'.'+localHostAddressSplit[2]+'.'
    allHosts=[basicSubnet+`i` for i in range(1,255)]
    
    #gateway
    gatewayD=netifaces.gateways()
    gatewayDLookup=gatewayD[netifaces.AF_INET]
    gateway=gatewayDLookup[0][0]
    
    networkMap=[localHostAddress, allHosts, gateway]
    return networkMap
  

def getActiveHosts(nm):    
    activeHosts=[]
    for i in range(0,254):
        activeCheck=os.system('ping -c1 -t1 ' + nm[1][i])
        if(activeCheck==0):
            activeHosts.append(nm[1][i])
            
    return activeHosts    



nm=createNetworkMap()
getActiveHosts(nm)