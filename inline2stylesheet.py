#!/usr/bin/python
from HTMLParser import HTMLParser
class inline2stylesheet(HTMLParser):
    """this class extends the HTMLParser to extract the css from the style attributes of html elements, and output them in a generated css file"""
    stylesDict = {}
    tagNest = []
    def handle_starttag(self, tag, attrs):
        self.tagNest.append(tag)
        if(len(attrs) <= 0): return
        attrDict = dict(attrs)
        if(not attrDict.has_key('style')): return
        styleString = attrDict['style']
        styleList = [rule.strip() for rule in styleString.split(';') if rule.strip()!='']
        styleList.sort()
        styleKey = ';'.join(styleList)
        if(not self.stylesDict.has_key(styleKey)):
            self.stylesDict[styleKey] = []
        if(not self.stylesDict[styleKey].count(styleString)):
            self.stylesDict[styleKey].append(styleString);
    def handle_endtag(self, tag):
        self.tagNest.pop();
    def printStyles(self):
        for key in self.stylesDict.keys():
            print key
if __name__=="__main__":
    f = file('index.html')
    p = inline2stylesheet()
    p.feed(f.read())
    p.printStyles()
