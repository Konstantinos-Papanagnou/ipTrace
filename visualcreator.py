import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler


def create(ips, locations, lattitudes, longtitudes, orgs, outfile, mobileSupport):
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

    htmlpath = os.path.realpath(__file__).split('/')[:-1]
    htmlpath = '/'.join(htmlpath)
    htmlpath += '/htmlTemplate'

    with open(htmlpath, 'r') as html:
        htmltemplate = html.read()
        htmltemplate = htmltemplate.replace('%LOCATIONS%',htmloutput)
        outfile.write(htmltemplate)
        outfile.close()
       
    if mobileSupport:
        # Open a simple http server and trigger it to open the url on the default browser.
        httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
        os.system(f'xdg-open http://localhost:8000/{outfile.name}')
        httpd.serve_forever()
    else:
        os.system(f"firefox {outfile.name}")


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
