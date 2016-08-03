def city_info(city_name, country_name, population=None):
    """Return a single string in the form of City, Country."""
    if population:
        info = city_name + ", " + country_name + " - " + str(population)
    else:
        info = city_name + ", " + country_name
    return info.title()
