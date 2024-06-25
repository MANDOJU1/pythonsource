import numpy as np
import pandas as pd
import requests
from urllib.parse import quote

# naver api
client_id = "fas5rtyssc"  # 본인이 할당받은 ID 입력
client_pw = "ATYxURZ42gqOR9XqQLEYwO3wUYcmDFn8cWKXYhod"  # 본인이 할당받은 Secret 입력

api_url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query="

# 주소 목록 파일 (.xlsx)
data = pd.read_excel(
    "./api/file/list_of_address.xlsx", usecols="B, C", names=["구주소", "도로명주소"]
)

# 네이버 지도 API 이용해서 위경도 찾기
geo_coordi = []  # geographic coordinates
headers = {"X-NCP-APIGW-API-KEY-ID": client_id, "X-NCP-APIGW-API-KEY": client_pw}

for add in data["도로명주소"]:
    if pd.isna(add):  # NaN 값 검사
        latitude = None
        longitude = None
    else:
        add_urlenc = quote(
            add.encode("utf-8")
        )  # 주소를 URL에서 사용할 수 있도록 URL Encoding
        url = api_url + add_urlenc

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()  # HTTP 에러가 발생하면 예외를 발생시킴
            response_body = response.json()

            if "addresses" in response_body and response_body["addresses"]:
                latitude = response_body["addresses"][0]["y"]
                longitude = response_body["addresses"][0]["x"]
                print("Success!")
            else:
                print("No addresses found in the response.")
                latitude = None
                longitude = None
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            latitude = None
            longitude = None
        except Exception as e:
            print(f"Error: {e}")
            latitude = None
            longitude = None

    geo_coordi.append([latitude, longitude])

np_geo_coordi = np.array(geo_coordi)
pd_geo_coordi = pd.DataFrame(
    {
        "구주소": data["구주소"].values,
        "도로명주소": data["도로명주소"].values,
        "위도": np_geo_coordi[:, 0],
        "경도": np_geo_coordi[:, 1],
    }
)

# save result
with pd.ExcelWriter("output_v2.xlsx") as writer:
    pd_geo_coordi.to_excel(writer, sheet_name="Sheet1", index=False)
