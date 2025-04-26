class city:
    """
    City model class to represent a city in the database.
    """
    def __init__(self, id, name, country, population, lat, lon):
        self.id = id
        self.name = name
        self.country = country
        self.population = population
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"City(id={self.id}, name={self.name}, country={self.country}, population={self.population})"

    def __repr__(self):
        return self.__str__()

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "country": self.country,
            "population": self.population,
            "lat": self.lat,
            "lon": self.lon
        }

    @staticmethod
    def from_json(json):
        return city(
            json["id"],
            json["name"],
            json["country"],
            json["population"],
            json["lat"],
            json["lon"]
        )