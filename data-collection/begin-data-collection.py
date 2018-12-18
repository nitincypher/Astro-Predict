import dsoloader
import scraper
import os

#Get All the DSO Data Handlers
dsoloaders = dsoloader.load_dso_list_files()

#Merge all the arrays
#TODO: Add code block to merge all the errors

#Scrape the images
cwd = os.getcwd()
cwd = cwd + os.path.sep + "pics"
os.mkdir(cwd)
for dsoloader in dsoloaders:
    for dso in dsoloader.getObjectList():
        print(dso)
        os.mkdir(cwd+os.path.sep+dso)
        scraper.run(dso, cwd+os.path.sep+dso, 10)
#scraper.run()


