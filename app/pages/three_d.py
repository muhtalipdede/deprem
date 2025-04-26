from flask import render_template
from app.api.get_three_d_map import get_three_d_map

def three_d_page():
    try:
        # 3D haritayı oluştur
        _three_d_map = get_three_d_map()
    except ValueError as e:
        print(f"3D harita oluşturulurken bir hata oluştu: {e}")
        _three_d_map = """
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <strong class="font-bold">Hata:</strong>
            <span class="block sm:inline">3D harita oluşturulamadı. Lütfen daha sonra tekrar deneyin.</span>
        </div>
        """
    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")
        _three_d_map = """
        <div class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
            <strong class="font-bold">Hata:</strong>
            <span class="block sm:inline">Beklenmeyen bir hata oluştu. Lütfen daha sonra tekrar deneyin.</span>
        </div>
        """

    # Şablonu render et
    return render_template('three_d.html', three_d_map=_three_d_map)