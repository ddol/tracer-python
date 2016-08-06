#!/usr/bin/env python
# Origional Author: Rikard Anglerud (2013-06-29)
# http://www.rawmeat.org/raspberrypi-network-monitor.html

import argh 
import re
import sh

class Route(object):
    def __init__(host=''):
        self.target=host
        
        

class Host(object):
    def __init__(ip = '0.0.0.0'):
        self.ip = ip
    
def ping(self):
    pass
        
    
def run(targets=[]):
    for target in targets:
        host=Host(target)
        print("host ip: ".format(host.ip))
        #route_hosts=Route(host)
    return None

def find_gateway(host):
    print 'Starting Traceroute...'
    gateway_lines = [l for l in sh.traceroute(host).split('\n')]
    print ' -> '.join(gateway_lines)
    return gateway_lines[0].strip().split()[1]


def ping_host(host_name):
    delay = sh.ping(host_name, 9)

    if not delay:
        return None

    return round(delay * 1000, 4)

    
def main():
    print 'Entering main()'
    failures = 0
    gateway_host = find_gateway('www.skynet.ie')
    print 'Measuring ping latency to {}'.format(gateway_host)

    try:
        while True:
            ping_time = ping_host(gateway_host)

            if not ping_time:
                failures += 1
                send_metric("network.dropout", failures)
                print 'packet lost'
            else:
                send_metric("network.ping_time", ping_time)
                print 'ping_time: {}'.format(ping_time)

            time.sleep(10)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    targets = ['8.8.8.8']
    #run(targets)
    argh.dispatch_command(main)

    