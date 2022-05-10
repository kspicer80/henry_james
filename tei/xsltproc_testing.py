import libxml2
import libxslt

styledoc = libxml2.parsefFile('hj_tots.xsl')
style = libxslt.parseStylesheetDoc(styledoc)
doc = libxml2.parseFile('hj_tots_tei.xml')
result = style.applyStylesheet(doc, None)
style.saveResultToFilename("html_test.html", result, 0)
style.freeStylesheet()
doc.freeDoc()
result.freeDoc()