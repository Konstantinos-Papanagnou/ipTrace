import sys
import argparse
from bannermagic import printBannerPadding, printMessage

class ArgumentParser:

    def __init__(self):
        self.printBanner()
        parser = self.ConfigureParser()
        args = parser.parse_args()
        self.verbosity = args.verbose
        self.accurate = args.accurate 
        self.visual = args.visual
        if self.accurate and self.visual:
            print('[-]  Unable to use accurate mode with visual mode!')
        if args.input:
            self.list = False
            self.ipaddr = args.input
        else:
            if not args.listinput:
                sys.stderr.write('You need to specify at least -i or -l option!\n\n Run iptrace.py -h for more help\n')
                exit()
            self.list = True
            with open(args.listinput, 'r') as inputfile:
                content = inputfile.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
            self.ipaddr = content
        self.output = args.output
        self.mobile = args.mobile

    def printBanner(self):
        printBannerPadding('*')
        printMessage('IP TRACE BY KONSTANTINOS PAP')
        printMessage('POWERED BY ip-api & whatismyipaddress.com')
        printBannerPadding('*')


    def ConfigureParser(self):
        parser = argparse.ArgumentParser(prog='iptrace.py', usage='iptrace.py [-h] [-v] [-a] [--visual] [-o outputfile] (-l inputfile)/(-i ipaddr)', description='Automation script for ip lookup', epilog='At least one of the -l or -i option must be declared!')
        parser.add_argument('-i', '--input', help='The ip address or domain name to examine')
        parser.add_argument('-v', '--verbose', action='store_true', help='Increase output verbosity')
        parser.add_argument('-l', '--listinput', help='Input a list of addresses and/or domain names from an external file. The file must contain one ip address or domain name per line')
        parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='Output file to export data')
        parser.add_argument('-a', '--accurate', action='store_true',  help="The ip-api is not very accurate on it's geolocation traces so use the -a option to get more accurate results from whatismyipaddress.com. whatismyipaddress strictly does not allow webscraping to their website so you will be prompted there automatically when using this option.")
        parser.add_argument('-V', '--visual', type=argparse.FileType('w'), help='Create Visual Map (Make a htmloutput.html file in the current directory and display it on firefox)')
        parser.add_argument('-m', '--mobile', action='store_true', help='Using Termux for android support')
        return parser

