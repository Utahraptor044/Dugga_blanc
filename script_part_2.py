import sys
import pandas as pd
import csv
import argparse

#### exo a.
# recover a csv file with argparse, create an argument
# ask to recover the file

parser = argparse.ArgumentParser(description="Read a csv file and print its statistics")

# Demande de récupérer le script convoité
parser.add_argument('file', help="Choose a csv file to analyse")

# Encode its value
args = parser.parse_args()

# Read the csv file, and copy it into a variable that make it usable later
with open(args.file, "r", newline ='', encoding='latin-1') as file:
    reader = csv.reader(file, delimiter = ",")
    # create a variable that recover all of the data
    data = list(reader)


# Create the pandas dataframe
df = pd.DataFrame(data)

for col in df.columns[6:8]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

#pd.to_numeric try to convert each value into an int for the 7th and 8th column. Get by AI

print("Contenu du fichier :")
print(df)

print("\nRésumé statistique :")
print(df.describe())

###############################"
# ###"exo b.

print(df.columns.tolist())
# The wanted column is the 8
# sort the data
sorted_df = df.sort_values(7, axis = 0, ascending = False, inplace = False)

head_data = sorted_df.head(n = 20)
# The subset dataframe is in head_data

print("20 firsts rows :")
print(head_data)

######################################""
### exo c.

from plotnine import ggplot, aes, geom_point, ggtitle, xlab, ylab, geom_smooth, theme, element_text

import matplotlib.pyplot as plt
import numpy as np


# Vérifier que les colonnes sont numériques
for col in [6, 7]:
    head_data[col] = pd.to_numeric(head_data[col], errors="coerce")

# Enlever les lignes sans valeurs numériques
plot_data = head_data.dropna(subset=[6, 7])

#create an empty figure
plt.figure(figsize=(8, 6))
# Create the datas. 
plt.scatter(plot_data[0], plot_data[6], color='blue', marker='o', label="TPM unstranded")
plt.scatter(plot_data[0], plot_data[7], color='red', marker='x', label="FPKM unstranded")
plt.title("Comparition between two normalisation methods :\n TPM (transcript per milion) and FPKM (Fragment per Kilobase Milion)")
plt.xlabel("Gene name")
plt.ylabel("Per milions")
# Créé une légende avec les deux séries
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
# Fais pivoter les labels de 90° pour plus de visibilité
plt.xticks(rotation=90, ha='right')
plt.savefig("mon_graphique.png", dpi=150, bbox_inches="tight")

#############################################
### exo d.

#a title, the x- and y-labels are already added to the plot
# Easy to read if want to compare each method for each gene. 