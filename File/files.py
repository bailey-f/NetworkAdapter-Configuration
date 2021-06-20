from Adapters import adapters as ad
import os
import json

class Data():
    def __init__(self, adapter):
        self.filename = "Presets"

    def createFile(self, adapter, presetname):
        # make a path for the new folder
        self.directory = str(self.filename)
        self.parent_dir = "C:/NETWORK INTERFACE PRESETS/"
        self.path = os.path.join(self.parent_dir, self.directory)

        try:
            os.mkdir(self.path)
        except:
            pass

        self.file_path = self.path + "/" + adapter.name + "-" + str(presetname) + ".json"
        # count number of files already in directory and therefore new file name
        print("file " + str(self.file_path) + " made")

        # json dump the contents
        with open(self.file_path, 'a') as f:
            f.write(adapter.get_json() + "\n")
            f.close()

        return str(self.file_path)

    def loadFile(self, file):
        data = None
        for line in file:
            line = json.loads(line)
            data = (ad.Adapter(line))
        file.close()
        return data

    def get_normal(self, rdata):
        rdata = rdata[1:(len(rdata)-2)]
        rdata = rdata.strip()
        bytesr = (rdata)
        return bytesr
