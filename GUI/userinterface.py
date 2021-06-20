import tkinter as tk
from tkinter import *
from tkinter import filedialog
from pathlib import Path

### CSS for python? lol? -- steelblue2 for frame bg, steelblue2 for labels and gray91 for writing.

class Adapters(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.allbuttons = []
        self.highlighted_row = 0

        adapterframe = Frame(self, bg="steelblue2", height=620, width=530, bd=4)
        adapterframe.pack(side="left", padx=2, pady=2)
        adapterframe.pack_propagate(0)

        head = Label(adapterframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="ADAPTERS", font=("roboto", 24), fg="gray91")
        head.pack(side="top", padx=2, pady=2)

        # make the canvas & scrollbar for where we are holding our packets
        self.adapterrows = Canvas(adapterframe, bg="steelblue2", relief="flat")
        adapterframevsb = Scrollbar(
            adapterframe, orient="vertical", command=self.adapterrows.yview, bd=0)
        self.adapterrows.pack(side="top", padx=2, pady=2)
    
    def addAdapters(self, adapter, adapterid):
        self.button = Button(self.adapterrows)
        self.button.configure(text=str(adapter.name))
        self.button.pack(fill="both")
        self.button.configure(activebackground="lightgreen", highlightcolor="lightblue", background="steelblue2", font=("roboto", 12), borderwidth=0, command=lambda: self.onClick(adapter, adapterid))
        self.onHover(self.button)
        self.allbuttons.append(self.button)
        self.adapterrows.update()
        self.adapterrows.configure(scrollregion=self.adapterrows.bbox("all"))

    def onHover(self, button):
        if(button['bg'] == "lightgreen"):
            button['activebackground']="lightgreen"
            button.bind("<Leave>", func=lambda e: button.config(
                background="lightgreen"))
            button.bind("<Enter>", func=lambda e: button.config(
                background="lightblue"))
        elif(button['bg'] == "steelblue2"):
            button['activebackground']="steelblue2"
            button.bind("<Leave>", func=lambda e: button.config(
                background="steelblue2"))
            button.bind("<Enter>", func=lambda e: button.config(
                background="lightblue"))

    def onClick(self, adapter, adapterid):
        specific_row=self.allbuttons[adapterid-1]
        old_row=self.allbuttons[self.highlighted_row]

        # set current row highlighted
        
        specific_row.configure(bg="lightgreen")
        self.onHover(specific_row)

        # set old row not highlighted
        
        old_row.configure(bg="steelblue2")
        self.onHover(old_row)

        self.highlighted_row = adapterid - 1

        self.parent.configurationframe.loadInfo(adapter)
        self.parent._main.changeCurrentAdapter(adapter, self.parent.configurationframe.presetname.get())
        print(self.parent.configurationframe.presetname.get())


class Configuration(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        
        self.name = StringVar()
        self.ip = StringVar()
        self.ipEnabled = StringVar()
        self.subnet = StringVar()
        self.dnsPREF = StringVar()
        self.dnsALT = StringVar()
        self.dhcpEnabled = StringVar()
        self.defaultIPGateway = StringVar()
        self.presetname = StringVar()

        self.configurationframe = Frame(self, bg="steelblue2", height=620, width=530, bd=4)
        self.configurationframe.pack(side="left", padx=2, pady=2)
        self.configurationframe.pack_propagate(0)

        head = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="CONFIGURATION", font=("roboto", 24), fg="gray91")
        head.pack(side="top", padx=2, pady=2, fill="both")

        preset = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="PRESET NAME", font=("roboto", 12), fg="gray91")
        preset.pack(side="top", padx=2, pady=2)
        presetE = Entry(self.configurationframe,  bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.presetname, font=("roboto", 12))
        presetE.pack(side="top", padx=2, pady=2)

        name = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="ADAPTER NAME", font=("roboto", 12), fg="gray91")
        name.pack(side="top", padx=2, pady=2)
        nameE = Entry(self.configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.name, font=("roboto", 12))
        nameE.pack(side="top", padx=2, pady=2, fill="both")
        nameE.config(state='disabled')

        ip = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="IP ADDRESS", font=("roboto", 12), fg="gray91")
        ip.pack(side="top", padx=2, pady=2)
        self.ipE = Entry(self.configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.ip, validate="key", validatecommand=(self.ipVal, '%P', '%S'), font=("roboto", 12))
        self.ipE.pack(side="top", padx=2, pady=2, fill="both")

        ipEnabled = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="IP ENABLED?", font=("roboto", 12), fg="gray91")
        ipEnabled.pack(side="top", padx=2, pady=2)
        ipEnabledE = Entry(self.configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.ipEnabled, font=("roboto", 12))
        ipEnabledE.pack(side="top", padx=2, pady=2, fill="both")

        subnet = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="SUBNET", font=("roboto", 12), fg="gray91")
        subnet.pack(side="top", padx=2, pady=2)
        subnet = Entry(self.configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.subnet, font=("roboto", 12))
        subnet.pack(side="top", padx=2, pady=2, fill="both")

        dhcpEnabled = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="DHCP ENABLED?", font=("roboto", 12), fg="gray91")
        dhcpEnabled.pack(side="top", padx=2, pady=2)
        dhcpEnabledE = Entry(self.configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.dhcpEnabled, font=("roboto", 12))
        dhcpEnabledE.pack(side="top", padx=2, pady=2, fill="both")

        defaultGateway = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="DEFAULT GATEWAY", font=("roboto", 12), fg="gray91")
        defaultGateway.pack(side="top", padx=2, pady=2)
        self.defaultGatewayE = Entry(self.configurationframe,  bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.defaultIPGateway, font=("roboto", 12))
        self.defaultGatewayE.pack(side="top", padx=2, pady=2, fill="both")

        dnsPREF = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="DNS PREFERRED", font=("roboto", 12), fg="gray91")
        dnsPREF.pack(side="top", padx=2, pady=2)
        dnsPREFE = Entry(self.configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.dnsPREF, font=("roboto", 12))
        dnsPREFE.pack(side="top", padx=2, pady=2, fill="both")
        dnsPREFE.config(state='disabled')

        dnsALT = Label(self.configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="DNS ALT", font=("roboto", 12), fg="gray91")
        dnsALT.pack(side="top", padx=2, pady=2)
        dnsALTE = Entry(self.configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.dnsALT, font=("roboto", 12))
        dnsALTE.pack(side="top", padx=2, pady=2, fill="both")
        dnsALTE.config(state='disabled')

        self.DGbutton = Button(self.configurationframe)
        self.DGbutton.configure(text=str("AUTO GATEWAY"), height=60, width=5)
        self.DGbutton.pack(fill="both", side="top", anchor=N)
        self.DGbutton.configure(activebackground="lightgreen", highlightcolor="lightblue", background="steelblue2", font=("roboto", 12), borderwidth=0, command=lambda: self.onClick(None, 1))
        self.onHover(self.DGbutton)
        
    def ipVal(self, P, S):
        if S.isdigit():
            if 0 <= len(str(P)) <= 3:
                return True
        return False

    def onHover(self, button):
        if(button['bg'] == "lightgreen"):
            button['activebackground']="lightgreen"
            button.bind("<Leave>", func=lambda e: button.config(
                background="lightgreen"))
            button.bind("<Enter>", func=lambda e: button.config(
                background="lightblue"))
        elif(button['bg'] == "steelblue2"):
            button['activebackground']="steelblue2"
            button.bind("<Leave>", func=lambda e: button.config(
                background="steelblue2"))
            button.bind("<Enter>", func=lambda e: button.config(
                background="lightblue"))

    def onClick(self, adapter, adapterid):
        count = 0
        newText = self.ipE.get()
        newText.split()
        newText = newText[::-1]
        for i in range(0, len(newText)):
            if((newText[i] != '.') & (count<3)):
                count +=1
            else:
                newText = newText[i:]
                break
        newText = newText[::-1]
        self.defaultIPGateway.set(newText + "1")

    def loadPreset(self):
        filename=filedialog.askopenfile(mode="r")
        return filename

    def loadInfo(self, adapter):
        self.name.set(adapter.name)
        self.ip.set(adapter.ip)
        self.ipEnabled.set(adapter.ipEnabled)
        self.subnet.set(adapter.subnet)
        self.dnsPREF.set(adapter.dnsPREF)
        self.dnsALT.set(adapter.dnsALT)
        self.dhcpEnabled.set(adapter.dhcpEnabled)
        self.defaultIPGateway.set(adapter.defaultIPGateway)
        self.presetname.set(adapter.presetname)
        self.configurationframe.update()


