import Resolver
import ArgumentParser
import ResponseParser
import webbrowser
import sys

def main():
    args = ArgumentParser.ArgumentParser()
    parser = Resolver.Resolver(args.ipaddr, args.verbosity)

    resolved_ips = parser.getResolvedIps()
    if args.output:
        outfile = open(args.output, 'a')
    
    try:
        if(isinstance(resolved_ips, list)):
        
            if not resolved_ips:
                sys.stderr.write('[-] Could not resolve any ips... Exiting...\n\n')
                exit()

            print('\n\n[*] Resolved Ips: {0}'.format(len(resolved_ips)))
            for ip in resolved_ips:
                printResults(ip, args.verbosity, args.accurate, outfile)

        else:
            if not resolved_ips:
                sys.stderr.write('[-] Could not resolve any ips... Exiting...\n\n')
                exit()

            print('\n\nResolved Ip: {0}'.format(resolved_ips))
            printResults(resolved_ips, args.verbosity, args.accurate, outfile)

        print('\n\n===============================================================\n\n')
        print('[+]  Trace Completed Successfully!')
    finally:
        outfile.close()

def printResults(ip, verbose, accurate, output):
    if accurate:
        webbrowser.get('firefox').open('https://whatismyipaddress.com/ip/{0}'.format(ip))
        if output:
            sys.stderr.write('[-] Cannot write results when working in high accuracy mode\n')
        return

    rp = ResponseParser.ResponseParser(verbose)
    data = rp.GetParsedData(ip)

    print('\n\n===============================================================\n\n')
    print('[*] Tracing {0}'.format(ip))
    output.write('================================================================\n\n')
    output.write('  Tracing {0}\n\n'.format(ip))
    print('\n[*] Trace')
    
    genkeys=data.keys()
    for key in genkeys:
        print('[*] {0}  :   {1}'.format(key, data[key]))
        output.write('{0}   :   {1}\n'.format(key, data[key]))


if __name__ == "__main__":
    main()
