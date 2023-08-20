import requests
import json
import urllib3
import ieee_information

def single_page(headers, searchword, url, page):
    data = {
        "newsearch": 'true',
        "queryText": searchword,
        "contentType": 'journals',
        # "ranges": '2003_2023_Year',
        "highlight": 'true',
        # "returnFacets": 'ALL',
        "returnType": 'SEARCH',
        "matchPubs": 'true',
        "pageNumber": str(page),
        
    }
    res = requests.post(url=url, json=data,headers=headers,verify=False)
    resq = requests.get(url=url, json=data,headers=headers,verify=False)
    dic_obj = res.json()
    return dic_obj


def airtcle_list(searchword):
    headers = {
        'Accept': 'application/json,text/plain,*/*',
        'Accept-Encoding': 'gzip,deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '247',
        'Content-Type': 'application/json',
        'Referer': 'https://ieeexplore.ieee.org/',
        # 'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp',
        # 'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&highlight=true&ranges=2016_2023_Year',
        # 'Referer': 'https://ieeexplore.ieee.org/search/searchresult.jsp?highlight=true&returnFacets=ALL&returnType=SEARCH&matchPubs=true&ranges=2021_2024_Year',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.5790.170 '
                      'Safari/537.36 Edg/108.0.1462.46',
    }
    url = 'https://ieeexplore.ieee.org/rest/search'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    dic_obj = single_page(headers, searchword, url, 1)
    totalpage = int(dic_obj["totalPages"])
    totalpage = 5
    totalrecords = int(dic_obj["totalRecords"])
    print('keyword:' + searchword)
    print('sum select ' + str(totalrecords) + ' article')
    result_list = []    # 
    for i in range(1, totalpage + 1):
        dic_obj = single_page(headers, searchword, url, i)
        for dic_obj in dic_obj["records"]:
            result_list.append(dic_obj["articleNumber"])

    return result_list
if __name__ == "__main__":
    sd = airtcle_list("speech")
    for airtcle_number in sd:
        page_text = ieee_information.single_information(airtcle_number)
        title = ieee_information.get_title(page_text)
        print(airtcle_number + " "+title)