#!/usr/bin/env python
import os

from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.cli import CLI
from mininet.link import TCLink
from mininet.link import Intf
from mininet.log import setLogLevel, info

def myNetwork():
    net = Mininet( topo=None, build=False)
    info( '*** Adding controller\n' )
    net.addController(name='c0')
    
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1')
    
    info( '*** Add hosts\n')
    h1 = net.addHost('h1', ip='10.0.0.1')
    h2 = net.addHost('h2', ip='10.0.0.2')
    h3 = net.addHost('h3', ip='10.0.0.3')

    info( '*** Add links\n')
    net.addLink(h1, s1, cls=TCLink, bw=1000, delay='1ms', loss=1)
    net.addLink(h2, s1, cls=TCLink, bw=1000, delay='1ms', loss=1)
    net.addLink(h3, s1, cls=TCLink, bw=1000, delay='1ms', loss=1)

    info( '*** Starting network\n')
    net.start()

    os.popen('ovs-vsctl add-port s1 enp0s3')

#    h1.cmdPrint('dhclient '+h1.defaultIntf().name)
#    h2.cmdPrint('dhclient '+h2.defaultIntf().name)
#    h3.cmdPrint('dhclient '+h3.defaultIntf().name)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
