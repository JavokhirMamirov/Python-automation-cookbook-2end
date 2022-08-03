from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import xmltodict
from Chapter04.gps_conversion import exif_to_decimal, rdf_to_decimal

image1 = Image.open('images/photo-dublin-a1.jpg')

height = image1.height
width = image1.width
format = image1.format

exif_info_1 = {TAGS.get(tag, tag):value for tag, value in image1._getexif().items()}

# print(exif_info_1['Model'])
# print(exif_info_1['LensModel'])
# print(exif_info_1['DateTimeOriginal'])

image2 = Image.open('images/photo-dublin-a2.png')
# print(image2.height)
# print(image2.width)
# print(image2.format)

xmp_info = xmltodict.parse(image2.info['XML:com.adobe.xmp'])
# print(xnp_info)
rdf_info_2 = xmp_info['x:xmpmeta']['rdf:RDF']['rdf:Description']
# print(rdf_info_2['tiff:Model'])
# print(rdf_info_2['exifEX:LensModel'])
# print(rdf_info_2['xmp:CreateDate'])

gps_info_1 = {GPSTAGS.get(tag, tag):value
              for tag, value in exif_info_1['GPSInfo'].items()
              }

# print(gps_info_1)

# print(exif_to_decimal(gps_info_1))
# print(rdf_to_decimal(rdf_info_2))

image3 = Image.open('images/photo-dublin-b.png')
xmp_info = xmltodict.parse(image3.info['XML:com.adobe.xmp'])
rdf_info_3 = xmp_info['x:xmpmeta']['rdf:RDF']['rdf:Description']
print(rdf_info_3['xmp:CreateDate'])
print(rdf_to_decimal(rdf_info_3))