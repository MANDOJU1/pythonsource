import requests
import csv


url = "http://apis.data.go.kr/1543061/abandonmentPublicSrvc/abandonmentPublic"
params = {
    "bgnde": "20240101",
    "endde": "20240512",
    "pageNo": "1",
    "numOfRows": "1000",
    "serviceKey": "onr2dF6kAgGjBXVxNMOm2DSD6wsM24sEsylFqWITUO0x5S/kGMBhTHF36x1rwpkWaowKB6oM0jrArcmquppyyg==",
    "_type": "json",
    "upkind": 417000,
}


# 요청

r = requests.get(url, params=params)
res = r.json()

# json 응답 확인
# print(animals)

animals = res["response"]["body"]["items"]["item"]

with open("./animals.csv", "w+", newline="") as f:
    fieldnames = [
        "desertionNo",
        "filename",
        "happenDt",
        "happenPlace",
        "kindCd",
        "colorCd",
        "age",
        "weight",
        "noticeNo",
        "noticeSdt",
        "noticeEdt",
        "popfile",
        "processState",
        "sexCd",
        "neuterYn",
        "specialMark",
        "careNm",
        "careTel",
        "careAddr",
        "orgNm",
        "officetel",
    ]
    wt = csv.DictWriter(f, fieldnames=fieldnames)
    wt.writeheader()
    for animal in animals:
        dict = {
            "desertionNo": animal["desertionNo"],
            "filename": animal["filename"],
            "happenDt": animal["happenDt"],
            "happenPlace": animal["happenPlace"],
            "kindCd": animal["kindCd"],
            "colorCd": animal["colorCd"],
            "age": animal["age"],
            "weight": animal["weight"],
            "noticeNo": animal["noticeNo"],
            "noticeSdt": animal["noticeSdt"],
            "noticeEdt": animal["noticeEdt"],
            "popfile": animal["popfile"],
            "processState": animal["processState"],
            "sexCd": animal["sexCd"],
            "neuterYn": animal["neuterYn"],
            "specialMark": animal["specialMark"],
            "careNm": animal["careNm"],
            "careTel": animal["careTel"],
            "careAddr": animal["careAddr"],
            "orgNm": animal["orgNm"],
            "officetel": animal["officetel"],
        }
        print(dict)
        wt.writerow(dict)
