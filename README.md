# Price Notifier

## Problem Statement
Online shoppers and investors often struggle with tracking price changes. Fluctuations in product prices, especially during sales events, can lead to missed opportunities to save money. Similarly, the volatile nature of cryptocurrencies and stocks can result in missed profitable trades or potential losses if not closely monitored.
## Solution
The Price Notifier is a user-friendly tool designed to solve the challenges of monitoring prices in an ever-changing market. Key features include:

- **Product Price Monitoring**:  Track prices across multiple e-commerce platforms.
- **Stock/Crypto Price Monitoring**: Keep an eye on stocks and cryptocurrencies with real-time data from Yahoo Finance.
- **Email Notifications**: Receive alerts when prices reach user-defined thresholds.
### Tech Stack:
- Web Scraping: Python and BeautifulSoup.
- Database: MongoDB.
- Frontend: HTML, CSS, JavaScript, React
- Deployment: Heroku.

## Project Structure
The website is divided into two main sections:

1. E-commerce Products
2. Stocks/Cryptocurrencies
   
### E-commerce Products Section
![image](https://github.com/user-attachments/assets/1065dc12-b5cd-448c-a6a2-f082b3b1ae91)

- User Interaction:

Users can visit the website and enter their email, product URL, target price, and a monitoring duration (either until the price drops or for a specific number of days).
The information is stored in **MongoDB** for further processing.
- Price Monitoring:

Web scraping, using BeautifulSoup, is implemented to monitor target product prices across popular e-commerce platforms such as **Amazon, Flipkart, Nykaa, ShopClues, and Snapdeal**.
The application checks for price drops and compares them with the user's target price.

### Stocks/Cryptocurrencies Section

![image](https://github.com/user-attachments/assets/23d3828b-2d7a-428d-aef6-77fbaf4f4d75)

- User Interaction:

Users can enter the stock or cryptocurrency symbol they wish to monitor.
They can set an option to receive email alerts if the price goes either up or down.

- Price Monitoring:

The application uses **Yahoo Finance** to fetch real-time data on stocks and cryptocurrencies.
Users receive email notifications based on the configured price movements.
### Email Notification

- Notification System:
A Python function utilizing smtplib library is implemented to send an email to the user when the price of the monitored item drops below the target or meets the specified condition.
This ensures users are promptly informed about favorable price changes.

![image](https://github.com/user-attachments/assets/510f93ab-bf98-4778-b7f7-a80b74d37636)

![image](https://github.com/user-attachments/assets/589eeba4-3f06-4282-a86b-9bde914c20df)
### Check out the website:
[Price notifier](https://pricenotifier.onrender.com/)


