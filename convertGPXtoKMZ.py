import gpxpy
import simplekml
import os

def convert_gpx_to_kmz(gpx_file_path, kmz_file_path):
    # 1. Parse the GPX file
    try:
        with open(gpx_file_path, 'r') as gpx_file:
            gpx = gpxpy.parse(gpx_file)
    except FileNotFoundError:
        print(f"Error: The file {gpx_file_path} was not found.")
        return
    except Exception as e:
        print(f"An error occurred while parsing GPX: {e}")
        return

    # 2. Initialize SimpleKML
    kml = simplekml.Kml()

    # 3. Iterate through tracks, segments, and points
    for track in gpx.tracks:
        for segment in track.segments:
            # Extract coordinates as (longitude, latitude, optional elevation)
            coords = []
            for point in segment.points:
                coords.append((point.longitude, point.latitude, point.elevation))
            
            # Create a LineString in the KML
            linestring = kml.newlinestring(name=track.name or "GPX Track")
            linestring.coords = coords
            # Optional: Style the line (color is aabbggrr in hex)
            linestring.style.linestyle.color = simplekml.Color.rgb(255, 0, 0) # Red
            linestring.style.linestyle.width = 3

    # 4. Save as KMZ
    # simplekml handles the zipping automatically when the extension is .kmz
    try:
        kml.savekmz(kmz_file_path)
        print(f"Success! KMZ saved to: {kmz_file_path}")
    except Exception as e:
        print(f"An error occurred while saving KMZ: {e}")

if __name__ == "__main__":
    # Example Usage
    input_gpx = "input.gpx"     # Replace with your file name
    output_kmz = "output.kmz"
    
    convert_gpx_to_kmz(input_gpx, output_kmz)