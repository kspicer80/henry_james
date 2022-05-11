import lxml.html
from lxml import etree

# Following http://makble.com/convert-xml-to-html-with-lxml-xslt-in-python
xslt_doc = etree.parse('hj_tots.xsl')
xslt_transformer = etree.XSLT(xslt_doc)

source_doc = etree.parse('hj_tots_tei.xml')
output_doc = xslt_transformer(source_doc)

print(str(output_doc))
output_doc.write('lxml_html_test.html', pretty_print=True)