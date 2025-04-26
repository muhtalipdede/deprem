from datetime import datetime, timedelta
import pandas as pd
import requests
import os

def get_earthquake(last_day):
    url = "https://deprem.afad.gov.tr/EventData/GetEventsByFilter"
    last = datetime.now() - timedelta(hours=24 * last_day)
    now = datetime.now()

    request_payload = {
        "EventSearchFilterList": [
            {"FilterType": 1, "Value": "22.4502"},
            {"FilterType": 2, "Value": "52.7088"},
            {"FilterType": 3, "Value": "24.7742"},
            {"FilterType": 4, "Value": "47.6258"},
            {"FilterType": 8, "Value": last.strftime("%Y-%m-%dT%H:%M:%S.%fZ")},
            {"FilterType": 9, "Value": now.strftime("%Y-%m-%dT%H:%M:%S.%fZ")}
        ],
        "Skip": 0,
        "Take": 100000,
        "SortDescriptor": {"field": "eventDate", "dir": "desc"}
    }

    try:
        # API isteği gönderme
        response = requests.post(url, json=request_payload, timeout=60)
        response.raise_for_status()  # HTTP hatalarını kontrol et

        # JSON yanıtını işleme
        response_data = response.json().get("eventList", [])
        if not response_data:
            raise ValueError("API'den boş bir yanıt alındı veya 'eventList' bulunamadı.")

        # Verileri işleme
        data = []
        for earthquake in response_data:
            try:
                date = earthquake["eventDate"]
                address = earthquake["location"]
                magnitude = float(earthquake["magnitude"])
                latitude = float(earthquake["latitude"])
                longitude = float(earthquake["longitude"])
                depth = -float(earthquake["depth"])
                data.append([magnitude, latitude, longitude, date, address, depth])
            except KeyError as e:
                print(f"Veri işleme sırasında bir anahtar hatası oluştu: {e}")
            except ValueError as e:
                print(f"Veri dönüştürme sırasında bir hata oluştu: {e}")

        # DataFrame oluşturma
        df = pd.DataFrame(
            data, columns=['magnitude', 'latitude', 'longitude', 'date', 'address', 'depth']
        )

        today_data = df[df['date'].str.startswith(now.strftime("%Y-%m-%d"))]

        # Veriyi 'datas' klasörüne kaydetme
        save_path = os.path.join("datas", f"earthquake_data_{now.strftime('%Y%m%d')}.csv")
        os.makedirs("datas", exist_ok=True)  # 'datas' klasörü yoksa oluştur
        today_data.to_csv(save_path, index=False, encoding="utf-8")  # CSV olarak kaydet
        print(f"Veri '{save_path}' dosyasına kaydedildi.")

        return df

    except requests.exceptions.RequestException as e:
        print(f"API isteği sırasında bir hata oluştu: {e}")
        return pd.DataFrame(columns=['magnitude', 'latitude', 'longitude', 'date', 'address', 'depth'])

    except ValueError as e:
        print(f"Yanıt işleme sırasında bir hata oluştu: {e}")
        return pd.DataFrame(columns=['magnitude', 'latitude', 'longitude', 'date', 'address', 'depth'])

    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        return pd.DataFrame(columns=['magnitude', 'latitude', 'longitude', 'date', 'address', 'depth'])