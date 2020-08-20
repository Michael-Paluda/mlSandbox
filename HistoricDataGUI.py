
import tkinter as Tk
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import countryGUI
import mlSandbox
import GuiOption

class HistoricGui(countryGUI.CountryGui):
    
    def __init__(self, country_data):
        options = {}
        options[1] = GuiOption.Option("Population", "pop")
        options[2] = GuiOption.Option("GDP per Capita", "gdpPercap")
        options[3] = GuiOption.Option("Life Expectancy", "lifeExp")

        super().__init__(country_data, options, "year")

def main():
    country_data = mlSandbox.getCountryData()
    gui = HistoricGui(country_data)

if __name__ == "__main__":
    main()