class Presets(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        presetframe = Frame(self, bg="steelblue2", height=620, width=280, bd=4)
        presetframe.pack(side="left", padx=2, pady=2)
        presetframe.pack_propagate(0)

        head = Label(presetframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="PRESETS", font=("roboto", 24), fg="gray91")
        head.pack(side="top", padx=2, pady=2)


class ChangeSave(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        changesaveframe = Frame(self, bg="steelblue2", height=80, width=1076, bd=4)
        changesaveframe.pack(side="bottom", padx=2, pady=2)
        changesaveframe.pack_propagate(0)

        self.save = Button(changesaveframe)
        self.save.configure(text="SAVE PRESET", height=50, width=40)
        self.save.pack(side="right")
        self.save.configure(activebackground="lightgreen", highlightcolor="lightblue", background="steelblue2", font=("roboto", 12), borderwidth=0, command=lambda: self.onClick(adapter, adapterid))
        self.onHover(self.save)

        self.load = Button(changesaveframe)
        self.load.configure(text="LOAD PRESET", height=50, width=40)
        self.load.pack(side="right")
        self.load.configure(activebackground="lightgreen", highlightcolor="lightblue", background="steelblue2", font=("roboto", 12), borderwidth=0, command=lambda: self.onClick(adapter, adapterid))
        self.onHover(self.load)

        self.applypreset = Button(changesaveframe)
        self.applypreset.configure(text="APPLY PRESET", height=50, width=40)
        self.applypreset.pack(side="right")
        self.applypreset.configure(activebackground="lightgreen", highlightcolor="lightblue", background="steelblue2", font=("roboto", 12), borderwidth=0, command=lambda: self.onClick(adapter, adapterid))
        self.onHover(self.applypreset)


    def onHover(self, button):
        if(button['bg'] == "lightgreen"):
            button['activebackground']="lightgreen"
            button.bind("<Leave>", func=lambda e: button.config(
                background="lightgreen"))
            button.bind("<Enter>", func=lambda e: button.config(
                background="lightblue"))
        elif(button['bg'] == "steelblue2"):
            button['activebackground']="steelblue2"
            button.bind("<Leave>", func=lambda e: button.config(
                background="steelblue2"))
            button.bind("<Enter>", func=lambda e: button.config(
                background="lightblue"))

    def onClick(self, adapter, adapterid):
        specific_row=self.allbuttons[adapterid-1]
        old_row=self.allbuttons[self.highlighted_row]

        # set current row highlighted
        
        specific_row.configure(bg="lightgreen")
        self.onHover(specific_row)

        # set old row not highlighted
        
        old_row.configure(bg="steelblue2")
        self.onHover(old_row)

        self.highlighted_row = adapterid - 1

    def setButton(self, name, func):
        if(name == "SAVE PRESET"):
            self.save.configure(command=func)
        elif(name == "APPLY PRESET"):
            self.applypreset.configure(command=func)
        elif(name == "LOAD PRESET"):
            self.load.configure(command=func)


class UserInterface(tk.Tk):
    def __init__(self, main):
        super().__init__(screenName="Network Adapter Configuration")
        self._main = main
        self.minsize(1080, 720)
        pathiconimg = Path(__file__).parent / "img/package.png"
        self.iconphoto(False,
                       tk.PhotoImage(file=str(pathiconimg)))
        self.state('zoomed')
        self.title('Network Adapter Configuration')
        self.adapterid = 0

        self.changesave=ChangeSave(self)
        self.changesave.pack(side="bottom",
                              padx=2, pady=2, expand=True)

        self.adapterframe=Adapters(self)
        self.adapterframe.pack(side="left",
                              padx=2, pady=2, expand=True)

        self.configurationframe=Configuration(self)
        self.configurationframe.pack(side="left",
                              padx=2, pady=2, expand=True)
        
        #self.presetframe=Presets(self)
        #self.presetframe.pack(side="left",
        #                      padx=2, pady=2, expand=True)

    def addAdapter(self, adapter):
        self.adapterid += 1
        self.adapterframe.addAdapters(adapter, self.adapterid)
    
    def registerAdapter(self, adapter):
        try:
            for widget in self.adapterframe.adapterrows.winfo_children():
                if widget.winfo_class() == "Button":
                    if widget['text'] == str(adapter.name):
                        widget.invoke()
        except:
            pass
        self.configurationframe.loadInfo(adapter)

    
    def add_button_command(self, name, func):
        self.changesave.setButton(name, func)

    def pop_message(self, title, msg):
        popup=Toplevel(self)
        popup.title(title)
        label=Label(popup, text=msg, font=("roboto", 10))
        label.pack(side="top", fill="x", pady=10, padx=10)
        ok=Button(popup, text="Okay", command=popup.destroy)
        ok.pack(side="bottom", pady=10)
        popup.mainloop()

    def render(self):
        self.mainloop()