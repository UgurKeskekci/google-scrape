import requests
import json
from bs4 import BeautifulSoup
import os




# input
query = input("Enter your query: ")

# Google search
url = f"https://www.google.com/search?q={query}"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}

# request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

if "hava durumu" in query or "hava nasil" in query or "weather" in query or "temperature" in query:
    elements = soup.find_all("div", class_="eKPi4")
    if elements:
        location = elements[0].text
        print(location)
    else:
        print("Hava durumu sonucu bulunamadı.")


    temperature = soup.find_all("div", class_="wob_dcp")
    if elements:
        temp = temperature[0].text
        print(temp)
    else:
        print("Hava durumu sonucu bulunamadı.")


    data = {
        'query': query,
        'location': location,
        'temperature': temp
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
elif "trafik" in query or "yol durumu" in query or "traffic" in query or "road" in query:
    # elementler
    elements = soup.find_all("div", class_="UBoxCb vdQmEd EtOod pkphOe")
    if elements:
        description = elements[0].text
        print(description)


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
    else:
        print("Arama sonucunda trafik durumu bilgisi bulunamadı.")
elif "otel" in query or "hotel" in query or "konaklama" in query or "accommodation" in query or "motel" in query:

    elements = soup.find_all("div", class_="fQtNvd")
    if elements:
        description = elements[0].text
        description1 = elements[1].text
        print(description)


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
    else:
        print("Arama sonucunda otel bilgisi bulunamadı.")
elif "biografi" in query or "kim" in query or "kimdir" in query or "biography" in query:
    elements = soup.find_all("div", class_="kno-rdesc")
    if elements:
        info = elements[0].span.text
        print(info)


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
        print("Arama sonucu bulunamadı.")
elif "uçuş" in query or "flight" in query or "flights" in query:
    elements = soup.find_all("a", class_="ikUyY a-no-hover-decoration")
    if elements:
        flights = elements[0].text
        print(flights)


        data = {
            'query': query,
            'flights': flights
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
        print("Uçuş bulunamadı.")
else:
    print("I'm sorry, I don't understand your query.")
