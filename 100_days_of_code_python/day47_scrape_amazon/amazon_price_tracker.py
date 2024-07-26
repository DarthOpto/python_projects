from bs4 import BeautifulSoup
import requests
import smtplib


practice_url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(practice_url)

soup = BeautifulSoup(response.content, "html.parser")

# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)

# Get the product title
title = soup.find(id="productTitle").get_text().strip()
print(title)

# Set the price below which you would like to get a notification
BUY_PRICE = 100

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price}!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login("darthopto@gmail.com", "D@rth0pt0")
        connection.sendmail(
            from_addr="darthopto@gmail.com",
            to_addrs="darthopto@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )

