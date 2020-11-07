import sys
import socket

class Resolver:
    
    def __init__(self, ipaddr, verbose):
        self.ipaddr = []
        if isinstance(ipaddr, list):
            for ip in ipaddr:
                self.resolve(ip, verbose, True)
        else:  # if its not a list
            self.resolve(ipaddr, verbose, False)


    def resolve(self, ip, verbose, append=True):
        if self.isDomain(ip):
            try:
                temp = socket.gethostbyname(ip)
                if append:
                    self.ipaddr.append(temp)
                else:
                    self.ipaddr = temp
                if verbose:
                    print('[+] Domain name {0} registered to: {1}'.format(ip, temp))
            except socket.gaierror:
                if verbose:
                    sys.stderr.write('[-] Invalid domain name. Maybe the domain is not registered or it is malformed    Skipping domain: [{0}]...\n'.format(ip))
        else: # if its not a domain
            if append:
                self.ipaddr.append(ip)
            else:
                self.ipaddr = ip
            if verbose:
                print('[+] Ip: {0}'.format(ip))


    def isDomain(self, ip):
        regex = 'abcdefghijklmopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' 
        for c in regex:
            if c in ip: 
                return True
        return False

    def getResolvedIps(self):
        return self.ipaddr


