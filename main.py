from bs4 import BeautifulSoup
import requests

try:
    url  = "https://www.flipkart.com/search?q=" 
    txt = input('Enter the item name: ')
    x = txt.split()
    srh = '%20'.join(x)
    newurl = url + srh
    print(newurl)

    response = requests.get(newurl)                               
    soup     = BeautifulSoup(response.text,'html.parser')          
    products   = soup.find_all('div',class_='_3pLy-c row')
    print(len(products))

    # Dictionary format 
    phone = {   'pnum':0,'name':'nodata' , 'price':'no data' , 'rate':'no data',
                'ram':'' ,  'rom':'' ,   'mem':'',
                'size':'',  'bcam':'',   'fcam':'',
                'bat':'' ,  'pro':'' ,   'war':'' 
            }
    num = 0
    for prod in products:
        num = num + 1
        phone['pnum'] = num 
    
        name  = prod.find('div',class_='col col-7-12').find('div',class_='_4rR01T').text
        phone['name'] = name
        price = prod.find('div',class_='col col-5-12 nlI3QM').find('div',class_='_30jeq3 _1_WHN1').text
        phone['price'] = price
        rate  = prod.find('div',class_='col col-7-12').find('div',class_='_3LWZlK').text
        phone['rate'] = rate
        specs = prod.find('div',class_='col col-7-12').find('div',class_='fMghEO').find('ul').find_all('li',class_='rgWa7D')
        
        '''All Specifictaion are added to List'''
        allspecs = []
        for item in specs:
            allspecs.append(item.text)

        ''' separation of specifications '''
        for each in allspecs:
            if 'GB' in each:
                storage = each.split('|')

                for item in storage:
                    if "RAM" in item:
                        phone['ram'] =item
                        
                    elif "ROM" in item:
                        phone['rom'] =item
                    
                    elif "Expandable" in item:
                        phone['mem'] =item

            elif 'Display' in each:
                size = each
                phone['size'] =size
                
            elif 'MP' in each:
                camera = each
                if '|' in camera:
                    camera =camera.split('|')
                    bcam = camera[0]
                    fcam = camera[1]
                else:
                    bcam = camera
                    fcam = ''

                phone['bcam'] = bcam
                phone['fcam'] = fcam

            elif 'Battery' in each:
                bat = each
                phone['bat'] = bat

            elif 'Processor' in each:
                pro = each
                phone['pro'] = pro
                
            elif 'Warranty' in each:
                war = each
                phone['war'] = war
                
            else:
                print('missing criteria')  

        for key , value in phone.items():
            
            print(key,end=' ')
            print(value,end=' ')
            print()
        print('***********************************')


   
except Exception as msg:
    print('today Error : ',msg)
    print("Error ")


