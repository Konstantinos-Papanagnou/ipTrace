import requests
import sys
import json

class ResponseParser:

    def __init__(self, verbose):
        self.url = "http://ip-api.com/json/"
        self.verbose = verbose

    def GetParsedData(self, ip):
        response = self.GetResponse(ip)
        parsed = json.loads(response.text)
        
        if parsed['status'] != 'success':
            sys.stderr.write('[-] Could not pull up any info on ip: {0}\n'.format(ip))
        
        del parsed['status']
        newdict = {}

        keys = parsed.keys()
        for key in keys:
            if parsed[key] == '':
                continue
            newdict[key] = parsed[key]
        return newdict


    def GetResponse(self, ip):
        try:
            return requests.get(self.url + ip)
        except Exception as ex:
            sys.stderr.write('Something went wrong with the request to the remote server :( ...\nMore Details: {0}\n'.format(str(ex)))
        
    

def Debug():
    rp = ResponseParser(True)
    response = rp.GetParsedData('46.12.148.37')
    print(response)

if __name__ == '__main__':
    Debug()
