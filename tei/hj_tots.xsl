<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xpath-default-namespace="http://www.tei-c.org/ns/1.0"
	xmlns="http://www.w3.org/1999/xhtml"
	version="3.0">
	<xsl:output method="xhtml" html-version="5" omit-xml-declaration="no"
		include-content-type="no" indent="yes"/>

	<xsl:strip-space elements="*"/>
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

	<xsl:template match="div[@type='chapter']">
		<p>
			<xsl:attribute name='type'>
				<xsl:text>Chapter: </xsl:text><xsl:value-of select="@n"/>
			</xsl:attribute>
			<xsl:apply-templates/>
		</p>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='douglas']">
			<font color='paleturquoise'>
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
		<font color='Goldenrod'>
			<xsl:apply-templates/></font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who='flora']">
		<font color='Green'>
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

	<xsl:template match="//TEI//text//body//div//seg[@ana='touch-figurative']">
		<font color='tomato'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='fire']">
		<font color='maroon'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//date">
		<font color='DarkSlateGray'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//time">
		<font color='Olive'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-red']">
		<font color='red'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-golden' | @ana='colors-gold']">
		<font color='gold'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-brown']">
		<font color='brown'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-blue']">
		<font color='azure'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-rose']">
		<font color='darkmagenta'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-pink']">
		<font color='pink'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-gray']">
		<font color='gray'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-crimson']">
		<font color='crimson'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana='colors-green']">
		<font color='lawngreen'>
			<xsl:apply-templates/>
		</font>
	</xsl:template>

<xsl:template match="//TEI//text//body//div//seg[@ana='touch-figurative']">
	<font color='lightgoldenrodyellow'>
		<xsl:apply-templates/>
	</font>
</xsl:template>





<xsl:template match="//TEI//text//body//div//seg[@ana='touch-figurative'"><font color='lightblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='repetition'"><font color='darkorange'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='touch-figurative touch-literal'"><font color='forestgreen'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision-physical'"><font color='gray'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='touch-physical'"><font color='lightgoldenrodyellow'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='taste-figurative'"><font color='seagreen'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision-figurative'"><font color='rosybrown'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='delay'"><font color='moccasin'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound-physical'"><font color='azure'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='writing'"><font color='snow'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='weather-figurative'"><font color='lightsalmon'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='delay sound-physical'"><font color='whitesmoke'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound-figurative sound-literal'"><font color='slategray'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='writing letters'"><font color='rosybrown'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='weather'"><font color='lightseagreen'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='interruptions'"><font color='magenta'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='letters'"><font color='darkgray'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='fire touch-physical'"><font color='deeppink'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='fire-figurative'"><font color='darkslategrey'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='reading'"><font color='rebeccapurple'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='book reading'"><font color='ivory'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision'"><font color='dimgrey'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound'"><font color='lavenderblush'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='colors-white'"><font color='olive'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='reading romance books'"><font color='lemonchiffon'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='epistle'"><font color='lightgray'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='letter reading-figurative'"><font color='lightcyan'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='touch'"><font color='moccasin'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision-figurative touch-figurative'"><font color='beige'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound-figurative sound-physical vision-physical'"><font color='darkorchid'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='fire delay'"><font color='violet'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='master-nonknowledge'"><font color='darkturquoise'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='delay-hesitation'"><font color='steelblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='reading-figurative'"><font color='moccasin'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision-physical vision-figurative'"><font color='darkorange'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='reading books'"><font color='oldlace'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='imaginative play'"><font color='sienna'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='colors-black'"><font color='lightpink'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision-figurative vision-physical'"><font color='paleturquoise'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='colors'"><font color='darkslateblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='smell-figurative'"><font color='lightgray'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound-physical vision-physical'"><font color='gainsboro'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound-figurative'"><font color='sienna'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision-literal'"><font color='palevioletred'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound-physical sound-figurative'"><font color='cornflowerblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sight-figurative'"><font color='darkgreen'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='letters writing'"><font color='cyan'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision-physical touch-figurative'"><font color='black'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='smell-physical'"><font color='rosybrown'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound-figurative sound-physical'"><font color='turquoise'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='reading writing letters'"><font color='mediumseagreen'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='fire-figurative delay'"><font color='darkorange'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='reading letters'"><font color='darkblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vison-physical'"><font color='limegreen'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='physical-figurative'"><font color='cadetblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sexuality'"><font color='deeppink'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='touch-physical sound-physical'"><font color='powderblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sexuality-figurative'"><font color='lightcyan'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='fire-figurative vision-figurative'"><font color='deepskyblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sealed senses'"><font color='cornflowerblue'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='vision-physical touch-physical'"><font color='slategrey'><xsl:apply-templates/></font></xsl:template>
<xsl:template match="//TEI//text//body//div//seg[@ana='sound-physical repetition'"><font color='silver'><xsl:apply-templates/></font></xsl:template>
	<xsl:template match="p">
		<p>
			<xsl:apply-templates/>
		</p>
	</xsl:template>
</xsl:stylesheet>
