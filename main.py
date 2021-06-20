from GUI import userinterface as ui
from Adapters import adapters as ad
from Adapters import apply as apply
from File import files

class Application():
    def __init__(self):
        self.ui = ui.UserInterface(self)
        self.currentAdapter = ad.Adapter([None])
        self.currentPresetName = None
        self.ui.add_button_command("SAVE PRESET", self._savePreset)
        self.ui.add_button_command("LOAD PRESET", self._loadPreset)
        self.ui.add_button_command("APPLY PRESET", self._applyPreset)
        self.files = files
        self._populateAdapters()
        self.ui.render()

    def _populateAdapters(self):
        for interface in ad.nic_configs:
            adapter = ad.Adapter(interface)
            self.ui.addAdapter(adapter)
    
    def _applyPreset(self):
        self.currentPresetName = self.ui.configurationframe.presetname.get()
        self.currentAdapter.presetname = self.ui.configurationframe.presetname.get()
        self.currentAdapter.name = self.ui.configurationframe.name.get()
        self.currentAdapter.ip = self.ui.configurationframe.ip.get()
        self.currentAdapter.ipEnabled = self.ui.configurationframe.ipEnabled.get()
        self.currentAdapter.subnet = self.ui.configurationframe.subnet.get()
        self.currentAdapter.dnsPREF = self.ui.configurationframe.dnsPREF.get()
        self.currentAdapter.dnsALT = self.ui.configurationframe.dnsALT.get()
        self.currentAdapter.dhcpEnabled = self.ui.configurationframe.dhcpEnabled.get()
        self.currentAdapter.defaultIPGateway = self.ui.configurationframe.defaultIPGateway.get()
        apply.main(self.currentAdapter)
        return

    def _savePreset(self):
        self.currentPresetName = self.ui.configurationframe.presetname.get()
        self.currentAdapter.presetname = self.ui.configurationframe.presetname.get()
        self.currentAdapter.name = self.ui.configurationframe.name.get()
        self.currentAdapter.ip = self.ui.configurationframe.ip.get()
        self.currentAdapter.ipEnabled = self.ui.configurationframe.ipEnabled.get()
        self.currentAdapter.subnet = self.ui.configurationframe.subnet.get()
        self.currentAdapter.dnsPREF = self.ui.configurationframe.dnsPREF.get()
        self.currentAdapter.dnsALT = self.ui.configurationframe.dnsALT.get()
        self.currentAdapter.dhcpEnabled = self.ui.configurationframe.dhcpEnabled.get()
        self.currentAdapter.defaultIPGateway = self.ui.configurationframe.defaultIPGateway.get()
        
        self.ui.pop_message("File Saved", "File " + str(self.files.Data(self.currentAdapter
            ).createFile(self.currentAdapter, self.currentPresetName)) + " successfully created.")
    
    def _loadPreset(self):
        fn = self.ui.configurationframe.loadPreset()
        data = self.files.Data(None).loadFile(fn)
        self._registerAdapter(data)

    def _registerAdapter(self, adapter):
        self.ui.registerAdapter(adapter)

    def changeCurrentAdapter(self, adapter, presetname):
        #self.currentAdapter = adapter
        return

# Exec main if this python file is run directly
if __name__ == "__main__":
    app = Application()