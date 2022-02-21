# Capstone - final project from the Data Analytics Bootcamp at [neuefische GmbH](https://www.neuefische.de/weiterbildung/data-analytics)

## __Clean Data - Clean Cars__
__Data driven decision making for small businesses__

Developing a tool in the form of a dashboard in Tableau to help small sized businesses to make data-driven business decisions. In this example where to build the next carwash, as an case for a small business

<img src="./data/carwash.png" width=75% height=50%>

___

#### __Table of Contents__


  - [Weather KPIs](#weather-kpis)
  - [Traffic KPIs](#traffic-kpis)
  - [Socio Demographic KPIs](#socio-demographic-kpis)
  - [Points of Interest KPIs](#points-of-interest-kpis)
  - [Ranking Formula](#ranking-formula)


## Weather KPIs

__Data Source:__ Meteostat API (daily Point data) <br>

__Data timespan:__ January 2017- December 2021


* #### __Snow Days per year:__ <br>
  - average snow days aggregated over 5 years
  - a day counts as a snow day when there is snow fall of more than 0mm 
  - smaller numbers are better
  - reasoning: the assumed likelihood of washing your car on a day when it is snowing is 		   	very small (the ranking assumes that the likelihood is 0)

<br>

+ #### __Rain Days per year:__ <br>
  - average rain days aggregated over 5 years
  - a day counts as a rain day when there is a precipitation total ofmore than 2.5mm a day
  - smaller numbers are better
  - reasoning: the assumed likelihood of washing your car on a daywhen it is raining is very 		small (the ranking assumes thatthe likelihood is 0)

<br>

* #### __Sun-hours per day:__ <br>
	- average sun-hours aggregated over 5 years
	- higher numbers are better
	- reasoning: the assumed likelihood of washing your car rises with good weather (similar to 	the “spring cleaning”
 
 <br>

* #### __Avg. temperature:__ <br>
	- measure unit: degrees Celsius
	- average daily temperature aggregated over 5 years
	- higher numbers are better
	- reasoning: the assumed likelihood of washing your car on a day when it is warm is higher 	than on a day when it is cold (and when it is near freezing or freezing it is assumed to be 0)


## Traffic KPIs

__Data Source:__ tomtom Traffic Stats API
- based on tomtom historic data <br>
- Traffic Area Data
- uses GPS location data from non-professional regular drivers

__Data timespan:__ January 1, 2021 - January 31, 2021

We used area data to gather the traffic density and harmonic average speeds on each street in all our five cities.
The streets are separated into segments which are created by: 
- change of speed limit
- change of street name
- crossing of city borders
- change of house number format <br>


**➡️** We aggregated the street segments and built averages for the harmonic average speed and the unique car count.

<br>

* #### __Harmonic average speed:__ <br>
  - measure unit: km/h
  - average speed on all of the relevant streets (aggregated over one month)
  - relevant streets are all streets where cars are allowed to drive
  - lower numbers are better
  - reasoning: the assumed likelihood of seeing a carwash and/or deciding to take a turn 			into a carwash rises with lower speeds

<br>

* #### __Traffic Density:__ <br>
	- average unique cars per relevant street (aggregated over one month)
	- relevant streets are all streets where cars are allowed to drive
	- higher numbers are better
	- reasoning: the assumed likelihood of a car taking a turn into a carwash rises with higher 		number of cars on the streets, it also shows the availability of possible customers


## Socio Demographic KPIs

__Data Source:__ statista, wikipedia, KBA (Kraftfahrt-Bundesamt), Agentur für Arbeit, UrbiStat, suche-postleitzahl.org (OpenStreetMap contributors)
 
 <br>

* #### __Population-density:__ <br>
	- measure unit: people/km²
	- AdminStat Data from 2019 (population), 
	- OpenStreetMap Data from 2022 (city size)
	- higher numbers are better
	- reasoning: general information about the city

<br>

* #### __Income per capita:__ <br>
	- measure unit: €
	- wikipedia (Statistisches Bundesamt) 2018
	- higher numbers are better
	- reasoning: the assumed likelihood of washing a car rises with the availability of money to 		spend on such things
	- reasoning to why income per capita instead of GDP per capita: the GDP per capita is 			more prone to being skewed by commuters and therefore has less of validity for prosperity 	than the income per capita

<br>

* #### __Unemployment rate:__ <br>
  - relation between unemployed and employed in %
  - data source? 
  - lower numbers are better
  - reasoning: the assumed likelihood of washing a car rises with the availability of money 		which decreases with a higher number of unemployed
 
 <br>

* #### __Unemployment rate:__ <br>
  - relation between unemployed and employed in %
  - data source? 
  - lower numbers are better

    __reasoning:__ the assumed likelihood of washing a car rises with the availability of money 		which decreases with a higher number of unemployed

<br>

* #### __Cars per capita:__ <br>
  - KBA data 2021
  - Bestand an Kraftfahrzeugen und Kraftfahrzeuganhängern nach Zulassungsbezirken
  - higher numbers are better:

    __reasoning:__ general information about the city (more cars = more possible customers)

## Points of Interest KPIs

__Data Source:__ tomtom places API

__Data date:__ February 2022

<br>

* #### __Negatively influencing Places:__ <br>

  - **Competitors** (existing carwashes In postal code)
    - absolute number of carwashes in postal code
    - lower numbers are better <br>

    <br> __reasoning:__ the assumed likelihood for cars to chose your carwash decreases with higher 		amount of competition in the designated area

<br>

* #### __Positively influencing Places:__ <br>
  

  - **Car Rentals:**
	- absolute number of car rentals in postal code
	- higher numbers are better

    <br> __reasoning:__ car rentals need a place to clean their cars after renting them out, if your 			carwash is located in close proximity to a car rental place it is likely they will clean their 			cars at your place


   - **Car Dealers:**
    	- absolute number of car dealers in postal code
    	- higher numbers are better

        <br> __reasoning:__ car dealers need a place to clean their cars to show them off and after test 			drives, if your carwash is located in close proximity to a car rental place it is likely they will 		clean their cars at your place

  - __Gas Stations:__
	- absolute number of gas stations in postal code
	- higher numbers are better

    <br> __reasoning:__ car owners are used to seeing a carwash directly at a gas station, so they will 		assume that they can find one there, also gas stations are frequently visited places for car 		owners and a carwash could benefit off of that

## Ranking Formula

The ranking is based on following criteria:
* Weather KPI
* POI KPI
* Traffic KPI
* Additional information (socio demographic data)

__The weighting of each criteria__ <br>
The criteria are standardised via assigning points (higher number = better) so they can be put inside of a formula. <br>
The standardised points rank from 0 to 10.

The weighting happens via an input by the user from 0 - 100%. This input will be transformed to a decimal in order to use it inside of the formula.
The sum of the weighting inputted by the user should always equal 100%. Else the data will not be showing correct numbers and the tool will let you know what is wrong.

<br>

**The formula looks like this:** <br>
**P** = WP * WW + SDP * SDW + ASP * ASW + TDP * TDW + BPP * BPW + CPP * CPW

<br>

---
__Acronyms:__ <br>
P = Points <br>
WP = Weather Points <br>
WW = Weather Weighting <br>
SDP = Socio-Demographic Points <br>
SDW = Socio-Demographic Weighting <br>
ASP = Average Speed Points <br>
ASW = Average Speed Weighting <br>
TDP = Traffic Density Points <br>
TDW = Traffic Density Weighting <br>
BPP = Beneficial Places Points (these consist of: Gas Stations, Car Rentals, Car Dealers and are grouped by default) <br>
BPW = Beneficial Places Weighting <br>
CPP = Compromising Places Points (these consist of: Carwashes and are grouped by default) <br>
CPW = Compromising Places Weighting <br>

---

### __Example 1:__ (user inputs weightings)
P = WP * 5% + SDP * 5% + ASP * 30% + TDP * 30% + BPP * 15% + CPP * 15%

### **->** Translates in the backend to: <br>
P = (WP * 0.05 + SDP * 0.05 + ASP * 0.3  + TDP * 0.3% + BPP * 0.15 + CPP * 0.15) * 10


The following factors that resemble the standardised points are standardised by us and cannot be changed by the user. The user can only change the weighting of the standardised points.
The factors are:

<br>

**Weather Points** consisting of the criteria inside the weather KPI as mentioned in Part1. <br>

They are weighted as follows: <br>
Snowdays = 34%, Raindays = 22%, Sunhours = 22%, Average Temperature = 22%

**Socio-Demographic Points** consisting of the criteria inside the Socio Demographic KPI as mentioned in Part1.

They are weighted as follows: <br>
Cars per Capita = 30%, Income per Capita = 30%, Population Density = 20%, Unemployment Rate = 20%





<br>





#### Team
- [Evans Witte](https://github.com/evanswitte)
- [Pascal Sommer](https://github.com/passom)
- [Andre Kiehm](https://github.com/AndreK1992)
- [Jan Fernando Bohlmann](https://github.com/janb89)
