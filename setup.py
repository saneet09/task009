from flask import Flask, render_template, request
from flask_cors import CORS
import json
import os
import sys
import numpy as np 
url = 'https://drive.google.com/a/greendeck.co/uc?id=19r_vn0vuvHpE-rJpFHvXHlMvxa8UOeom&export=download'
app = Flask(__name__)
CORS(app)
def init_files(dump_path = 'dumps/netaporter_gb.json'):
    if dump_path.split('/')[0] not in os.listdir():
        os.mkdir(dump_path.split('/')[0])
    if os.path.exists(dump_path):
        pass
    else:
        gdown.download(url = url, output = dump_path, quiet=False)
def prepare_dataset(path = 'dumps/netaporter_gb.json'):
    '''YOUR DATA PREPARATION CODE HERE'''
    pass        
@app.route("/")
def home1():
    return render_template("home1.html")
   # return render_template('home1.html',data=Todos.query.all())
@app.route('/task1',methods=['get','post'])
def task1():
    product_json=[]
    with open("dumps/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    offer=[]
    regular=[]
    arr=[]
    ids=[]
    for i in range(52383):
        offer.append(product_json[i]["price"]["offer_price"]["value"])
        regular.append(product_json[i]["price"]["regular_price"]["value"])
    for i in range(len(regular)):
        diff=regular[i]-offer[i]
        div=diff/regular[i]
        discount=div*100
        if(discount>5):
            arr.append(i)
    for i in range(len(arr)):
        ids.append(product_json[arr[i]]['_id']['$oid'])
                

    return render_template("result.html",prediction=ids) 

@app.route("/task2",methods=['get','post'])
def task2():
    product_json=[]
    with open("dumps/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    offer=[]
    regular=[]
    arr=[]
    ids=[]
    for i in range(52383):
        offer.append(product_json[i]["price"]["offer_price"]["value"])
        regular.append(product_json[i]["price"]["regular_price"]["value"])
    for i in range(len(regular)):
        diff=regular[i]-offer[i]
        div=diff/regular[i]
        discount=div*100
        if(discount>5):
            arr.append(i)
    for i in range(len(arr)):
        if(product_json[arr[i]]['brand']['name']=="balenciaga"):
            ids.append(product_json[arr[i]]['_id']['$oid'])
    return render_template("task2.html",prediction=ids) 

@app.route("/task3",methods=['get','post'])
def task3():
    product_json=[]
    with open("dumps/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    index=[]
    offer=[]
    regular=[]
    discounts=[]
    ids=[]
    for i in range(52383):  
        if(product_json[i]['brand']['name']=="gucci"):
            offer.append(product_json[i]["price"]["offer_price"]["value"])
            regular.append(product_json[i]["price"]["regular_price"]["value"])
    for i in range(len(regular)):
        diff=regular[i]-offer[i]
        div=diff/regular[i]
        discount=div*100
        discounts.append(discount)
    length=len(discounts)
    total=0
    for i in range(length):
        total =total+discounts[i]
    avgdiscount=total/length
    return render_template("task3.html",prediction=avgdiscount,totals=length)

@app.route("/task4",methods=['get','post'])
def task4():
    product_json=[]
    with open("E:/flask/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    index=[]
    discounts=[]
    listbrand=[]
    ids=[]
    brand=[]
    for i in range(52383):
        brand.append(product_json[i]['brand']['name'])      
    brandarr = np.array(brand)  
    uniquebrand=np.unique(brandarr)
    leng=len(uniquebrand)
    j=0
    for j in range(leng):
        offer=[]
        regular=[]
        for i in range(52383):
            if(product_json[i]['brand']['name']==uniquebrand[j]):
                offer.append(product_json[i]["price"]["offer_price"]["value"])
                regular.append(product_json[i]["price"]["regular_price"]["value"])  
        for i in range(len(regular)):
            diff=regular[i]-offer[i]
            div=diff/regular[i]
            discount=div*100
            discounts.append(discount)
        length=len(discounts)
        total=0
        for i in range(length):
            total =total+discounts[i]
            avgdiscount=total/length        
        if(avgdiscount>10):
            listbrand.append(uniquebrand[j])
    t=len(listbrand)        
    return render_template("task4.html",prediction=listbrand,totals=t)

@app.route("/task5",methods=['get','post'])
def task5():
    product_json=[]
    with open("dumps/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    value=0
    ids=[]
    for i in range(52383):
        if 'similar_products' in product_json[i]:
            if(product_json[i]['price']['basket_price']['value']>product_json[i]['similar_products']['meta']['max_price']['basket']):
                ids.append(product_json[i]['_id']['$oid']) 
    return render_template("task5.html",prediction=ids)

@app.route("/task6",methods=['get','post'])
def task6():
    product_json=[]
    with open("dumps/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    value=0
    ids=[]
    for i in range(52383):
        if 'similar_products' in product_json[i]:
            if(product_json[i]['price']['basket_price']['value']>product_json[i]['similar_products']['meta']['max_price']['basket']):
                if(product_json[i]['brand']['name']=="balenciaga"):
                    ids.append(product_json[i]['_id']['$oid'])        
    return render_template("task6.html",prediction=ids)

@app.route("/task7",methods=['get','post'])
def task7():
    product_json=[]
    with open("dumps/netaporter_gb.json",encoding="utf8") as fp:
        for product in fp.readlines():
            product_json.append(json.loads(product))
    a=52383
    offer=[]
    regular=[]
    arr=[]
    ids=[]
    for i in range(52383):
        if(product_json[i]['website_id']['$oid']=='5d0cc7b68a66a100014acdb0'):
            offer.append(product_json[i]["price"]["offer_price"]["value"])
            regular.append(product_json[i]["price"]["regular_price"]["value"])
    for i in range(len(regular)):
        diff=offer[i]-regular[i]
        div=diff/offer[i]
        discount=div*100
        if(discount>10):
            arr.append(i)
    for i in range(len(arr)):
        ids.append(product_json[arr[i]]['_id']['$oid'])        

    return render_template("task7.html",prediction=ids) 


    
if __name__ == "__main__":
    init_files('dumps/netaporter_gb.json') 
    prepare_dataset('dumps/netaporter_gb.json')
    #os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.dev")
    app.debug=True
    app.run()