from skyfield.api import load

def get_planet_position(planet_name='mars', year=2025, month=7, day=7):
    planets = load('de421.bsp')
    ts = load.timescale()

    t = ts.utc(year, month, day)
    earth = planets['earth']
    planet = planets[planet_name]

    astrometric = earth.at(t).observe(planet)
    ra, dec, distance = astrometric.radec()

    return {
        'right_ascension': ra.hours,
        'declination': dec.degrees,
        'distance_km': distance.km
    }

