#!/usr/bin/env python

"""
Python class example.
"""

###############################################################################
#######################   Element and Its Sub Classes   #######################
###############################################################################

class Element(object):
	# Tag Name
	tag = ''

	# Indentation to concatenate for each nested Element.
	indentation = '    '

	# Attributes
	attributes = ''

	# Constructor
	# Source: http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
	def __init__(self, content=None, **kwargs):
		if content == None: # If no content
			self.content = []	# Make empty list
		else:
			self.content = [content]	# add content to list
		for key, value in kwargs.items():	# add attributes to attribute string.
			self.attributes = " " + key + "=" + "\"" + value + "\"" + self.attributes

	# Appends content to the Element's content
	def append(self, content):
		# Add content to the self.content list.
		self.content.append(content)

	# Renders the tag and the strings in the content
	def render(self, file_out, ind=0):
		# Print tag
		file_out.write(self.indentation * ind + "<" + self.tag + self.attributes + ">\n")
		for item in self.content:	# Check if the item is an object or a string
			if isinstance(item, str):
				file_out.write(self.indentation * (ind+1) + item + '\n') # If string, print content
			else:
				item.render(file_out, ind+1) # If an object, render that object using a recursive render call (nesting each object)
		file_out.write(self.indentation * ind + "</" + self.tag + ">\n")

# Subclasses that extends Element class.
class Html(Element):
	tag = 'html'
	def render(self, file_out, ind=0): # override the Element render class to include DOCTYPE
		file_out.write('<!DOCTYPE html>\n')
		Element.render(self, file_out, ind)

class Body(Element): 
	tag = 'body'

class P(Element):
	tag = 'p'

class Head(Element):
	tag = 'head'

class OneLineTag(Element): # subclass of Element class to print on one line.
	def render(self, file_out, ind=0): # Override render so that the element prints on one line.
		file_out.write(self.indentation * ind + "<" + self.tag + self.attributes + ">")
		for item in self.content:	
			if isinstance(item, str):
				file_out.write(item)
			else:
				item.render(file_out, ind)
		file_out.write("</" + self.tag + ">\n")

class Title(OneLineTag):
	tag = 'title'

class SelfClosingTag(Element):
	def render(self, file_out, ind=0): # override render method; shouldn't have any string content.
		file_out.write(self.indentation * ind + "<" + self.tag + self.attributes + " />\n")

class Hr(SelfClosingTag):
	tag = 'hr'

class Br(SelfClosingTag):
	tag = 'br'

class A(OneLineTag):
	def __init__(self, link, content):
		Element.__init__(self, content, href=link)	# replace attributes with link.
	tag = 'a'	

class Ul(Element):
	tag = 'ul'

class Li(Element):
	tag = 'li'

class H(OneLineTag):
	header_number = ''
	tag = 'h'
	def __init__(self, header_level, content=None, **kwargs):
		Element.__init__(self, content, **kwargs)
		self.header_number = str(header_level)
		self.tag += self.header_number
		
class Meta(SelfClosingTag):
	tag = 'meta'