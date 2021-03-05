import csv
import pandas as pd
import numpy as np
import os.path
from os import path


print("Initial setup...")
user_one = input("Enter user one: ")
print("\nType 'q' to finish inputting values\n")

with open('netflix_n_chill.csv', mode = 'w') as netflix_n_chill:
    filewriter = csv.writer(netflix_n_chill, delimiter=',',
                                quotechar= '|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(["Movies/TV Shows", "Year"])
    filewriter.writerow([user_one])

    #add movie tv show
    tv_movie_input = input("Enter movie or TV show: ")
    year_input = input("Enter year: ")
    print("\n")
    
    while(tv_movie_input != 'q' or year_input != 'q'):

        #write user input to row
        filewriter.writerow([tv_movie_input, year_input])

        #add movie tv show
        tv_movie_input = input("Enter movie or TV show: ")
        if (tv_movie_input == 'q' or year_input == 'q'):
            print("\n")
            break
        year_input = input("Enter year: ")
        if (tv_movie_input == 'q' or year_input == 'q'):
            print("\n")
            break
        print("\n")
            
    user_two = input("Enter user two: ")
    print("\nType 'q' to finish inputting values \n")

        #add movie tv show
    tv_movie_input = input("Enter movie or TV show: ")
    year_input = input("Enter year: ")
    filewriter.writerow([user_two])
    print("\n")
    
    while(tv_movie_input != 'q' or year_input != 'q'):

        #write user input to row
        
        filewriter.writerow([tv_movie_input, year_input])

        #add movie tv show
        tv_movie_input = input("Enter movie or TV show: ")
        if (tv_movie_input == 'q' or year_input == 'q'):
            print("\n")
            break
        year_input = input("Enter year: ")
        if (tv_movie_input == 'q' or year_input == 'q'):
            print("\n")
            break
        print("\n")

#search for duplicates using pandas
print("Searching for matches...\n")
df = pd.read_csv('netflix_n_chill.csv')
#print(df.head())
duplicateRowsDF = df[df.duplicated()]

print("Matches found are: ")
print(duplicateRowsDF)



#search for duplicates using read
'''
with open("netflix_n_chill.csv", newline = '') as File:
    reader = csv.reader(File)
    for row in reader:
        print(row)
        if (row == 
'''
