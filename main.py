from GUI import userinterface as ui
from Adapters import adapters as ad
from File import files

class Application():
    def __init__(self):
        self.ui = ui.UserInterface(self)
        self.currentAdapter = None
        self.currentPresetName = None
        self.ui.add_button_command("SAVE PRESET", self._savePreset)
        self.ui.add_button_command("LOAD PRESET", self._loadPreset)
        self.files = files
        self._populateAdapters()
        self.ui.render()

    def _populateAdapters(self):
        for interface in ad.nic_configs:
            adapter = ad.Adapter(interface)
            self.ui.addAdapter(adapter)

    def _savePreset(self):
        self.currentAdapter.presetname=self.currentPresetName
        self.ui.pop_message("File Saved", "File " + str(self.files.Data(self.currentAdapter
            ).createFile(self.currentAdapter, self.currentPresetName)) + " successfully created.")
    
    def _loadPreset(self):
        fn = self.ui.configurationframe.loadPreset()
        data = self.files.Data(None).loadFile(fn)
        self._registerAdapter(data)

    def _registerAdapter(self, adapter):
        self.ui.registerAdapter(adapter)

    def changeCurrentAdapter(self, adapter, presetname):
        self.currentPresetName = presetname
        self.currentAdapter = adapter


# Exec main if this python file is run directly
if __name__ == "__main__":
    app = Application()