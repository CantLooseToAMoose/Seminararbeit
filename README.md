# Seminararbeit


First install the "shp2walls" project from https://github.com/laskama/shp2walls .

When you get an Error concerning
- A GDAL API version must be specified. Provide a path to gdal-config using a GDAL_CONFIG environment variable or use a GDAL_VERSION environment variable.

loading this project, try using:

<code>
pip install pipwin
<br>
pipwin install gdal<br>
pipwin install fiona<br>
pip install geopandas
</code>


Virtual environment is recommended.