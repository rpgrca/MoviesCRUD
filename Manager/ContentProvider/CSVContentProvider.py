#    def _track_rooms_load_previous_day(self, filename):
#        """
#        Auxiliar function, load information from previous day.
#        Currently unused.
#        """
#        _ = timezone('Asia/Tokyo')
#        last = {}
#        with open(filename, "r") as input_file:
#            reader = csv.reader(input_file, delimiter='\t')
#            for room_id, _, date, _, followers, viewers, points, diff in reader:
#                if room_id not in last:
#                    last[room_id] = {
#                        "points": points, "date": date, "viewers": viewers,
#                        "followers": followers, "diff": diff
#                    }
#

"""FileContentProvider.py"""

from typing import List, Any
from Manager.ContentProvider.ContentProvider import ContentProvider

class CSVContentProvider(ContentProvider):
    def __init__(self, filename: str):
        super(CSVContentProvider, self).__init__()
        self.__filename = filename

    def get_name(self) -> str:
        return "Archivo CSV"

    def load(self):
        # TODO: Cargar items del archivo
        pass

    def save(self):
        # TODO: Grabar items del archivo
        pass
