# ajmera_infotech_assignment-web_scraping
i have selected 2nd problem statement which is of web scrapping from flipcart website.
in this  assignment i have wrote code that first go to flipkart page using "https://www.flipkart.com" as url and "iPhone" as query and got response.
then i have used BeautifulSoup for parsing html file that we have got in response.
then  get the values of name,price,rating and feature list from flipkart website using class name of <div> tags.
then from name i have separated color and ram of phones.
from price i have separated value and currency type('₹': 'Rupees', '$': 'Dollars', '€': 'Euros', '£': 'Pounds', '¥': 'Yen').
then from features i have separated values of display,camera,processor,warranty,rom.
then divided each columns in to multiple meaningful columns.
i have also kept no. of request to minimum so that it will be efficient and less prone to errors.
finally i have saved all information in csv format.
thank you.
