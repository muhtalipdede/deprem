
from datetime import datetime

class DatetimeHelper:
    @staticmethod
    def get_current_datetime():
        return datetime.now()
    
    @staticmethod
    def get_current_datetime_str():
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    @staticmethod
    def format_datetime_str(datetime_str):
        return datetime.strptime(datetime_str, '%Y-%m-%dT%H:%M:%S').strftime('%d/%m/%Y %H:%M:%S')
