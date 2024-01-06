# ajmera_infotech_assignment-web_scraping
# Flipkart Mobiles Web Scraping Assignment

## Introduction

This Python script performs web scraping on Flipkart's search pages to gather information about mobile phones. The script collects data such as name, ratings, color, RAM, ROM, price, currency type, processor chip, processor cores, main camera, front camera, display size, display type, and warranty.

## Prerequisites

Make sure you have the following installed:

- Python 3
- Required Python libraries: `requests`, `beautifulsoup4`

## Detailed info

i have selected 2nd problem statement which is of web scrapping from flipcart website.
in this  assignment i have wrote code that first go to flipkart page using "https://www.flipkart.com" as url and "iPhone" as query and got response.
then i have used BeautifulSoup for parsing html file that we have got in response.
then  get the values of name,price,rating and feature list from flipkart website using class name of <div> tags.
then from name i have separated color and ram of phones.
from price i have separated value and currency type('₹': 'Rupees', '$': 'Dollars', '€': 'Euros', '£': 'Pounds', '¥': 'Yen').
then from features i have separated values of display,camera,processor,warranty,rom.
then divided each columns in to multiple meaningful columns.
in display i have divided in to display size and display type.
camera is divided in to main_camera and front_camera.
processor  is divided in to processor chips and number of cores.
so that it will be easier and efficient for user of data to convineantly access the data of phones.
i have also kept no. of request to minimum so that it will be efficient and less prone to errors.
finally i have saved all information in csv format.
thank you.
