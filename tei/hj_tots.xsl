<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    xpath-default-namespace="http://www.tei-c.org/ns/1.0"
    xmlns="http://www.w3.org/1999/xhtml"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:output method="xhtml" html-version="5" omit-xml-declaration="no" 
        include-content-type="no" indent="yes"/>
    
    <xsl:template match="/">
        <html>
            <head>
                <link rel="stylesheet" href="hj_tots.css"/>
                <title>Title goes here</title>
            </head>
            <body>
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>
        
    <xsl:template match="//said">
        <p>
            <xsl:if test="@who='governess'">
                <text><xsl:attribute name='class'>governess</xsl:attribute></text>
            </xsl:if>
        </p>
    </xsl:template>
</xsl:stylesheet>