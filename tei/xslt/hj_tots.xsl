<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
	xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xpath-default-namespace="http://www.tei-c.org/ns/1.0" xmlns="http://www.w3.org/1999/xhtml"
	version="3.0">
	<xsl:output method="xhtml" html-version="5" omit-xml-declaration="no" include-content-type="no"
		indent="yes"/>

	<xsl:strip-space elements="*"/>
	<!-- The Entire HTML Web Page -->
	<xsl:template match="/">
		<html>
			<head>
				<title>
					<italic>The Turn of the Screw</italic>
				</title>
			</head>
			<body>
				<xsl:apply-templates/>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="div[@type = 'chapter']">
		<div class="chapter">
			<xsl:attribute name="n">
				<xsl:value-of select="@n"/>
			</xsl:attribute>
			<xsl:if test="@type = 'chapter'">
				<h3>
					<xsl:text>Chapter: </xsl:text>
					<xsl:value-of select="@n"/>
				</h3>
			</xsl:if>
			<xsl:apply-templates/>
		</div>
	</xsl:template>

	<xsl:template match="div[@type = 'paragraph']">
		<div class="paragraph">
			<xsl:attribute name="n">
				<xsl:value-of select="@n"/>
			</xsl:attribute>
			<xsl:if test="@type = 'paragraph'">
				<sup>
					<xsl:text>¶</xsl:text>
					<xsl:value-of select="@n"/>
				</sup>
			</xsl:if>
			<xsl:apply-templates/>
		</div>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'douglas']">
		<font color="paleturquoise">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'narrator']">
		<font color="BlueViolet">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'mrsgrose']">
		<font color="Periwinkle">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'miles']">
		<font color="Goldenrod">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'flora']">
		<font color="Green">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'governess']">
		<font color="Indigo">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'mrsgriffin']">
		<font color="yelloworange">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'storygroupmember']">
		<font color="SaddleBrown">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'storygroupmembers']">
		<font color="SlateBlue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//said[@who = 'mrgriffin']">
		<font color="Yellow">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'fire']">
		<font color="maroon">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//date">
		<font color="GreenYellow">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//time">
		<font color="Olive">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-red']">
		<font color="red">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template
		match="//TEI//text//body//div//seg[@ana = 'colors-golden'] | seg[@ana = 'colors-gold']">
		<font color="gold">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-brown']">
		<font color="brown">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-blue']">
		<font color="azure">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-rose']">
		<font color="darkmagenta">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-pink']">
		<font color="pink">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-gray']">
		<font color="gray">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-crimson']">
		<font color="crimson">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-green']">
		<font color="lawngreen">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'touch-figurative']">
		<font color="teal">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'repetition']">
		<font color="mistyrose">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-physical']">
		<font color="magenta">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'touch-physical']">
		<font color="teal">
			<xsl:apply-templates/>
			
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'taste-figurative']">
		<font color="darkgreen">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-figurative']">
		<font color="magenta">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'delay']">
		<font color="lightpink">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-physical']">
		<font color="sienna">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'writing']">
		<font color="aqua">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'weather-figurative']">
		<font color="orange">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'writing letters']">
		<font color="purple">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'weather']">
		<font color="lightpink">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'interruptions']">
		<font color="mediumpurple">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'letters']">
		<font color="bisque">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'fire-figurative']">
		<font color="maroon">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading']">
		<font color="lime">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'book reading']">
		<font color="lime">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision']">
		<font color="magenta">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound']">
		<font color="sienna">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading romance books']">
		<font color="lime">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'epistle']">
		<font color="blueviolet">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'letter reading-figurative']">
		<font color="lime">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'master-nonknowledge']">
		<font color="lightgreen">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'delay-hesitation']">
		<font color="lightpink">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading-figurative']">
		<font color="lime">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading books']">
		<font color="lime">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'imaginative play']">
		<font color="salmon">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-black']">
		<font color="plum">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors']">
		<font color="darksalmon">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'smell-figurative']">
		<font color="Peru">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-figurative']">
		<font color="sienna">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-literal']">
		<font color="magenta">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sight-figurative']">
		<font color="mediumblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'letters writing']">
		<font color="lemonchiffon">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'smell-physical']">
		<font color="Peru">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'fire-figurative delay']">
		<font color="maroon">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading letters']">
		<font color="lime">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sexuality']">
		<font color="royalblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sexuality-figurative']">
		<font color="royalblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sealed senses']">
		<font color="mediumseagreen">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="emph[@rend = 'italics']">
		<em>
			<xsl:apply-templates/>
		</em>
	</xsl:template>
	<xsl:template match="foreign">
		<em>
			<xsl:apply-templates/>
		</em>
	</xsl:template>
</xsl:stylesheet>
