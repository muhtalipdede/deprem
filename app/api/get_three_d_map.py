import plotly.graph_objects as go
from app.api.get_earthquake import get_earthquake

def get_three_d_map():
    # Deprem verilerini al
    data = get_earthquake(7)

    # Verilerin doğruluğunu kontrol et
    if data.empty:
        raise ValueError("DataFrame is empty. No data available for 3D graph.")
    if not all(col in data.columns for col in ["latitude", "longitude", "magnitude", "depth"]):
        raise ValueError("DataFrame must contain 'latitude', 'longitude', 'magnitude', and 'depth' columns.")
    if not all(data[col].dtype.kind in 'fi' for col in ["latitude", "longitude", "magnitude", "depth"]):
        raise ValueError("Latitude, Longitude, Magnitude, and Depth columns must be of type float or int.")

    data = data[data['magnitude'] > 4]

    # 3D scatter plot oluştur
    fig = go.Figure()

    # Ana deprem noktalarını ekle
    fig.add_trace(go.Scatter3d(
        x=data["longitude"],  # Boylam
        y=data["latitude"],   # Enlem
        z=-data["depth"],     # Derinlik (negatif değerler yerin altını ifade eder)
        mode='markers',
        marker=dict(
            size=data["magnitude"] * 2,  # Büyüklüğe göre nokta boyutu
            color=data["depth"],        # Derinliğe göre renk
            colorscale='Viridis',       # Renk skalası
            opacity=0.8
        ),
        text=[f"Magnitude: {mag}<br>Depth: {depth} km" for mag, depth in zip(data["magnitude"], data["depth"])],  # Popup metni
        name="Earthquakes"
    ))

    # Dalga efektlerini ekle
    for index, row in data.iterrows():
        for i in range(1, 4):  # 3 dalga halkası
            fig.add_trace(go.Scatter3d(
                x=[row["longitude"]],  # Boylam
                y=[row["latitude"]],   # Enlem
                z=[-row["depth"]],     # Derinlik
                mode='markers',
                marker=dict(
                    size=row["magnitude"] * 2 * i,  # Dalga yarıçapı büyüklüğe ve iterasyona bağlı
                    color='rgba(255, 0, 0, 0.2)',   # Kırmızı renk, şeffaflık 0.2
                    opacity=0.2                     # Dalga şeffaflığı
                ),
                name=f"Wave {i} (Magnitude: {row['magnitude']})"
            ))

    # Grafik düzenlemeleri
    fig.update_layout(
        title="3D Earthquake Visualization with Wave Effects",
        scene=dict(
            xaxis_title="Longitude",
            yaxis_title="Latitude",
            zaxis_title="Depth (km)",
            zaxis=dict(autorange="reversed")  # Derinlik eksenini ters çevir
        )
    )

    # Grafiği HTML olarak döndür
    return fig.to_html(full_html=False)