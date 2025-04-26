import folium
import folium.plugins
import datetime


def get_magnitude_waves_map(df, fault_line):
    # Latitude ve Longitude sütunlarında eksik değerleri kontrol et
    if df['latitude'].isnull().any() or df['longitude'].isnull().any():
        raise ValueError("DataFrame'de eksik latitude veya longitude değerleri var.")
    
    # Sadece 4'ten büyük depremleri filtrele
    df = df[df['magnitude'] > 4]
    
    # Harita oluşturma
    magnitude_map = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=7)

    # Animasyon için GeoJSON formatında veri oluşturma
    features = []
    for index, row in df.iterrows():
        # Depremin büyüklüğüne göre dalga sayısını ve rengini belirle
        if 4 <= row['magnitude'] < 5:
            wave_count = 3
            wave_color = "#ffff00"  # Sarı
        elif 5 <= row['magnitude'] < 6:
            wave_count = 5
            wave_color = "#ffa500"  # Turuncu
        elif 6 <= row['magnitude']:
            wave_count = 10
            wave_color = "#ff0000"  # Kırmızı
        else:
            wave_count = 0
            wave_color = "#ffffff"  # Beyaz (varsayılan)

        # Dalga halkalarını ekle
        for i in range(1, wave_count + 1):  # Dalga sayısı kadar iterasyon
            features.append({
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [row['longitude'], row['latitude']]
                },
                "properties": {
                    "time": (datetime.datetime.now() + datetime.timedelta(seconds=i * 2)).isoformat(),
                    "style": {
                        "color": wave_color,
                        "radius": row['magnitude'] * 2 * i,
                        "fillOpacity": 0.4
                    },
                    "icon": "circle"
                }
            })

    # TimestampedGeoJson ile animasyonlu dalgaları ekleme
    folium.plugins.TimestampedGeoJson(
        {
            "type": "FeatureCollection",
            "features": features
        },
        period="PT2S",  # Her dalga 2 saniyede bir gösterilecek
        add_last_point=True,
        auto_play=True,
        loop=True
    ).add_to(magnitude_map)

    # Fay hattını haritaya ekleme
    folium.GeoJson(
        fault_line,
        name='geojson',
        style_function=lambda feature: {
            'fillColor': '#ff0000',
            'color': '#ff0000',
            'weight': 1,
            'dashArray': '5, 5',
        }
    ).add_to(magnitude_map)

    # Ek harita katmanları ekleme
    folium.TileLayer(
        tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
        attr='Esri',
        name='Esri Satellite',
        overlay=True,
        control=True,
        show=False
    ).add_to(magnitude_map)

    # Kullanıcı konumunu gösterme
    folium.plugins.LocateControl(
        drawCircle=False,
        showPopup=False,
        locateOptions={'maxZoom': 10}
    ).add_to(magnitude_map)

    # Katman kontrolü ekleme
    folium.LayerControl().add_to(magnitude_map)

    # Tam ekran modu ekleme
    folium.plugins.Fullscreen(
        position='topright',
        title='Expand me',
        title_cancel='Exit me',
        force_separate_button=True
    ).add_to(magnitude_map)

    return magnitude_map._repr_html_()