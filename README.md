# gpx-convert-kmz

### create your venv
`python3 -m venv venv`


### activate the venv
`source venv/bin/activate`


### install the requirements
`pip install gpxpy simplekml`


### call the function to perform the conversion from GPX to KMZ
`python3`

`import convertGPXtoKMZ`

`x = convertGPXtoKMZ.convert_gpx_to_kmz("./path/to/my/file.gpx", "./path/to/output/file.kmz")`

