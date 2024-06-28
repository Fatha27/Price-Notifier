from bs4 import BeautifulSoup
import requests
import time
import smtplib
import ssl
from email.message import EmailMessage
import random
import pymongo
import datetime
from time import sleep
# MongoDB Atlas connection string
connection_string ="MongoDB String "

# Create a MongoClient object
client = pymongo.MongoClient(connection_string)

# Access a specific database
db = client['test']

# Access a specific collection
collection = db['prods']

def delete_document_by_field(field_name, field_value):
    query = {field_name: field_value}
    result = collection.delete_one(query)
    if result.deleted_count == 1:
        print("Document deleted successfully.")
    else:
        print("Document not found.")    
#function for sending emails
def em(prod,price,URL):
    sender="scraptivists@gmail.com"
    password="Password"
    subject = f"Price drop Alert - {prod} !!"
    body=html_content = f"""<html><body> <p>Dear Customer,We're excited to inform you that the price of <b>{prod}</b>  has dropped to <b>{price}</b> .<br>This is a limited-time offer that you wouldn't want to miss.</p><ul><li>Product: <b>{prod}</b></li><li>Price: <b>{price}</b></li>\n</ul><p style="text-align: center;">Take advantage of this reduced price and secure your <b>{prod}</b> today.</p>
    <div style="text-align: center;"> <a href=" {URL}" style="display:inline-block; background-color: #007bff; color: #fff; padding: 10px 20px;text-decoration: none; border-radius: 4px;">Click here</a></div>
    <p style="text-align: center;">Thank you for choosing us. We look forward to serve you again.</p>
    <p>Best regards,<br>Price Notifier</p>
    </body>
    </html>
    """
            
    em=EmailMessage()
    em['From']=sender
    em['To']=receiver
    em['Subject']=subject
    em.set_content(body)
    em.add_alternative(html_content, subtype="html")
    context=ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
        smtp.login(sender,password)
        smtp.sendmail(sender,receiver,em.as_string())
    #delete_document_by_field('Link', URL)
### amazon ###
def amazon():
   print('₹',pricea.replace(',','').replace('.',''))

   ##  flipkart  ###
def flipkart():
   print('₹',pricef.replace(',','').replace('₹',''))
   
def snapdeal():
   print('₹',pricesd)

def shopprint():
   print('₹',pricea.replace(',','').replace('.',''))
   ##  crypto ###

def nykaaprint():
   print(pricea.replace(',','').replace('.',''))


cursor=collection.find({})
for document in cursor:
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
            sleep(random.randint(5,20))
            URL=document["Link"]
            target=document["Price"] 
            receiver=document["Email"]
        
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53736 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
            page=requests.get(URL, headers=headers) 
            soup1=BeautifulSoup(page.text,"html.parser")

        
            if "amazon" in URL:
                prod=soup1.find('span',id='productTitle',).text
                if prod is None:
                    print("Product not found on Amazon")
                    continue
                pricea=soup1.find('span',class_='a-price-whole').text
                if pricea is None:
                    print("Price not found on Amazon")
                    continue
                
                price=float(pricea.replace(',','').replace('₹',''))
                print(prod.strip())
                amazon()
            elif "flipkart" in URL:
                prod=soup1.find('span',class_='B_NuCI').text
                pricef=soup1.find('div',class_='_30jeq3 _16Jk6d').text
                price=float(pricef.replace(',','').replace('₹',''))
                print(prod.strip())
                flipkart()
            elif "snapdeal" in URL:
                prod=soup1.find('h1',class_='pdp-e-i-head').text
                pricesd=soup1.find('span',class_='payBlkBig').text
                price=float(pricesd)
                print(prod.strip())
                snapdeal()
            elif "nykaa" in URL:
                prod=soup1.find("h1",class_="css-1gc4x7i").text
                #prod=soup1.find('h1',class_='pdp-name').text
                pricea=soup1.find("span",class_="css-1jczs19").text
                price=float(pricea.replace(',','').replace('₹',''))
                print(prod.strip())
                nykaaprint()
            
            elif "shopclues" in URL:
                prod=soup1.find('h1',itemprop='name').text
                #prod=soup1.find('h1',class_='pdp-name').text
                pricea=soup1.find('span',class_='f_price').text
                price=float(pricea.replace(',','').replace('₹',''))
                print(prod.strip())
                shopprint()
            
            else:
                pass
            ## email ##
            
            if price < target or price == target :
                em(prod,price,URL)    
        else:
            pass
client.close()