import json


class FeatureCollection(object):
    """
    Class for storing points and paths in GeoJSON.
    
    Generates GeoJSON compatible with GitHub's map rendering.
    https://help.github.com/articles/mapping-geojson-files-on-github
    
    Styling and markers can be passed in the properties dict.
    """
    
    def __init__(self):
        self.features = []
        
    def add_point(self, lat, lon, properties={}):
        """ Add point to list of features. """
        
        # create a new point feature
        point = {}
        point["type"] = "Feature"
        point["properties"] = properties
        point["geometry"] = {"type": "Point", "coordinates": [lon, lat]}
        
        self.features.append(point)
    
    def add_path(self, lat_list, lon_list, properties={}):
        """ Add path as a LineString object. """
        
        # create list of coordinates
        coord_list = map(list, zip(lon_list, lat_list))
        
        # create a new path feature
        path = {}
        path["type"] = "Feature"
        path["geometry"] = {"type": "LineString", "coordinates": coord_list}
        path["properties"] = properties
        
        self.features.append(path)
    
    def add_polygon(self, lat_list, lon_list, properties={}):
        """ Add a single polygon (no holes). """
        
        # create list of coordinates
        coord_list = map(list, zip(lon_list, lat_list))
        
        # create a new path feature
        poly = {}
        poly["type"] = "Feature"
        poly["geometry"] = {"type": "Polygon", "coordinates": [coord_list]}
        poly["properties"] = properties
        
        self.features.append(poly)
    
    def save(self, filename):
        """ Save the features to GeoJSON file. """
        json_data = {"type": "FeatureCollection", "features": self.features}
        with open(filename, 'w') as f:
            f.write(json.dumps(json_data, indent=2))
    
    def dumps(self):
        """ Return GeoJSON as string. """
        return json.dumps({"type": "FeatureCollection", "features": self.features}, indent=2)
    
    def load(self, filename):
        """ Load features from file. """
        with open(filename, 'r') as f:
            json_data = json.loads(f.read())
        self.features = json_data['features']
    
    def __add__(self, other):
        """ Add two feature collections. """
        res = self.__class__()
        res.features = self.features + other.features
        return res
