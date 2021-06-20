from os import error
from tkinter.constants import TRUE
from Adapters import adapters as ad

def main(adapter):
    a = None
    b = None
    e = None
    d = None
    print([adapter])
    for interface in ad.nic_configs:
        if (interface.caption[10:] == adapter.name):
            try: a = interface.EnableStatic(IPAddress=[adapter.ip], SubnetMask=[adapter.subnet])
            except error: print(error); pass
            try: b = interface.SetGateways(DefaultIPGateway=[adapter.defaultIPGateway])
            except error: print(error); pass
            dnsSearchorder = [str(adapter.dnsPREF), str(adapter.dnsALT)]
            print(dnsSearchorder)
            try: h = interface.SetDynamicDNSRegistration(1)
            except error: print(error)
            #try: e = interface.SetDNSServerSearchOrder([dnsSearchorder])
            #except error: print(error); pass
            if(adapter.dhcpEnabled == "1"):
                try: d = interface.EnableDHCP()
                except error: print(error); pass
            print(a, b, e, d, h)