import arxivscraper
import datetime
import time
import requests
import json
from datetime import timedelta


def get_daily_code(DateToday,cats):
    """
    @param DateToday: str
    @param cats: dict
    @return paper_with_code: dict
    """
    from_day = until_day = DateToday
    content = dict()
    content1 =dict()
    # content
    output = dict()
    for k,v in cats.items():
        scraper = arxivscraper.Scraper(category=k, date_from=from_day,date_until=until_day,filters={'categories':v})
        tmp = scraper.scrape()
        print(tmp)
        if isinstance(tmp,list):
            for item in tmp:
                if item["id"] not in output:
                    output[item["id"]] = item
        time.sleep(30)

    base_url = "https://arxiv.paperswithcode.com/api/v0/papers/"
    cnt = 0

    for k,v in output.items():
        print(v["id"])
        _id = v["id"]
        paper_title1 = " ".join(v["title"].split())
        paper_title1 = paper_title1.lower()
        print(paper_title1)
        print("#"*5)
        if paper_title1.__contains__("acoustic echo") or paper_title1.__contains__("residual echo"):
            paper_type = "aec"
        elif paper_title1.__contains__("noise suppress") or paper_title1.__contains__("noise reduction"):
            paper_type = "ans"
        elif paper_title1.__contains__("gain control"):
            paper_type = "agc"
        elif paper_title1.__contains__("dereveb"):
            paper_type = "dereverb"
        elif paper_title1.__contains__("howling"):
            paper_type = "howling"
        elif paper_title1.__contains__("doa") or paper_title1.__contains__("direction-of-arrival") or paper_title1.__contains__("source localization") or paper_title1.__contains__("source track"):
            paper_type = "source_localization"
        elif paper_title1.__contains__("speech separation"):
            paper_type = "speech_separation"
        elif paper_title1.__contains__("speech enhancement"):
            paper_type = "speech_enhancement"
        else:
            paper_type = None

        if paper_type is not None:
            paper_title = " ".join(v["title"].split())
            paper_author = v["authors"]
            paper_title1 = v["title"]
            paper_url = v["url"]
            paper_abstract = v["abstract"]
            # url = base_url + _id
            content[_id] = f"|{paper_type.upper()}|{paper_title}|{paper_url}|{paper_author}|\n"
            content1[paper_type.upper()] = f"|{paper_type.upper()}|{paper_title}|{paper_abstract}|{paper_url}|{paper_author}|\n"

        # try:
        #     r = requests.get(url).json()
        #     if "official" in r and r["official"]:
        #         cnt += 1
        #         repo_url = r["official"]["url"]
        #         repo_name = repo_url.split("/")[-1]

        #         # content[_id] = f"|[{paper_title}]({paper_url})|[{repo_name}]({repo_url})|\n"
        #         content[_id] = f"|[{paper_title}]({paper_url})|\n"
        # except Exception as e:
        #     print(f"exception: {e} with id: {_id}")
    content1 = dict(sorted(content1.items(), reverse=False))
    data = {DateToday:content1}
    return data

def update_daily_json(filename,data_all):
    with open(filename,"r") as f:
        content = f.read()
        if not content:
            m = {}
        else:
            m = json.loads(content)
    
    #灏哾atas鏇存柊鍒癿涓?
    for data in data_all:
        m.update(data)

    # save data to daily.json

    with open(filename,"w") as f:
        json.dump(m,f)
    



def json_to_md(filename):
    """
    @param filename: str
    @return None
    """

    with open(filename,"r") as f:
        content = f.read()
        if not content:
            data = {}
        else:
            data = json.loads(content)
    # clean README.md if daily already exist else creat it
    with open("README.md","w+") as f:
        pass
    # write data into README.md
    with open("README.md","a+") as f:
        # 瀵筪ata鏁版嵁鎺掑簭
        for day in sorted(data.keys(),reverse=True):
            day_content = data[day]
            if not day_content:
                continue
            # the head of each part
            f.write(f"## {day}\n")
            f.write("|type|paper|abstract|url|author|\n" + "|---|---|---|---|---|\n")
            for k,v in day_content.items():
                f.write(v)
    
    print("finished")        

if __name__ == "__main__":

    DateToday = datetime.date.today()
    N = 3# 往前查询的天数
    data_all = []
    for i in range(2,N):
        day = str(DateToday + timedelta(-i))
        # you can add the categories in cats
        cats = {
        "eess":["eess.AS"],
        # "cs":["cs.SD"]
    }
        data = get_daily_code(day,cats)
        data_all.append(data)
    update_daily_json("daily.json",data_all)
    json_to_md("daily.json")
