import tkinter as Tk
import HistoricDataGUI
import covidGUI
import os

class MainMenu:

    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("Select the Data To View")
        self.buttonFrame = Tk.Frame(self.root)
        self.covidButton = Tk.Button(self.buttonFrame, text = "Covid Data", command = self.callCovid)
        self.historicButton = Tk.Button(self.buttonFrame, text = "Historic Data", command = self.callHistoric)

        self.dir = os.path.dirname(__file__)
        
        self.covidButton.pack(side = Tk.LEFT)
        self.historicButton.pack(side = Tk.LEFT)
        self.buttonFrame.pack()

        Tk.mainloop()

    def callCovid(self):
        os.chdir(self.dir)
        os.system("python coivdGUI.py")
    
    def callHistoric(self):
        os.chdir(self.dir)
        os.system("python HistoricDataGUI.py")

def main():
    mainMenu = MainMenu()

if __name__ == '__main__':
    main()

