from typing import List
from fastapi import FastAPI
import requests
from bs4 import BeautifulSoup
import os
import json

app = FastAPI()

"""
def main(query):
    if "hava durumu" in query or "hava nasil" in query or "weather" in query or "temperature" in query:
        scrape_weather(query)
    elif "trafik" in query or "yol durumu" in query or "traffic" in query or "road" in query:
        scrape_traffic(query)
    elif "otel" in query or "hotel" in query or "konaklama" in query or "accommodation" in query or "motel" in query:
        scrape_hotel(query)
    elif "biografi" in query or "kim" in query or "kimdir" in query or "biography" in query:
        scrape_biography(query)
    elif "uçuş" in query or "flight" in query or "flights" in query:
        scrape_flight(query)
"""

@app.get("/scrape_search/hava_durumu")
async def scrape_weather(query: str):


    # google search
    url = f"https://www.google.com/search?q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    # request
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # output
    elements = soup.find_all("div", class_="eKPi4")
    if elements:
        location = elements[0].text
    else:
        return {"error": "Hava durumu sonucu bulunamadı."}

    temperature = soup.find_all("div", class_="wob_dcp")
    if elements:
        temp = temperature[0].text
    else:
        return {"error": "Hava durumu sonucu bulunamadı."}

    # write date
    data = {
        "query": query,
        "location": location,
        "temperature": temp,
    }

    file_path = "scrape_search.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            existing_data = json.load(file)

        existing_data.append(data)

        with open(file_path, "w") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
    else:
        with open(file_path, "w") as file:
            json.dump([data], file, ensure_ascii=False, indent=4)

    return data

@app.get("/scrape_search/trafik_durumu")
async def scrape_traffic(query: str):

    url = f"https://www.google.com/maps/search/{query}/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    elements = soup.find_all("div", class_="UBoxCb vdQmEd EtOod pkphOe")
    if elements:
        description = elements[0].span.text
    else:
        return {"error": "Trafik durumu sonucu bulunamadı."}

    data = {
        'query': query,
        'description': description
    }

    file_path = 'scrape_search.json'

    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            existing_data = json.load(file)

        existing_data.append(data)

        with open(file_path, 'w') as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
    else:
        with open(file_path, 'w') as file:
            json.dump([data], file, ensure_ascii=False, indent=4)

    return data

@app.get("/scrape_search/biography")
async def scrape_biography(query: str):
    url = f"https://www.google.com/search?q={query} biography"

    header = "Biography"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all("div", class_="kno-rdesc")

    if elements:
        info = elements[0].span.text
        print(info)

        # write data
        data = {
            'query': query,
            'info': info
        }

        file_path = 'scrape_search.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = json.load(file)

            existing_data.append(data)

            with open(file_path, 'w') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
        else:
            with open(file_path, 'w') as file:
                json.dump([data], file, ensure_ascii=False, indent=4)
    else:
        return {"error": "arama sonucu bulunamadı."}

    return data

@app.get("/scrape_search/flight")
async def scrape_flight(query: str):
    url = f"https://www.google.com/search?q={query} flight"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    elements = soup.find_all("a", class_="ikUyY a-no-hover-decoration")

    if elements:
        info = elements[0].text

        # write data
        data = {
            'query': query,
            'info': info
        }

        file_path = 'scrape_search.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = json.load(file)

            existing_data.append(data)

            with open(file_path, 'w') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
        else:
            with open(file_path, 'w') as file:
                json.dump([data], file, ensure_ascii=False, indent=4)

        return data
    else:
        return {"error": "arama sonucu bulunamadı."}

@app.get("/scrape_search/hotel")
async def scrape_hotel(query: str):
    url = f"https://www.google.com/search?q={query}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    elements = soup.find_all("div", class_="fQtNvd")
    if elements:
        description = elements[0].text
        description1 = elements[1].text
        print(description)
        print(description1)

        # write data
        data = {
            'query': query,
            'info1': description,
            'info2': description1
        }

        file_path = 'scrape_search.json'

        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                existing_data = json.load(file)

            existing_data.append(data)

            with open(file_path, 'w') as file:
                json.dump(existing_data, file, ensure_ascii=False, indent=4)
        else:
            with open(file_path, 'w') as file:
                json.dump([data], file, ensure_ascii=False, indent=4)
        return data
    else:
        return {"error": "arama sonucu bulunamadı."}

"""
@app.get("/scrape_search")
async def scrape_search(query: str):
    main(query)

"""
