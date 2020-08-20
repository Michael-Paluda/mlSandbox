import mlSandbox
import tkinter as Tk
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import GuiOption
import countryGUI

class CovidGui(countryGUI.CountryGui):
    
    def __init__(self, country_data):
        options = {}
        options[1] = GuiOption.Option("New Cases", "new_cases")
        options[2] = GuiOption.Option("New Deaths", "new_deaths")

        country_data.loc[:, 'date'] = pd.to_datetime(country_data['date'], format='%Y-%m-%d')

        super().__init__(country_data, options, "date")

def main():
    
    covid_data = mlSandbox.getCovidData()
    gui = CovidGui(covid_data)

if __name__ == "__main__":
    main()

