from PIL import Image
from PIL.ExifTags import TAGS
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager

import time


def open_map(image_path):
    #print("@@@image")
    image = Image.open(image_path)
    #print(image)
    info = image._getexif()
    image.close()

    taglabel = {}

    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        taglabel[decoded] = value

    exif_gps = taglabel['GPSInfo']
    #print(taglabel)
    lat_data = exif_gps[2]
    lon_data = exif_gps[4]

    # 도, 분, 초로 나타내기
    # lat = str(int(lat_data[0])) + "°" + str(int(lat_data[1])) + "'" + str(lat_data[2]) + "\"" + exif_gps[1]
    # lon = str(int(lon_data[0])) + "°" + str(int(lon_data[1])) + "'" + str(lon_data[2]) + "\"" + exif_gps[3]

    # 도 decimal로 나타내기
    # 위도 계산
    lat = (lat_data[0] + (lat_data[1] + lat_data[2] / 60.0) / 60.0)
    # 북위, 남위 인지 판단, 남위일 경우 -로 변경
    if exif_gps[1] == 'S':
        lat = lat * -1

    # 경도 계산
    lon = (lon_data[0] + (lon_data[1] + lon_data[2] / 60.0) / 60.0)
    # 동경, 서경 인지를 판단, 서경일 경우 -로 변경
    if exif_gps[3] == 'W':
        lon = lon * -1

    #print(lat, lon)

    return "https://www.google.com/maps/place/" + str(lat) + "+" + str(lon)

    # webbrowser.open_new("https://www.google.com/maps/place/" + lat + "+" + lon)


def get_geo_info(image_path):

    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--headless')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--remote-debugging-port=9222")

    
    try:

        url = open_map(image_path)
        time.sleep(2)
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        time.sleep(6)
    # time.sleep(5)
    # search_box = driver.find_element(By.ID, "input_search1665595183744")
    # search_box.send_keys("36.61919722222222 127.28920833333333")
    # time.sleep(3)
        s = driver.find_element(By.CLASS_NAME, 'DkEaL')
        time.sleep(6)
        addr = s.text.split()
        assert s.is_displayed() is True
        print("위치정보 추출 완료\n")
        #print(addr)
        print(addr[0])
        print(addr[1])
        print(addr[2])
    except Exception as ex:
        print(ex)


    return(addr[2])
