#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    # Change main dir to this (need for Pentest Box)
    import os
    os.path.abspath(__file__)

    from Classes import (Credits,
                         OKadminFinderClass,
                         MessengerClass)

    import urllib2
    import socket
    import socks
    import sys
    from urllib2 import urlopen
    from colorama import Fore, Back, Style

    # Get Messenger class to print information
    messenger = MessengerClass.Messenger()

except():
    exit('\n\t[!] Session Cancelled; Something wrong with import modules')

try:
    # Get credits and print it
    messenger.writeMessage(Credits.getCredits()[0], 'green')

    # Get main class object
    OKadminFinder = OKadminFinderClass.OKadminFinder()

    # Add header from credits
    OKadminFinder.header = {'user-agent': 'OKadminFinder/%s' % Credits.getCredits()[1]}

    # Additional params
    if not messenger.writeRawInputWithYesNo(Fore.YELLOW + 'Do you want use default params?'):
        timeout = messenger.writeInput(Fore.YELLOW + 'Change timeout. Please write value in seconds: ' + Fore.GREEN)
        OKadminFinder.timeout = timeout

    tor = ""
    while (tor not in ["y","n"]):
        tor = raw_input(Fore.YELLOW + 'Would you like to use tor? [Y][n]  $ ')
        tor = tor.lower().strip()
        if tor == "y":
            socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
            socket.socket = socks.socksocket
            urllib2.urlopen
        
        elif tor == "n":
            continue

    print('')
    my_ip = urlopen('http://ip.42.pl/raw').read()
    messenger.writeMessage('Your IP address is:','cyan'); 
    print (my_ip) 
    print('')
    # Get site
    site = messenger.writeRawInput('Enter Site Name \nexample : example.com or www.example.com \n' +Fore.GREEN +'$ ', 'white'); print ('')
    
    if OKadminFinder.checkUrl(site):
        messenger.writeMessage('\nSite %s is stable\n' % site,'green')
    else:
        messenger.writeMessage('Something wrong with url', 'red')
        exit(SystemExit)

    # Get links for checking
    urls = OKadminFinder.getUrls('LinkFile/adminpanellinks.txt')

    # Counters for total links, and admin panel find
    totalCount = len(urls)
    adminCount = 0

    # Checking all links
    for url in urls:

        # Create test link with getting params from input and links.txt file
        reqLink = OKadminFinder.createReqLink(site, url)
        messenger.writeMessage('\t [#] Checking http://' + reqLink, 'yellow')

        # Test created link for HTTPerrors. If not error - potential admin panel
        if OKadminFinder.checkUrl(reqLink):
            adminCount += 1
            messenger.writeMessage('%s %s' % ('\n>>> http://' + reqLink, 'Admin page found!'), 'green')

            # Stopped process? and waiting for input for continue
            messenger.writeRawInput('Press enter to continue scanning.\n')

        # If HTTPerrors continue testing other links
        else:
            continue

    # Write last information about scanning with counters
    messenger.writeMessage('\n\nCompleted \n', 'green')
    messenger.writeMessage(str(adminCount) + ' Admin pages found', 'white')
    messenger.writeMessage(str(totalCount) + ' total pages scanned', 'white')
    messenger.writeRawInput('[/] Scanning over; Press Enter to Exit', 'green')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')

except (KeyboardInterrupt, SystemExit):
    messenger.writeMessage('\n\t[!] Session Cancelled', 'red')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')

except():
    messenger.writeMessage('\n\t[!] Session Cancelled; Unknown error', 'red')

    # This magic for Pentest Box. This is return normal color style of console
    messenger.writeMessage('','white')

