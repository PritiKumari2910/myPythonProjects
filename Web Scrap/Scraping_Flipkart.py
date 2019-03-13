from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url='https://www.flipkart.com/search?q=iphone&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_3&otracker1=AS_QueryStore_OrganicAutoSuggest_0_3&as-pos=0&as-type=RECENT&as-searchtext=iph'

#uReq, opens the webpage and packs it to var
uClient = uReq(my_url)
#uClient will read the parsed url
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div", {"class": "_3O0U0u"})

#print(len(containers))

#pretiffy is a function to beautify html or used to organize the html contents
#print(soup.prettify(containers[0]))

#picks 1st product
container = containers[0]

#alt is an attribute & attribute should always be written in square brackets
#print(container.div.img["alt"])

#to get the price

#price = container.findAll("div", {"class": '_1vC4OE _2rQ-NK'})
#.text helps to get only the price as text not extra tags or attributes in output
#print(price[0].text)

#ratings = container.findAll("div",{"class":"niH0FQ"})
#print(ratings[0].text)


# to show the output in file
filename = "products.csv"
f = open(filename,"w")

headers="Product_Name,Pricing,Ratings\n"
f.write(headers)


# to get all the products in file
for container in containers:
    product_name = container.div.img["alt"]

    price_container = container.findAll("div", {"class": '_1vC4OE _2rQ-NK'})
    price = price_container[0].text.strip()

    rating_container = container.findAll("div",{"class":"niH0FQ"})
    rating = rating_container[0].text

   # print("product name : ", product_name)
    #print("price : ",price)
   # print("rating : ", rating)

    #string parsing

    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    final_price = "Rs."+rm_rupee[1]


    final_rating: object = rating[0:3]
    #print("rating : ",final_rating)

    print(product_name+"|"+final_price+"|"+final_rating)

    #to write the output in csv file
    f.write(product_name+"|"+final_price+"|"+final_rating+"\n")

f.close()
