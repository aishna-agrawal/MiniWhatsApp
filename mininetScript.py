from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController
import time
class CustomTopo (Topo):

    def build(self):

        B = self.addSwitch('s1')
        C = self.addSwitch('s2')
        D = self.addSwitch('s3')
        E = self.addSwitch('s4')
        F = self.addSwitch('s5')
        G = self.addSwitch('s6')
        A = self.addSwitch('s7')
        S = self.addHost('h1') #registry.py
        H = self.addHost('h2') #peer.py
        I = self.addHost('h3') #peer.py
        J = self.addHost('h4') #peer.py
        K = self.addHost('h5') #peer.py
        L = self.addHost('h6') #peer.py
        M = self.addHost('h7') #peer.py
        N = self.addHost('h8') #peer.py
        O = self.addHost('h9') #peer.py
        self.addLink(S, A, bw=4)
        self.addLink(A, B, bw=4)
        self.addLink(A, C, bw=4)
        self.addLink(B, D, bw=2)
        self.addLink(B, E, bw=2)
        self.addLink(D, H, bw=1)
        self.addLink(D, I, bw=1)
        self.addLink(E, J, bw=1)
        self.addLink(E, K, bw=1)
        self.addLink(C, F, bw=2)
        self.addLink(C, G, bw=2)
        self.addLink(F, L, bw=1)
        self.addLink(F, M, bw=1)
        self.addLink(G, N, bw=1)
        self.addLink(G, O, bw=1)

topo = CustomTopo()
net = Mininet(topo)
net.start()
CLI(net)
net.stop()
