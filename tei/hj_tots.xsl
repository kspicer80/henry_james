<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xpath-default-namespace="http://www.tei-c.org/ns/1.0"
	xmlns="http://www.w3.org/1999/xhtml"
	version="3.0">

	<xsl:output method="xhtml" html-version="5" omit-xml-declaration="no"
		include-content-type="no" indent="yes"/>

		<!-- The Entire HTML Web Page -->
	<xsl:template match="/">
		<html>
			<head>
				<title><italic>The Turn of the Screw</italic></title>
			</head>
			<body>
				<xsl:apply-templates/>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='douglas']">
			<font color='pink'>
				<xsl:apply-templates/></font>
	</xsl:template>
</xsl:stylesheet>
