import bs4
import requests
import csv

def function1():

    base_url = "https://www.bssnews.net/bangla/all-news"
    catagory = "sports"
    #next_page = "18"

    national_catagory = [""]

    all_url = []
    i=0
    for page_index in national_catagory:
        i=i+1
        if i==1:
            complete_url =  base_url + '/' + catagory + '/'#+ next_page + '/'
            #print(complete_url + '18')
            #print(complete_url + '36')
        else:
            complete_url = base_url + '/' + catagory + '/' +str(page_index)
            #print(complete_url + '18')
            #print(complete_url + '36')
        all_url.append([complete_url])
        all_url.append([complete_url+'?pg=2'])
        all_url.append([complete_url + '?pg=3'])
        all_url.append([complete_url + '?pg=4'])
        all_url.append([complete_url + '?pg=5'])
        all_url.append([complete_url + '?pg=6'])
        all_url.append([complete_url + '?pg=7'])
        all_url.append([complete_url + '?pg=8'])
        all_url.append([complete_url + '?pg=9'])
        all_url.append([complete_url + '?pg=10'])
        all_url.append([complete_url + '?pg=11'])
        all_url.append([complete_url + '?pg=12'])
        all_url.append([complete_url + '?pg=13'])
        all_url.append([complete_url + '?pg=14'])
        all_url.append([complete_url + '?pg=15'])
        all_url.append([complete_url + '?pg=16'])
        all_url.append([complete_url + '?pg=17'])
        all_url.append([complete_url + '?pg=18'])
        all_url.append([complete_url + '?pg=19'])
        all_url.append([complete_url + '?pg=20'])
        all_url.append([complete_url + '?pg=21'])
        all_url.append([complete_url + '?pg=22'])
        all_url.append([complete_url + '?pg=23'])
        all_url.append([complete_url + '?pg=24'])
        all_url.append([complete_url + '?pg=25'])
        all_url.append([complete_url + '?pg=26'])
        all_url.append([complete_url + '?pg=27'])
        all_url.append([complete_url + '?pg=28'])
        all_url.append([complete_url + '?pg=29'])
        all_url.append([complete_url + '?pg=30'])
        all_url.append([complete_url + '?pg=31'])
        all_url.append([complete_url + '?pg=32'])
        all_url.append([complete_url + '?pg=33'])
        all_url.append([complete_url + '?pg=34'])
        all_url.append([complete_url + '?pg=35'])
        all_url.append([complete_url + '?pg=36'])
        all_url.append([complete_url + '?pg=37'])
        all_url.append([complete_url + '?pg=38'])
        all_url.append([complete_url + '?pg=39'])
        all_url.append([complete_url + '?pg=40'])
        all_url.append([complete_url + '?pg=41'])
        all_url.append([complete_url + '?pg=42'])
        all_url.append([complete_url + '?pg=43'])
        all_url.append([complete_url + '?pg=44'])
        all_url.append([complete_url + '?pg=45'])
        all_url.append([complete_url + '?pg=46'])
        all_url.append([complete_url + '?pg=47'])
        all_url.append([complete_url + '?pg=48'])
        all_url.append([complete_url + '?pg=49'])
        all_url.append([complete_url + '?pg=50'])
        all_url.append([complete_url + '?pg=51'])
        all_url.append([complete_url + '?pg=52'])
        all_url.append([complete_url + '?pg=53'])
        all_url.append([complete_url + '?pg=54'])
        all_url.append([complete_url + '?pg=55'])
        all_url.append([complete_url + '?pg=56'])
        all_url.append([complete_url + '?pg=57'])
        all_url.append([complete_url + '?pg=58'])
        all_url.append([complete_url + '?pg=59'])
        all_url.append([complete_url + '?pg=60'])
        all_url.append([complete_url + '?pg=61'])
        all_url.append([complete_url + '?pg=62'])
        all_url.append([complete_url + '?pg=63'])
        all_url.append([complete_url + '?pg=64'])
        all_url.append([complete_url + '?pg=65'])
        all_url.append([complete_url + '?pg=66'])
        all_url.append([complete_url + '?pg=67'])
        all_url.append([complete_url + '?pg=68'])
        all_url.append([complete_url + '?pg=69'])
        all_url.append([complete_url + '?pg=70'])
        all_url.append([complete_url + '?pg=71'])
        all_url.append([complete_url + '?pg=72'])
        all_url.append([complete_url + '?pg=73'])
        all_url.append([complete_url + '?pg=74'])
        all_url.append([complete_url + '?pg=75'])
        all_url.append([complete_url + '?pg=76'])
        all_url.append([complete_url + '?pg=77'])
        all_url.append([complete_url + '?pg=78'])
        all_url.append([complete_url + '?pg=79'])
        all_url.append([complete_url + '?pg=80'])
        all_url.append([complete_url + '?pg=81'])
        all_url.append([complete_url + '?pg=82'])
        all_url.append([complete_url + '?pg=83'])
        all_url.append([complete_url + '?pg=84'])
        all_url.append([complete_url + '?pg=85'])
        all_url.append([complete_url + '?pg=86'])
        all_url.append([complete_url + '?pg=87'])
        all_url.append([complete_url + '?pg=88'])
        all_url.append([complete_url + '?pg=89'])
        all_url.append([complete_url + '?pg=90'])
        all_url.append([complete_url + '?pg=91'])
        all_url.append([complete_url + '?pg=92'])
        all_url.append([complete_url + '?pg=93'])
        all_url.append([complete_url + '?pg=94'])
        all_url.append([complete_url + '?pg=95'])
        all_url.append([complete_url + '?pg=96'])
        all_url.append([complete_url + '?pg=97'])
        all_url.append([complete_url + '?pg=98'])
        all_url.append([complete_url + '?pg=99'])
        all_url.append([complete_url + '?pg=100'])
        all_url.append([complete_url + '?pg=101'])
        all_url.append([complete_url + '?pg=102'])
        all_url.append([complete_url + '?pg=103'])
        all_url.append([complete_url + '?pg=104'])
        all_url.append([complete_url + '?pg=105'])
        all_url.append([complete_url + '?pg=106'])
        all_url.append([complete_url + '?pg=107'])
        all_url.append([complete_url + '?pg=108'])
        all_url.append([complete_url + '?pg=109'])
        all_url.append([complete_url + '?pg=110'])
        all_url.append([complete_url + '?pg=111'])
        all_url.append([complete_url + '?pg=112'])
        all_url.append([complete_url + '?pg=113'])
        all_url.append([complete_url + '?pg=114'])
        all_url.append([complete_url + '?pg=115'])
        all_url.append([complete_url + '?pg=116'])
        all_url.append([complete_url + '?pg=117'])
        all_url.append([complete_url + '?pg=118'])
        all_url.append([complete_url + '?pg=119'])
        all_url.append([complete_url + '?pg=120'])
        all_url.append([complete_url + '?pg=121'])
        all_url.append([complete_url + '?pg=122'])
        all_url.append([complete_url + '?pg=123'])
        all_url.append([complete_url + '?pg=124'])
        all_url.append([complete_url + '?pg=125'])
        all_url.append([complete_url + '?pg=126'])
        all_url.append([complete_url + '?pg=127'])
        all_url.append([complete_url + '?pg=128'])
        all_url.append([complete_url + '?pg=129'])
        all_url.append([complete_url + '?pg=130'])
        all_url.append([complete_url + '?pg=131'])
        all_url.append([complete_url + '?pg=132'])
        all_url.append([complete_url + '?pg=133'])
        all_url.append([complete_url + '?pg=134'])
        all_url.append([complete_url + '?pg=135'])
        all_url.append([complete_url + '?pg=136'])
        all_url.append([complete_url + '?pg=137'])
        all_url.append([complete_url + '?pg=138'])
        all_url.append([complete_url + '?pg=139'])
        all_url.append([complete_url + '?pg=140'])
        all_url.append([complete_url + '?pg=141'])
        all_url.append([complete_url + '?pg=142'])
        all_url.append([complete_url + '?pg=143'])
        all_url.append([complete_url + '?pg=144'])
        all_url.append([complete_url + '?pg=145'])
        all_url.append([complete_url + '?pg=146'])
        all_url.append([complete_url + '?pg=147'])
        all_url.append([complete_url + '?pg=148'])
        all_url.append([complete_url + '?pg=149'])
        all_url.append([complete_url + '?pg=150'])
        all_url.append([complete_url + '?pg=151'])
        all_url.append([complete_url + '?pg=152'])
        all_url.append([complete_url + '?pg=153'])
        all_url.append([complete_url + '?pg=154'])
        all_url.append([complete_url + '?pg=155'])
        all_url.append([complete_url + '?pg=156'])
        all_url.append([complete_url + '?pg=157'])
        all_url.append([complete_url + '?pg=158'])
        all_url.append([complete_url + '?pg=159'])
        all_url.append([complete_url + '?pg=160'])
        all_url.append([complete_url + '?pg=161'])
        all_url.append([complete_url + '?pg=162'])
        all_url.append([complete_url + '?pg=163'])
        all_url.append([complete_url + '?pg=164'])
        all_url.append([complete_url + '?pg=165'])
        all_url.append([complete_url + '?pg=166'])
        all_url.append([complete_url + '?pg=167'])
        all_url.append([complete_url + '?pg=168'])
        all_url.append([complete_url + '?pg=169'])
        all_url.append([complete_url + '?pg=170'])
        all_url.append([complete_url + '?pg=171'])
        all_url.append([complete_url + '?pg=172'])
        all_url.append([complete_url + '?pg=173'])
        all_url.append([complete_url + '?pg=174'])
        all_url.append([complete_url + '?pg=175'])
        all_url.append([complete_url + '?pg=176'])
        all_url.append([complete_url + '?pg=177'])
        all_url.append([complete_url + '?pg=178'])
        all_url.append([complete_url + '?pg=179'])
        all_url.append([complete_url + '?pg=180'])
        all_url.append([complete_url + '?pg=181'])
        all_url.append([complete_url + '?pg=182'])
        all_url.append([complete_url + '?pg=183'])
        all_url.append([complete_url + '?pg=184'])
        all_url.append([complete_url + '?pg=185'])
        all_url.append([complete_url + '?pg=186'])
        all_url.append([complete_url + '?pg=187'])
        all_url.append([complete_url + '?pg=188'])
        all_url.append([complete_url + '?pg=189'])
        all_url.append([complete_url + '?pg=190'])
        all_url.append([complete_url + '?pg=191'])
        all_url.append([complete_url + '?pg=192'])
        all_url.append([complete_url + '?pg=193'])
        all_url.append([complete_url + '?pg=194'])
        all_url.append([complete_url + '?pg=195'])
        all_url.append([complete_url + '?pg=196'])
        all_url.append([complete_url + '?pg=197'])
        all_url.append([complete_url + '?pg=198'])
        all_url.append([complete_url + '?pg=199'])








    with open('main_page_url.csv',mode = 'w', newline='') as main_url_list:
        main_url_writer = csv.writer(main_url_list,delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for url in all_url:
            print(url)
            main_url_writer.writerow(url)

    main_url_list.close()
    return all_url
function1()
