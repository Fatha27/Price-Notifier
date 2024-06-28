from bs4 import BeautifulSoup
import requests
import smtplib
import ssl
from email.message import EmailMessage
import random
import pymongo
import datetime
from time import sleep
# MongoDB Atlas connection string
connection_string = "MongoDB String"

# Create a MongoClient object
client = pymongo.MongoClient(connection_string)

# Access a specific database
db = client['test']

# Access a specific collection
collection = db['stocks']


def delete_document_by_field(field_name, field_value):
    query = {field_name: field_value}
    result = collection.delete_one(query)
    if result.deleted_count == 1:
        print("Document deleted successfully.")
    else:
        print("Document not found.")    

def emc(symbol,minprice,maxprice,price):
    sender="scraptivists@gmail.com"
    password="Password"
    if price<minprice and price<maxprice:
        subject = f"Price drop Alert - {symbol} !!"	
        body=html_content = f"""<html><body> <p>Dear Customer,We're excited to inform you that the price of <b>{symbol}</b>  has dropped to <b>{pricec}</b> .<br>This is a limited-time offer that you wouldn't want to miss.</p><ul><li>Stock/Cryptocurrency: <b>{symbol}</b></li><li> Target Price: <b>{minprice}</b></li>\n</ul><p style="text-align: center;">Take advantage of this reduced price and secure your <b>{symbol}</b> today.</p>		
        <p style="text-align: center;">Thank you for choosing us. We look forward to serving you again.</p>	
        <p>Best regards,<br><b>Price Notifier</b></p>	
        </body>	
        </html>	
        """
    elif price>maxprice and price>minprice:
        subject = f"Price rise Alert - {symbol} !!"	
        body=html_content = f"""<html><body> <p>Dear Customer,We're excited to inform you that the price of <b>{symbol}</b>  has risen to <b>{pricec}</b> .<br>This is a limited-time offer that you wouldn't want to miss.</p><ul><li>Stock/Cryptocurrency: <b>{symbol}</b></li><li>Target Price: <b>{maxprice}</b></li>\n</ul><p style="text-align: center;">Take advantage of this reduced price and secure your <b>{symbol}</b> today.</p>		
        <p style="text-align: center;">Thank you for choosing us. We look forward to serving you again.</p>	
        <p>Best regards,<br><b>Price Notifier</b></p>	
        </body>	
        </html>	
        """         
    emc=EmailMessage()
    emc['From']=sender
    emc['To']=receiver
    emc['Subject']=subject
    emc.set_content(body)
    emc.add_alternative(html_content,subtype="html")
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,emc.as_string())
    #delete_document_by_field('Symbol',Stock)
def crypto():
    print(pricec.replace(',',''))


cursor=collection.find({})
for document in cursor:
    print(document)
    start_date=document["time"]
    start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
    days=document["noofdays"]
    if days != None:
            # Calculate the end date by adding the specified number of days to the start date
        end_date = start_date + datetime.timedelta(days=int(days))
             # Get the current date
        current_date = datetime.datetime.now().date()
        if (current_date > end_date):
                delete_document_by_field('noofdays', days)
        # Compare the current date with the end date
    if (days == None) or (current_date <= end_date) :
        sleep(random.randint(5,10))
        Stock=document["Symbol"]
        maxprice=document["maxPrice"]
        minprice=document["minPrice"]
        URL=f'https://finance.yahoo.com/quote/{Stock}?p={Stock}' 
        receiver=document["Email"]
        headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
        page=requests.get(URL, headers=headers) 
        soup1=BeautifulSoup(page.text,"html.parser")
        if 'yahoo' in URL:
            symbol=soup1.find('h1',class_={'D(ib) Fz(18px)'}).text
            pricec=soup1.find('fin-streamer', class_={'Fw(b) Fz(36px) Mb(-4px) D(ib)'}).text
            print(f'pricec{pricec}')
            price=float(pricec.replace(',',''))
            print(symbol.strip())
            crypto()
        ## email ##
        if price < minprice or price > maxprice:
            emc(symbol,minprice,maxprice,price)
        else:
            pass
    else:
        print("skipped doc")
        pass
    
    # Close the connection
client.close()