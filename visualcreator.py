import os

def create(ips, locations, lattitudes, longtitudes, orgs):
    if not ips:
        print("[-]  No Ips detected. Exiting...")
        exit()
    if (isinstance(ips, list) and isinstance(locations, list) and isinstance(lattitudes, list) and isinstance(longtitudes, list) and isinstance(orgs, list)):
        #Parse data as list
        if (len(ips) == len(locations) and len(ips) == len(lattitudes) and len(ips) == len(longtitudes) and len(ips) == len(orgs)):
            htmloutput = ParseGeoTraces(ips,locations,lattitudes,longtitudes,orgs)
        else:
            print("[-]  Lengths do not match! Exiting...")
            exit()        
    elif not isinstance(ips, list) and not isinstance(locations, list) and not isinstance(lattitudes, list) and not isinstance(longtitudes, list) and not isinstance(orgs, list):
        #Parse data as singular trace
        htmloutput = ParseGeoTrace(ips,locations,lattitudes,longtitudes,orgs)
    else:
        print("[-]  Variable types are not matching")
        exit()

    with open('htmlTemplate', 'r') as html:
        output = open('htmloutput.html', 'w')
        htmltemplate = html.read()
        htmltemplate = htmltemplate.replace('%LOCATIONS%',htmloutput)
        output.write(htmltemplate)
        output.close()
       
    os.system("firefox htmloutput.html")


def ParseGeoTrace(ip, location, lattitude, longtitude, org, appendComma=False, marker=1):
    inside = "['{0}',{1},{2},{3}]".format('{0} | {1} org:{2}'.format(ip, location, org), lattitude, longtitude, marker)
    
    if appendComma:
        return inside + ','
    if not appendComma and marker > 1:
        return inside
    skeleton = "var locations = [{0}];".format(inside)
    return skeleton

def ParseGeoTraces(ips, locations, lattitudes, longtitudes, orgs):
    inside = ''
    for i in range(len(ips)):
        inside = inside + ParseGeoTrace(ips[i], locations[i], lattitudes[i], longtitudes[i], orgs[i], appendComma=True, marker=i)
    inside = inside[:-1]
    skeleton = "var locations = [{0}];".format(inside)
    return skeleton

#create(['192.168.1.58', '10.10.10.10'],["location1", "Home"],[10,20],[10,30],["Pap Industries", "Software Devs"])


