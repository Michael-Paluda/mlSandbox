import mlSandbox
import tkinter as Tk
import pandas as pd
import os
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


if __name__ == '__main__':
    covidData = mlSandbox.getCovidData()
    popData = mlSandbox.getPopData()