DS - Group 1 - Python Project : Signal Alert for Stocks

Goal :  
Give our subscribers the most accurate and relevant signals for their stocks 

System requirements are split into 4 parts: 
Registration to the program
API to one of the known/trusted stocks data brands. 
Algorithm for creating candidates of signals to be sent
API to Gmail for sending alerts 

Part Ⅰ : Registration to the program 

Registration will have 2 input values :  name, email. Taking all the user's inputs and saving them in list [email_1, email_2..]
For both name and email inputs make sure we lowercase all letters, and create a validation for the email address → aka must be in the format of “_____@__.__”. The email address accepts alphabets and integers only.
Create error messages that return  in case the email address / name  is not valid.
Create a “Thank you”message that returns if the email address and name are correct.  
Create a list of stocks we will send their signals on. 

Part Ⅱ : API to Stock’s market platform 

First brand selected is Yahoo Finance which has python API integration . 
Another brand test is : https://site.financialmodelingprep.com/developer/docs (our api key  is 4080b0c35a6df65e4b350be1d1fc841e) 
Create an account in Bloomberg to get the API key and the permissions. 
Whitelist our IPs (probably will be required by them) 
Create a list of requests we can ask from them (data, filters [by stock name, dates, changes etc] 
Test the API calls by calling the list of the stocks and save it in another dictionary that will include {datetime:{stock_name:value, stock_name:value}, datetime:{stock_name:value, stock_name:value}}. The first key is the datetime of the call GMT , another inner dict with the stock name and value. 
Calls will be every hour (if that’s too much information we can do it once a day / once in 12 hours.. ) 

Part Ⅲ : Candidates for sending as signals

The system will have a calculation formula that will decide which of the key and values from the dictionary created in part Ⅱ will be sent. 
Formula is minus the values of 2 of the same stock name, creating it to percentage . The calculation time will be immediately when new value will be added to the stocks_dict. Save the result in a variable (‘stock_diff’ for example)
Creating criteria for signals: 
if stock_diff > x% :  add to sending list 
else: don’t do anything 
Bonus :  create inner criteria for painting each difference (green: over 10%, orange: between 1-9.99%, red: lower than 5% ) 

Part Ⅳ : Gmail Integration and sending Emails

Creating gmail account  and integrating via python 
Test sending email from code 
Create a template for sending signals that will include: 
	Subject line with the name of the user + stockname + clickbait 
	Body : Hey {name},your stock {stockname} difference in the last {datetime_duration} 
	was {x%}. Thanks for using ECI signals alerts! 
Sending the alerts to the list of emails we got in Part Ⅰ
