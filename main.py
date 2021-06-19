from GUI import userinterface as ui
from Adapters import adapters as ad
from File import files

class Application():
    def __init__(self):
        self.ui = ui.UserInterface(self)
        self.currentAdapter = None
        self.currentPresetName = None
        self.ui.add_button_command("SAVE PRESET", self._savePreset)
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
    
    def changeCurrentAdapter(self, adapter, presetname):
        self.currentPresetName = presetname
        self.currentAdapter = adapter


# Exec main if this python file is run directly
if __name__ == "__main__":
    app = Application()