import tkinter as Tk
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import countryGUI
import mlSandbox
import GuiOption

class Historic3DGui(countryGUI.CountryGui):
    
    def __init__(self, country_data):
        self.options3d = {}
        self.options3d[1] = GuiOption.Option("Population", "pop")
        self.options3d[2] = GuiOption.Option("GDP per Capita", "gdpPercap")
        self.options3d[3] = GuiOption.Option("Life Expectancy", "lifeExp")

        super().__init__(country_data, None, "year")
    
    def plotData(self):
        
        ax = plt.axes(projection ="3d") 
        ax.set_xlabel(self.xAxisName)
        ax.set_ylabel(self.options3d[2].displayName)
        ax.set_zlabel(self.options3d[3].displayName)
        plt.title(" Time, Gdp Per Capita, and Life Expectancy 3D")
            
        for country in self.countryContainer:
            country = self.dataFrame.loc[country]
            xData = list(country[self.xAxisName])
            yData = list(country[self.options3d[2].pandasName])
            zData = list(country[self.options3d[3].pandasName])
            ax.scatter3D(xData, yData, zData, cmap = 'hsv', label = country.index[0])
                
        plt.legend(loc = "upper left")  
        plt.show()

def main():
    country_data = mlSandbox.getCountryData()
    gui = Historic3DGui(country_data)

if __name__ == "__main__":
    main()
