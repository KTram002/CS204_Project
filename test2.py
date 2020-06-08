#!/usr/bin/env python
import os

from mininet.node import Controller
from mininet.topo import Topo

class MyTopo ( Topo ):
    def __init__( self ):
        Topo.__init__( self )
    #def build(self , **_opts ):
        #    info( '*** Add switches\n')
            s1 = self.addSwitch('s1')
            s2 = self.addSwitch('s2')
            s3 = self.addSwitch('s3')

        #    info( '*** Add hosts\n')
            h1 = self.addHost('h1', ip='10.0.0.1')
            h2 = self.addHost('h2', ip='10.0.0.2')
            h3 = self.addHost('h3', ip='10.0.0.3')

        #    info( '* Add links\n')
            self.addLink(h1, s1, cls=TCLink, bw=10, delay='1ms', loss=1)
            self.addLink(h2, s1, cls=TCLink, bw=10, delay='1ms', loss=1)
            self.addLink(h3, s1, cls=TCLink, bw=10, delay='1ms', loss=1)

            self.addLink(h1, s2, cls=TCLink, bw=10, delay='1ms', loss=1)
            self.addLink(h2, s2, cls=TCLink, bw=10, delay='1ms', loss=1)
            self.addLink(h3, s2, cls=TCLink, bw=10, delay='1ms', loss=1)

            self.addLink(h1, s3, cls=TCLink, bw=10, delay='1ms', loss=1)
            self.addLink(h2, s3, cls=TCLink, bw=10, delay='1ms', loss=1)
            self.addLink(h3, s3, cls=TCLink, bw=10, delay='1ms', loss=1)


"""
def myNetwork():
    topo = MyTopo()
    net = Mininet( topo=topo )
    #info( '*** Adding controller\n' )
    #net.addController(name='c0')
    
    info( '* Starting network\n')
    net.start()
    net['s1'].cmd('ovs-vsctl add-port s1 enp0s9')
    net['s2'].cmd('ovs-vsctl add-port s2 enp0s10')
    net['s3'].cmd('ovs-vsctl add-port s3 enp0s3')

    net['h1'].cmd('ifconfig h1-eth0 0')
    net['h1'].cmd('dhclient h1-eth0')
 
    net['h2'].cmd('ifconfig h2-eth0 0')
    net['h2'].cmd('dhclient h2-eth0')
 
    net['h3'].cmd('ifconfig h3-eth0 0')
    net['h3'].cmd('dhclient h3-eth0')

    net['h1'].cmd('ifconfig h1-eth1 0')
    net['h1'].cmd('dhclient h1-eth1')
 
    net['h2'].cmd('ifconfig h2-eth1 0')
    net['h2'].cmd('dhclient h2-eth1')
 
    net['h3'].cmd('ifconfig h3-eth1 0')
    net['h3'].cmd('dhclient h3-eth1')

    net['h1'].cmd('ifconfig h1-eth2 0')
    net['h1'].cmd('dhclient h1-eth2')
 
    net['h2'].cmd('ifconfig h2-eth2 0')
    net['h2'].cmd('dhclient h2-eth2')
 
    net['h3'].cmd('ifconfig h3-eth2 0')
    net['h3'].cmd('dhclient h3-eth2')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
"""

topos = { 'mytopo': ( lambda: MyTopo() ) }
