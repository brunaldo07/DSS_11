import json 
import matplotlib.pyplot as plt
import numpy as np

# Visualize the results using a bar plot visualization in Python.

with open('numbers.json') as json_file:
    data = json.load(json_file)
    parse = data.replace("[","").replace("]","")
    parse = data.split(",")
    toarr = np.array(parse)
    plt.hist(toarr, bins=50)
    plt.gca().set(title='Frequency Histogram', ylabel='Frequency');