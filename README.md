# SNP Search Project - WebDev Project - M2 DLAD

## About this project 

This project was done in the purpose of a course project for a web development and database management course at the University of Aix-Marseille M2-DLAD. 
The project is **temporarily** available at: http://snpproject-georgealehandro.pythonanywhere.com/.
## Purpose
The goal of this project is to create a website that allows for an interactive search for Single Nucleotide Polymorphisms **SNPs** from a database in a Django-based web framework.  
The user should also be able to search for **Phenotypes** (aka. traits) and the SNPs related to each one of them.  
Additionally we provide the user the possibility to search by genes, to plot meaningful figures and to interactively move between the different pages.  
## Homepage
#### A carousel showcasing the different functionalities of the website, brought to you by Bootstrap.  

![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/homepage1.PNG)

#### Cards with a little bit more info, also from Bootstrap.

![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/homepag2.PNG)

##  SNP search
Search SNPs by rsid or by chromosome and positions.


![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/snp_search.PNG)

#### The results will be fetched and displayed by serverside datatable search.  


![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/snp_datatable1.png)

#### Clicking on a certain rsid will bring you to the association datatable.  


![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/snp_datatable2.png)

#### The user may generate statistics around the distribution of the traits related to a certain rsid.


![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/snp_stats.PNG)

#### Full action:

![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/gif/snp_stats.gif)

##  Trait search
#### Search name or display the full list and choose.


![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/traits_table.PNG)

#### The results will be fetched and displayed by serverside datatable search.  


![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/traits_datatable.PNG)
  

#### The user may generate statistics around the distribution of -logPvalue of association score between all the SNPs and a certain trait.  


![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/traits_stats.PNG)

#### Full action:

![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/gif/disease_stats.gif)

## Genes search
#### By heading over to the **genes** page and searching for the target gene, powered by auto-complete and datatable.

## Diverse functionalities
### Login
![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/login.PNG)
#### In order to contribute to our database:
![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/contribute.PNG)
### Docs
![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/docs.PNG)
### References
![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/references.PNG)


### Database Architecture

![Alt Text](https://github.com/GeorgeAlehandro/snpProject/blob/master/screenshots/db.png)
## Requirements
Please refer to requirements.txt for the packages used for this project on Python 3.9.
## Server versions
One local dev-version with debug On.  
A temporary online version hosted at pythonanywhere on the following link:  
#### http://snpproject-georgealehandro.pythonanywhere.com/
