import mlSandbox
import tkinter as Tk
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class GUI:
    
    def __init__(self, countries, country_data):
        self.root = Tk.Tk()
        self.root.geometry("300x300")
        
        self.pick = Tk.StringVar()
        self.pick.set(countries[0])
        self.options = Tk.OptionMenu(self.root, self.pick, *countries)

        self.graphPick = Tk.IntVar()
        self.graphPick.set(1)
        self.rad1 = Tk.Radiobutton(self.root, text= "Population", variable = self.graphPick, value = 1)
        self.rad2 = Tk.Radiobutton(self.root, text= "gdpPercap", variable = self.graphPick, value = 2)
        self.rad3 = Tk.Radiobutton(self.root, text= "Life Expectancy", variable = self.graphPick, value = 3)
        
        self.country_data = country_data
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
        self.rad1.pack()
        self.rad2.pack()
        self.rad3.pack()
        self.plotButton.pack()
        self.Label.pack()
        self.listBox.pack()
        
        Tk.mainloop()
    
    def plotData(self):
        fig = plt.figure()
        if self.graphPick.get() == 1:
            
            plt.xlabel("years")
            plt.ylabel("pop")
            plt.title("Population vs Time")
            
            for country in self.countryContainer:
                country = self.country_data.loc[country]
                xData = list(country["year"])
                yData = list(country["pop"])
                plt.plot(xData, yData, 'o', label = country.index[0])
               
        elif self.graphPick.get() == 2:

            plt.xlabel("years")
            plt.ylabel("gdpPercap")
            plt.title("Income vs Time")
            
            for country in self.countryContainer:
                country = self.country_data.loc[country]
                xData = list(country["year"])
                yData = list(country["gdpPercap"])
                plt.plot(xData, yData, 'o', label = country.index[0])
                 
        else:

            plt.xlabel("years")
            plt.ylabel("lifeExp")
            plt.title("Life Expectancy vs Time")
            
            for country in self.countryContainer:
            
                country = self.country_data.loc[country]
                xData = list(country["year"])
                yData = list(country["lifeExp"])
                plt.plot(xData, yData, 'o', label = country.index[0])

        plt.legend(loc = "upper left")  
        plt.show()

    def addCountry(self):
        pickLocal = self.pick.get()
        if pickLocal not in self.country_data.index or pickLocal in self.countryContainer:
                return

        self.countryContainer.add(pickLocal)
        self.listBox.insert(Tk.END, pickLocal)
    
    def clearCountries(self):
        self.countryContainer.clear()
        self.listBox.delete(0, Tk.END)

def main():
    country_data = mlSandbox.getCountryData()
    country_list = list(set(country_data.index.values))
    country_list.sort()
    gui = GUI(country_list, country_data)

if __name__ == "__main__":
    main()

