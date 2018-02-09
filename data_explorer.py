# author: Molly Jacobsen
# This app explores data and tells the user information about that data
# It can be run in ubuntu using python data_explorer.py <file-path-or-url>


# import libraries
import sys
import scipy
import numpy
import matplotlib
import pandas
import sklearn
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns



def loadData(url):
    # Load the dataset
    return(pandas.read_csv(url))

def colRow():
    # Displays the amount of columns and rows in dataset
    print("Rows:", rows)
    print("Columns:", columns)

def statSummary():
    # Provide a statisical summary of data
    print("Statistical Summary: ")
    print(dataset.describe())

def firstRows():
    # Print first 20 rows of data
    print(dataset.head(20))

def createBox():
    # Create the box plots
    sns.boxplot(data=dataset)
    plt.figure(1)

def createHist():
    # Create the histograms
    dataset.hist()
    plt.figure(2)

def createScatter():
    # Create the scatter matrix
    scatter_matrix(dataset)
    plt.figure(3)

def featureType():
    # Display types of each column
    print(dataset.dtypes)

def isMissing():
    # Find out if there is any data missing
    missingList = dataset.isnull().sum().sort_values(ascending = False)
    if(missingList[0] == 0):           # Not sure how to do the boolean yet
        print("No missing data")
    else:
        print("\n\nMISSING DATA!\n\nRows of missing data from each column: ")
        print(missingList)

def displayInfo():
    colRow()
    statSummary()
    firstRows()
    featureType()
    isMissing()

def displayGraphs():
    createBox()
    createHist()
    createScatter()
    plt.show()


if(len(sys.argv)<2):
    # Error Message if dataset is not provided
    print("Error: missing dataset")
else:
    dataset = loadData(sys.argv[1])
    rows = dataset.shape[0]
    columns = dataset.shape[1]
    displayInfo()
    displayGraphs()