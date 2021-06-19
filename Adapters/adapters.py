import wmi
import winreg as wr
import json

# initialise by scanning for all adapters
c = wmi.WMI()
nic_configs = c.Win32_NetworkAdapterConfiguration()
nic_configs.reverse()

class Adapter():
    def __init__(self, adapter):
        try: self.name = adapter.caption[10:]
        except: self.name = "none"
        try: self.name = adapter.caption[10:]
        except: self.name = "none"
        try: self.ip = adapter.IPAddress[0]
        except: self.ip = "none"
        try: self.ipEnabled = adapter.IPEnabled
        except: self.ipEnabled = "none"
        try: self.subnet = adapter.IPSubnet[0]
        except: self.subnet = self.subnet = "none"
        try: self.dnsPREF = adapter.DNSServerSearchOrder[0]
        except: self.dnsPREF = "none"
        try: self.dnsALT = adapter.DNSServerSearchOrder[1]
        except: self.dnsALT = "none"
        try: self.dhcpEnabled = adapter.DHCPEnabled
        except: self.dhcpEnabled = "none"
        try: self.defaultIPGateway = adapter.DefaultIPGateway[0]
        except: self.defaultIPGateway = "none"
        try: self.presetname = adapter.presetname
        except:self.presetname = "none"

    def get_json(self):
        return json.dumps(self.__dict__)
