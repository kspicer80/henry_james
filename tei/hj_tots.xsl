<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns:math="http://www.w3.org/2005/xpath-functions/math"
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
				<author>Henry James</author>
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

	<xsl:template match="//TEI//text//body//div//said[@who='narrator']">
		<font color='BlueViolet'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='mrsgrose']">
		<font color='Periwinkle'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='miles']">
		<font color='pink'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='flora']">
		<font color='green'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='governess']">
		<font color='Indigo'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='mrsgriffin']">
		<font color='Orange'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='storygroupmember']">
		<font color='SaddleBrown'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='storygroupmembers']">
		<font color='SlateBlue'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='mrgriffin']">
		<font color='Yellow'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//p//seg[@ana='touch-figurative']">
		<font color='SlateBlue'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//p//seg[@ana='fire']">
		<font color='red'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>
</xsl:stylesheet>
