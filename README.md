
# Data Visualisation Dashboard using InteractiveWebGL WebApp

The fast expansion of urbanization and the vehicle populace has brought about expanded number of accidents allover the world. According to World Health Organization (WHO) nearly 1.25 million people die in road crashes each year, onaverage, 3,287 deaths a day. Road safety has become a primary concern for most of the nations as it can be controlled and the number of disasters can be reduced. As human beings,it is ourresponsibility to be cautious of our surroundings and use science,knowledge and all the past experience to solve this problem. Thus, the objective of our project is to analyze and visualize the accidents that have occurred over the past few years in Canada and extract patterns from it. 
This repository cotains the code and the dataset used in our final project for the course MM 804 Computer Graphics and Animation. Our goal was educate the common people and help the officials about the possible accidents.
## Dataset
We  have  used  a  publically  avaiable  dataset  provided  by Transport  Canada   and  Statistics  Canada available  on Kaggle [https://www.kaggle.com/tbsteal/canadian-car-accidents-19942014]  of car accidents in Canada from 1994-2014. There are  22  features  with  a  total  of  5.8  million  data  points.  Some of the features in the data set are : Time of the day, Fatalities/Non  Fatalities,  Road  Configuration,  Driver  Details,  Weather Configuration. All  the  features  are  a  categorical  variable  withsome  features  comprising  of  2  categories  and  a  few  featureshaving  categories  greater  than  20. Since  the  data  was  too large  for  visualization,  we  reduced  the  time  period  to  be between 2004 - 2014 thus reducing the number of data points considerably. The data available was dirty and required a fair bit of pre-processing in order to be used for visualization. <br>
*Note:If you update the dataset keep the file name same as dataset.zip.*

## Project

The project is divided into three main components or modules
1. Backend
2. Website
3. CCrazy Ccops Unity Game

### Backend
____________________________________________________________________________________________________
The backend of the project is built up on Django REST Framework
Prerequists
```
python==3.6
pip==20.0.2
```

Install requirements.txt using the following command
```
pip install -r requirements.txt
```
Once all the requirements are installed
Navigate to the folder caraccidents which has manage.py and run the following commands
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver <your-ip-address>:<port-number>
```

### Frontend
____________________________________________________________________________________________________
The frontend of the project is built using alot of languages like Angular JS, HTML, CSS, Javascript, JQuery
Prerequists
```
Apache Web Server
```
Once you have installed the Apache Web Server move all the files in the www/html folder follow the steps mentioned below
https://github.com/mgechev/angular-seed/wiki/Deploying-prod-build-to-Apache-2


### CCrazy CCops
__________________________________________________________________________________________________________
The crazy cops game is built using Unity, Web GL, Cannon JS, Three JS
We have integrated the CCrazy CCops Game with the website so once you follow the above steps for hosting the website the game will get hosted automatically.
Once the website is hosted it will first redirect you to the game and then you can navigate the city and checkout the graphs.

#### Authors:

| Name | github handle |
| ---- | ------ |
| Jatin Dawar | [@jatin008](https://github.com/jatin008) |
| Prem Raheja     | [@prem1409](https://github.com/prem1409) |
| Utkarsh Vashisth     | [@uvashisth](https://github.com/uvashisth) |
| Vaibhav Rakheja| [@vaibhavrakheja11](https://github.com/vaibhavrakheja11 )|
