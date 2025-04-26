import folium
import folium.plugins


def get_magnitude_map(df, fault_line):
    # Latitude ve Longitude sütunlarında eksik değerleri kontrol et
    if df['latitude'].isnull().any() or df['longitude'].isnull().any():
        raise ValueError("DataFrame'de eksik latitude veya longitude değerleri var.")
    # Harita oluşturma
    magnitude_map = folium.Map(location=[df['latitude'].mean(), df['longitude'].mean()], zoom_start=7)

    # Deprem noktalarını haritaya ekleme
    for index, row in df.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            radius=row['magnitude'] * 2,
            popup=str(row['magnitude']) + ' M' + ' ' + row['address'],
            color='#3186cc',
            fill=True,
            fill_color='#3186cc'
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