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
        self.plotButton = Tk.Button(self.root, text = "Plot Data", command = self.plotData)
        self.addButton = Tk.Button(self.root, text = "Add Country", command = self.addCountry)
        
        self.options.pack()
        self.rad1.pack()
        self.rad2.pack()
        self.rad3.pack()
        self.plotButton.pack()
        self.addButton.pack()
        Tk.mainloop()
    def plotData(self):
        
        for country in self.countryContainer:
            
            country = self.country_data.loc[country]
            xData = list(country["year"])
            fig = plt.figure()
            plt.xlabel("years")

            if self.graphPick.get() == 1:
                yData = list(country["pop"])
                plt.ylabel("pop")
                plt.title("Population vs Time")
            
            elif self.graphPick.get() == 2:
                yData = list(country["gdpPercap"])
                plt.ylabel("gdpPercap")
                plt.title("Income vs Time")
            else:
                yData = list(country["lifeExp"])
                plt.ylabel("lifeExp")
                plt.title("Life Expectancy vs Time")

            plt.plot(xData, yData, 'o')
        plt.show()
    def addCountry(self):
        pickLocal = self.pick.get()
        if pickLocal not in self.country_data.index:
                return

        self.countryContainer.add(pickLocal)

def main():
    country_data = mlSandbox.getCountryData()
    country_list = list(set(country_data.index.values))
    country_list.sort()
    gui = GUI(country_list, country_data)

if __name__ == "__main__":
    main()

