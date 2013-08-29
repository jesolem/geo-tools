import json
import shapefile
import argparse

"""
Simple CLI for converting Shapefiles to GeoJSON.
Uses snippets from here http://geospatialpython.com/2013/07/shapefile-to-geojson.html
and the PyShp module https://pypi.python.org/pypi/pyshp/
"""

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("shapefile", help="filename of shapefile to convert")
    parser.add_argument("--jsonfile", help="filename of output file (optional, default is same as input with .json)")
    args = parser.parse_args()

    # read the shapefile
    reader = shapefile.Reader(args.shapefile)
    fields = reader.fields[1:]
    field_names = [field[0] for field in fields]
    buffer = []
    for sr in reader.shapeRecords():
        atr = dict(zip(field_names, sr.record))
        geom = sr.shape.__geo_interface__
        buffer.append(dict(type="Feature", geometry=geom, properties=atr)) 
    
    # write the GeoJSON file
    if args.jsonfile:
        outfile = args.jsonfile
    else:
        outfile = args.shapefile+".json"
    
    with open(outfile, "w") as geojson:
        geojson.write(json.dumps({"type": "FeatureCollection", "features": buffer}, indent=2) + "\n")
