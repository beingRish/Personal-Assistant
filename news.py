# importing requests package
import requests    
from output_module import output
from internet import check_internet_connection
 
def get_news():
    if check_internet_connection():
        
     
        # BBC news api
        # following query parameters are used
        # source, sortBy and apiKey
        query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "d06efeb11b384df7a2456e36f7d32bf3"
        }
        main_url = " https://newsapi.org/v1/articles"
    
        # fetching data in json format
        res = requests.get(main_url, params=query_params)
        open_bbc_page = res.json()
    
        # getting all articles in a string article
        article = open_bbc_page["articles"]
    
        # empty list which will
        # contain all trending news
        results = []
        
        for ar in article:
            results.append(ar["title"])
            
        for i in range(len(results)):
            
            # printing all trending news
            output(str(i + 1) + " " + results[i])
            
        return "So these were the top news from today "
    
    else:
        return "please check your internet connection first"
         
