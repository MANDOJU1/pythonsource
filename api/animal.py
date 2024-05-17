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
        "desertion_No",
        "filename",
        "happen_Dt",
        "happen_Place",
        "kind_Cd",
        "color_Cd",
        "age",
        "weight",
        "notice_No",
        "notice_Sdt",
        "notice_Edt",
        "popfile",
        "process_State",
        "sex_Cd",
        "neuter_Yn",
        "special_Mark",
        "care_Nm",
        "care_Tel",
        "care_Addr",
        "org_Nm",
        "officetel",
    ]
    wt = csv.DictWriter(f, fieldnames=fieldnames)
    wt.writeheader()
    for animal in animals:
        dict = {
            "desertion_No": animal["desertionNo"],
            "filename": animal["filename"],
            "happen_Dt": animal["happenDt"],
            "happen_Place": animal["happenPlace"],
            "kind_Cd": animal["kindCd"],
            "color_Cd": animal["colorCd"],
            "age": animal["age"],
            "weight": animal["weight"],
            "notice_No": animal["noticeNo"],
            "notice_Sdt": animal["noticeSdt"],
            "notice_Edt": animal["noticeEdt"],
            "popfile": animal["popfile"],
            "process_State": animal["processState"],
            "sex_Cd": animal["sexCd"],
            "neuter_Yn": animal["neuterYn"],
            "special_Mark": animal["specialMark"],
            "care_Nm": animal["careNm"],
            "care_Tel": animal["careTel"],
            "care_Addr": animal["careAddr"],
            "org_Nm": animal["orgNm"],
            "officetel": animal["officetel"],
        }
        print(dict)
        wt.writerow(dict)
