# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:45:49 2026
In this code a line graph is prodcued to show the trends in population across
six regions in the world. The pie chart and bar garph show the population for
the year 2023 which is the latest year in the dataset. The data was accessed
publicly and was cleaned into the required csv format to produce the code
@author: Mukuka Noward Mfula
"""
# importing the packages that are going to be used
import pandas as pd
import matplotlib.pyplot as plt
# define functions


def plot_bar(population, continents, filename):
    # Gives the bars distinct colour
    colours = ["red", "blue", "green", "yellow", "orange", "purple"]
    # labels for the bars
    labels = ["Africa", "Asia", "Europe", "North America", "Oceania",
              "South America"]
    # defined figure size to avoid names overlapping
    plt.figure(figsize=(10, 6))
    plt.bar(continents, population, color=colours, label=labels)
    plt.xlabel("Regions")
    plt.ylabel("Population in billions")
    plt.title("Global Population in 2023 by countries")
    plt.legend()
    plt.savefig(filename)
    plt.show()
    return
###################################################


def plot_pie(population, continents, filename):
    # to produce the figure
    plt.figure()
    plt.pie(continents, labels=population)
    plt.title("World population share in 2023")
    plt.show()
    return


##################################################
# making a dataframe for records in africa_population csv
df_africa = pd.read_csv("africa_poulation.csv")
# making a dataframe for records in asia_population csv
df_asia = pd.read_csv("asia_population.csv")
# making a dataframe for records in europe_population csv
df_europe = pd.read_csv("europe_population.csv")
# making a dataframe for records in northamerica_population csv
df_northamerica = pd.read_csv("northamerica_population.csv")
# making a dataframe for records in ocenia_population csv
df_ocenia = pd.read_csv("ocenia_population.csv")
# making a dataframe for records in southamerica_population csv
df_southamerica = pd.read_csv("southamerica_population.csv")
# making the graph at defined figure size to prevent over lapping of names
plt.figure(figsize=(10, 6))
plt.plot(df_africa["Year"], df_africa["Population"], label="Africa")
plt.plot(df_asia["Year"], df_asia["Population"], label="Asia")
plt.plot(df_europe["Year"], df_europe["Population"], label="Europe")
plt.plot(df_northamerica["Year"], df_northamerica["Population"],
         label="North America")
plt.plot(df_ocenia["Year"], df_ocenia["Population"], label="Oceania")
plt.plot(df_southamerica["Year"], df_southamerica["Population"],
         label="south america")
plt.title("Global population by region in the last 40 years")
# label years for x axis
plt.xlabel("Years")
# limiting x axis to 2024
plt.xlim(1982, 2024)
plt.ylabel("Populaion in billions")
# log is used becasue differences are huge
plt.yscale('log')
# label for years plotted outside the graph
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()
#####################################################################
year_2023 = pd.read_csv("populationpie.csv")
# the progam that is used to call the function
# the variables in the function
population_2023 = year_2023["Population"]
continents = year_2023["Name"]
# calling the function
plot_bar(population_2023, continents, "barpopulation.png")
plot_pie(continents, population_2023,"piechartpopulation.png")