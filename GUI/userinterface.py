import tkinter as tk
from tkinter import *
from pathlib import Path

### CSS for python? lol? -- steelblue2 for frame bg, steelblue2 for labels and gray91 for writing.

class Adapters(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent

        self.allbuttons = []
        self.highlighted_row = 0

        adapterframe = Frame(self, bg="steelblue2", height=620, width=400, bd=4)
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

        configurationframe = Frame(self, bg="steelblue2", height=620, width=400, bd=4)
        configurationframe.pack(side="left", padx=2, pady=2)
        configurationframe.pack_propagate(0)

        head = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="CONFIGURATION", font=("roboto", 24), fg="gray91")
        head.pack(side="top", padx=2, pady=2, fill="both")

        name = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="NAME", font=("roboto", 12), fg="gray91")
        name.pack(side="top", padx=2, pady=2)
        nameE = Entry(configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.name, font=("roboto", 12))
        nameE.pack(side="top", padx=2, pady=2, fill="both")

        ip = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="IP ADDRESS", font=("roboto", 12), fg="gray91")
        ip.pack(side="top", padx=2, pady=2)
        ipE = Entry(configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.ip, validate="key", validatecommand=(self.ipVal, '%P', '%S'), font=("roboto", 12))
        ipE.pack(side="top", padx=2, pady=2)

        ipEnabled = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="IP ENABLED?", font=("roboto", 12), fg="gray91")
        ipEnabled.pack(side="top", padx=2, pady=2)
        ipEnabledE = Entry(configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.ipEnabled, font=("roboto", 12))
        ipEnabledE.pack(side="top", padx=2, pady=2)

        subnet = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="SUBNET", font=("roboto", 12), fg="gray91")
        subnet.pack(side="top", padx=2, pady=2)
        subnet = Entry(configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.subnet, font=("roboto", 12))
        subnet.pack(side="top", padx=2, pady=2)

        dnsPREF = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="DNS PREFERRED", font=("roboto", 12), fg="gray91")
        dnsPREF.pack(side="top", padx=2, pady=2)
        dnsPREFE = Entry(configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.dnsPREF, font=("roboto", 12))
        dnsPREFE.pack(side="top", padx=2, pady=2)

        dnsALT = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="DNS ALT", font=("roboto", 12), fg="gray91")
        dnsALT.pack(side="top", padx=2, pady=2)
        dnsALTE = Entry(configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.dnsALT, font=("roboto", 12))
        dnsALTE.pack(side="top", padx=2, pady=2)

        dhcpEnabled = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="DHCP ENABLED?", font=("roboto", 12), fg="gray91")
        dhcpEnabled.pack(side="top", padx=2, pady=2)
        dhcpEnabledE = Entry(configurationframe, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.dhcpEnabled, font=("roboto", 12))
        dhcpEnabledE.pack(side="top", padx=2, pady=2)

        defaultGateway = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="DEFAULT GATEWAY", font=("roboto", 12), fg="gray91")
        defaultGateway.pack(side="top", padx=2, pady=2)
        defaultGatewayE = Entry(configurationframe,  bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.defaultIPGateway, font=("roboto", 12))
        defaultGatewayE.pack(side="top", padx=2, pady=2)
        
        preset = Label(configurationframe, anchor=CENTER, bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, text="PRESET NAME", font=("roboto", 12), fg="gray91")
        preset.pack(side="top", padx=2, pady=2)
        presetE = Entry(configurationframe,  bg="steelblue2", bd=2, justify=CENTER, relief=FLAT, textvariable=self.presetname, font=("roboto", 12))
        presetE.pack(side="top", padx=2, pady=2)

    def ipVal(self, P, S):
        if S.isdigit():
            if 0 <= len(str(P)) <= 3:
                return True
        return False

    def loadInfo(self, adapter):
        self.name.set(adapter.name)
        self.ip.set(adapter.ip)
        self.ipEnabled.set(adapter.ipEnabled)
        self.subnet.set(adapter.subnet)
        self.dnsPREF.set(adapter.dnsPREF)
        self.dnsALT.set(adapter.dnsALT)
        self.dhcpEnabled.set(adapter.dhcpEnabled)
        self.defaultIPGateway.set(adapter.defaultIPGateway)


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

        self.apply = Button(changesaveframe)
        self.apply.configure(text="APPLY PRESET", height=50, width=40)
        self.apply.pack(side="right")
        self.apply.configure(activebackground="lightgreen", highlightcolor="lightblue", background="steelblue2", font=("roboto", 12), borderwidth=0, command=lambda: self.onClick(adapter, adapterid))
        self.onHover(self.apply)

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
            self.apply.configure(command=func)


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
        
        self.presetframe=Presets(self)
        self.presetframe.pack(side="left",
                              padx=2, pady=2, expand=True)

    def addAdapter(self, adapter):
        self.adapterid += 1
        self.adapterframe.addAdapters(adapter, self.adapterid)
    
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