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
		<p>
			<xsl:attribute name="type">
				<xsl:value-of select="@n"/>
			</xsl:attribute>
				<xsl:if test="@type='chapter'">
					<span class='chapter_title'>
						<font size='30'>
							<xsl:text>Chapter: </xsl:text>
							<xsl:value-of select="@n"/>
						</font>
					</span>
				</xsl:if>

			<xsl:apply-templates/>
		</p>
	</xsl:template>
	
	<xsl:template match="/TEI/text/body/div/div">
		<p>
		<xsl:attribute name='paragraph'>
			<xsl:value-of select="@n"/>
		</xsl:attribute>
		<xsl:if test="@type='paragraph'">
			<span class='pilcrow'>¶</span>
		</xsl:if>
		<xsl:apply-templates select="@n | node()"/>
		</p>
		
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
		<font color="Orange">
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

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'touch-figurative']">
		<font color="teal">
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
		<font color="lightgoldenrodyellow">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="//TEI//text//body//div//seg[@ana = 'touch-figurative']">
		<font color="seashell">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'repetition']">
		<font color="mistyrose">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'touch-figurative touch-literal']">
		<font color="royalblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-physical']">
		<font color="palegoldenrod">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'touch-physical']">
		<font color="goldenrod">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'taste-figurative']">
		<font color="darkgreen">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-figurative']">
		<font color="wheat">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'delay']">
		<font color="lightpink">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-physical']">
		<font color="darkgoldenrod">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'writing']">
		<font color="whitesmoke">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'weather-figurative']">
		<font color="orange">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'delay sound-physical']">
		<font color="navy">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-figurative sound-literal']">
		<font color="darkblue">
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
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'fire touch-physical']">
		<font color="dodgerblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'fire-figurative']">
		<font color="lime">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading']">
		<font color="silver">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'book reading']">
		<font color="bisque">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision']">
		<font color="lightgreen">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound']">
		<font color="pink">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-white']">
		<font color="whitesmoke">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading romance books']">
		<font color="mistyrose">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'epistle']">
		<font color="blueviolet">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'letter reading-figurative']">
		<font color="tan">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'touch']">
		<font color="darkslateblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-figurative touch-figurative']">
		<font color="royalblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template
		match="//TEI//text//body//div//seg[@ana = 'sound-figurative sound-physical vision-physical']">
		<font color="lavenderblush">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'fire delay']">
		<font color="gold">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'master-nonknowledge']">
		<font color="lightgreen">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'delay-hesitation']">
		<font color="antiquewhite">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading-figurative']">
		<font color="deeppink">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-physical vision-figurative']">
		<font color="mediumpurple">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading books']">
		<font color="skyblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'imaginative play']">
		<font color="mistyrose">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors-black']">
		<font color="plum">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-figurative vision-physical']">
		<font color="darkslateblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'colors']">
		<font color="darksalmon">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'smell-figurative']">
		<font color="moccasin">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-physical vision-physical']">
		<font color="darkmagenta">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-figurative']">
		<font color="goldenrod">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-literal']">
		<font color="lavender">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-physical sound-figurative']">
		<font color="red">
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
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-physical touch-figurative']">
		<font color="cornflowerblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'smell-physical']">
		<font color="silver">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-figurative sound-physical']">
		<font color="crimson">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading writing letters']">
		<font color="olive">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'fire-figurative delay']">
		<font color="blueviolet">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'reading letters']">
		<font color="wheat">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vison-physical']">
		<font color="midnightblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'physical-figurative']">
		<font color="plum">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sexuality']">
		<font color="royalblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'touch-physical sound-physical']">
		<font color="mediumblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sexuality-figurative']">
		<font color="darkmagenta">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'fire-figurative vision-figurative']">
		<font color="tomato">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sealed senses']">
		<font color="mediumseagreen">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'vision-physical touch-physical']">
		<font color="cornflowerblue">
			<xsl:apply-templates/>
		</font>
	</xsl:template>
	<xsl:template match="//TEI//text//body//div//seg[@ana = 'sound-physical repetition']">
		<font color="chartreuse">
			<xsl:apply-templates/>
		</font>
	</xsl:template>

	<xsl:template match="p">
		<p>
			<xsl:apply-templates/>
		</p>
	</xsl:template>
	
	<xsl:template match="/TEI/text[1]/body[1]/div[1]/div[2]/p[1]/said[1]/emph[1]">
		<span class='emph'><xsl:apply-templates/></span>
	</xsl:template>
	
	<xsl:template match='foreign'>
		<span class='emph'><xsl:apply-templates/></span>
	</xsl:template>
</xsl:stylesheet>
