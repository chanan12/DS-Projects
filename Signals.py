


##################################
# Import modules
##################################
from datetime import datetime
from distutils.log import INFO
import json
#import pyodbc
import smtplib, ssl
from email.message import EmailMessage
import re
import logging
###########################
# Logging
###########################
logging.basicConfig(filename='stocks.log', level = INFO, 
                    format='%(asctime)s:%(levelname)s:%(message)s')
###########################
# Emails
###########################


##########################
# Init param
###########################

#msg = EmailMessage()
#msg.set_content("Stock Alert")
#msg["Subject"] = "Stock Alert"
#msg["From"] = "ds@ezevin.com"
#msg["To"] = "ds@ezevin.com"
#msg["To"]  = input("Enter Email:")
#email_addr_1  = input("Enter Email:")
email_addr_1 = 'jjjsdfsdfs;idan@avronim.net'
email_list = email_addr_1.split(";")

###################################
# Check if email address is valid
###################################
check_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def check(check_email,addr):
        for addr in email_list:
            if(re.fullmatch(check_email,addr)):
               
                return True
            else:
                print('Email not valid')                        
##################################
# built email text template 
##################################
msg_text = """
the Following stock was change  :\n
Stock :'{}'\n
Old Price :'{}'\n
New Price :'{}'\n
change value:'{}'\n
date :'{}'\n
"""

context=ssl.create_default_context()

# my_file_path = " C:\\Users\\User\\Desktop\\Python_Test\\filename.txt"         
           
# def write_row(my_file_path):
#     lines = ['Readme', 'How to write text files in Python']
#     with open(my_file_path, 'w') as f:
#         f.write(lines)
#         f.write('\n')

my_file_path = r"C:\Users\Idan\Desktop\DS Course\Python Project\signals_file.txt"
               
           
def write_row(  my_file_path, 
                Stock, 
                Old_Price,
                New_Price, 
                change,
                date):
    with open(my_file_path, 'a') as f:
        c = Stock + ',' +  str(Old_Price) + ',' + str(New_Price) + ',' + str(change) + ',' + date
        f.write(c)
        f.write('\n')
        logging.info(f'{Stock} Old:{Old_Price},New:{New_Price},change:{change}')


    # print(*columns, sep='\t', end='\n', file=my_file_path)
    # ### after Email_Message
    # with open (my_file_path, "a+") as f:
    #     print(my_file_path)
    #     if header_print==False:
    #         write_row(f, 'Stock', 'Old Price', 'New Price','change value', 'date','addres')
    #         header_print=True
        

##################################
# built Email Message
##################################
def Email_Message(    Stock, 
                      Old_Price,
                      New_Price, 
                      change,
                      date,
                      addr):
    try:
         if check(check_email,addr) == True: 
                      
            msg_content = msg_text.format(      Stock, 
                                            Old_Price,
                                            New_Price, 
                                            change,
                                            date)
    
    #print('~~~~~~~~~')
    #print(msg_content)
            msg = EmailMessage()
            msg.set_content("Stock Alert")
            msg["Subject"] = "Stock Alert"
            msg["From"] = "ds@ezevin.com"
            msg["To"] = addr  

            msg.set_content(msg_content)
    except Exception as e:
        print(e)         
    ##################################
    # connect to smtp & Send message
    ##################################
        with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
            smtp.starttls(context=context)
            smtp.login(msg["From"], "AaZz1234")
            smtp.send_message(msg)
##########################
# Simple WebSocket Demo
###########################

import time

from polygon import WebSocketClient, STOCKS_CLUSTER


def my_custom_process_message(message):
    print("this is my custom message processing", message)


def my_custom_error_handler(ws, error):
    print("this is my custom error handler", error)


def my_custom_close_handler(ws):
    print("this is my custom close handler")


def main():
    key = 'TJduOIVzU16y129apFCeYoCpKWklDp4A'
    my_client = WebSocketClient(STOCKS_CLUSTER, key, my_custom_process_message)
    my_client.run_async()

    my_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    time.sleep(1)

    my_client.close_connection()


if __name__ == "__main__":
    main()

##########################
# Simple REST Demo
###########################

from polygon import RESTClient


# def main():
#     key = 'TJduOIVzU16y129apFCeYoCpKWklDp4A'

#     # RESTClient can be used as a context manager to facilitate closing the underlying http session
#     # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
#     with RESTClient(key) as client:
#         resp = client.stocks_equities_daily_open_close("AAPL", "2021-06-11")
       
#         print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")


# if __name__ == '__main__':
#     main()


#######################################
# Query parameters for REST calls
#######################################

import datetime

from polygon import RESTClient


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = 'TJduOIVzU16y129apFCeYoCpKWklDp4A'
    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        from_ = "2022-01-01"
        to = "2022-01-05"
        resp = client.stocks_equities_aggregates("AAPL", 1, "day", from_, to, unadjusted=False)
        resp2 = client.stocks_equities_aggregates("MSFT", 1, "day", from_, to, unadjusted=False)

        #print(f"Minute aggregates for {resp.ticker} between {from_} and {to}.")
        #print(type(resp.results))
        #print(resp.results)

        ##################################
        # Our Code 
        ##################################
        ##################################
        # Init Param 
        ##################################

        stocks_dict = {}
        aapl_dict ={}
        msft_dict ={}
        new_price = 1 
        change = 0
        k=[]
        old_stock = 'a'
        i=0 

        for result in resp.results:
            dt = ts_to_datetime(result["t"])
            #print(f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} ")
            aapl_dict[dt] = result['c'] 
        
        stocks_dict[resp.ticker] =  aapl_dict

        for result in resp2.results:
            dt = ts_to_datetime(result["t"])
            #print(f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} ")
            msft_dict[dt] = result['c'] 
        stocks_dict[resp2.ticker] =  msft_dict
        
        #print(main_dict1) 
        
        for stock in stocks_dict:
            for dt, price in stocks_dict[stock].items():

                ######################################
                ## get first price for each stock 
                ######################################
                if old_stock != stock:
                    ##print ('---1 > ', old_stock, stock)
                    old_stock = stock
                    ######################################
                    # List Comprehension
                    # get first price for each stock 
                    ######################################
                    list1 =  [(k) for k in stocks_dict.values()]
                    list2 =  [(k) for k in list1[i].values()]
                    new_price = (list2[0])
                    i+=1

                    #print('--- > ', new_price)
                ######################################
                ## case there is change in the price 
                ######################################
               
                if new_price != price :
                    change = (price/new_price) -1   
                    #print('change -> ', change , 'current price-> ', price , 'old price',  new_price)    
                    old_price = new_price
                    new_price = price 
                    if abs(change) > 0.000003:
                        #print('change -> ', change , 'current price-> ', price , 'old price',  old_price) 
                        #write_row(my_file_path)
                        write_row(  my_file_path, 
                                    stock, 
                                    old_price,
                                    price, 
                                    change,
                                    dt)  
                        for addr in email_list:
                            print (addr)
                        # def check(addr):
                        #     if(re.fullmatch(check_email, addr)):
                            ##################################
                            # send messages
                            ##################################
                            Email_Message(  stock, 
                                            old_price,
                                            price, 
                                            change,
                                            dt,
                                            addr)
                                # else:
                                #     print("Invalid Email")   
                
                    
        #print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
        #print(dict2) 

if __name__ == '__main__':
    main()
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 
    print('work')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~') 

