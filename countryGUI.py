import mlSandbox
import tkinter as Tk
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import GuiOption

class CountryGui:

    def __init__(self, countries, options, xAxisName):
        self.root = Tk.Tk()
        self.root.geometry("300x300")
        self.xAxisName = xAxisName
        
        self.pick = Tk.StringVar()
        self.pick.set(countries[0])
        self.optionsMenu = Tk.OptionMenu(self.root, self.pick, *countries)
        self.options = options

        self.graphPick = Tk.IntVar()
        self.graphPick.set(1)
        self.radButtons = []
        for key in self.options:
            self.radButtons.append(Tk.Radiobutton(self.root,text = self.options[key].displayName, variable = self.graphPick, value = key))
        
        self.dataFrame = dataFrame
        self.countryContainer = set([])
        self.buttonFrame = Tk.Frame(self.root)
        self.plotButton = Tk.Button(self.root, text = "Plot Data", command = self.plotData)
        self.addButton = Tk.Button(self.buttonFrame, text = "Add Country", command = self.addCountry)
        self.clearButton = Tk.Button(self.buttonFrame, text = "Clear Countries", command = self.clearCountries)
        self.Label = Tk.Label(self.root, text = "Countries To Display Below")
        self.listBox = Tk.Listbox(self.root)
        
        self.options.pack()
        self.buttonFrame.pack()
        self.addButton.pack(side = Tk.LEFT)
        self.clearButton.pack(side = Tk.RIGHT)
        for rad in self.radButtons:
            rad.pack()
        self.plotButton.pack()
        self.Label.pack()
        self.listBox.pack()
        
        Tk.mainloop()
    
    def plotData(self):
        fig = plt.figure()
        
        pickLocal = self.graphPick.get()
        displayName = self.options[pickLocal].displayName
        pandasName = self.options[pickLocal].pandasName
          
        plt.xlabel(xAxisName)
        plt.ylabel(displayName)
        plt.title("{} vs {}".format(displayName, xAxisName))
            
        for country in self.countryContainer:
            country = self.dataFrame.loc[country]
            xData = list(country[xAxisName])
            yData = list(country[pandasName])
            plt.plot(xData, yData, 'o', label = country.index[0])
               
        plt.legend(loc = "upper left")  
        plt.show()

    def addCountry(self):
        pickLocal = self.pick.get()
        if pickLocal not in self.dataFrame.index or pickLocal in self.countryContainer:
                return

        self.countryContainer.add(pickLocal)
        self.listBox.insert(Tk.END, pickLocal)
    
    def clearCountries(self):
        self.countryContainer.clear()
        self.listBox.delete(0, Tk.END)