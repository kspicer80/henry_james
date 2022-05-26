#all thanks for this go to Adrien Barbaresi and his blog post here:  https://adrien.barbaresi.eu/blog/validating-tei-xml-python.html
import requests
from io import StringIO
from lxml import etree

schema = requests.get("http://www.tei-c.org/release/xml/tei/custom/schema/relaxng/tei_simplePrint.rng").text
schema = schema.replace('<?xml version="1.0" encoding="utf-8"?>', '<?xml version="1.0"?>', 1)

myxml = etree.parse(StringIO(schema))
tei_relaxng = etree.RelaxNG(myxml)
# open a file and parse it
filename_path = r'tei\hj_tots_tei.xml'
mytree = etree.parse(filename_path)
