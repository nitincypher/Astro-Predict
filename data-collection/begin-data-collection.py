import dsoloader
import scraper
import os

#Get All the DSO Data Handlers
dsoloaders = dsoloader.load_dso_list_files()

#Merge all the arrays
#TODO: Add code block to merge all the errors

#Scrape the images
for dsoloader in dsoloaders:
    for dso in dsoloader.getObjectList():
        print(dso)
        scraper.run(dso, "C:\nitin\astro-predict\pics", 10)
#scraper.run()


