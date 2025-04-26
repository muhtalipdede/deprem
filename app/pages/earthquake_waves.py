from flask import render_template
from app.api.get_earthquake import get_earthquake
from app.api.get_fault_line import get_fault_line
from app.api.get_magnitude_waves_map import get_magnitude_waves_map

def earthquake_waves_page():
    try:
        # Deprem verilerini al
        df = get_earthquake(7)
        
        # Fay hattı verilerini al
        fault_line = get_fault_line()
        
        # Haritayı oluştur
        _magnitude_map = get_magnitude_waves_map(df=df, fault_line=fault_line)
    except ValueError as e:
        print(f"Harita oluşturulurken bir hata oluştu: {e}")
        _magnitude_map = """
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <strong class="font-bold">Hata:</strong>
            <span class="block sm:inline">Harita oluşturulamadı. Lütfen daha sonra tekrar deneyin.</span>
        </div>
        """
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        _magnitude_map = """
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <strong class="font-bold">Hata:</strong>
            <span class="block sm:inline">Beklenmeyen bir hata oluştu. Lütfen daha sonra tekrar deneyin.</span>
        </div>
        """

    # Şablonu render et
    return render_template("earthquake_waves.html", magnitude_map=_magnitude_map)