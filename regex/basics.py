import re

text="abc123 XYZ !@#"
numbers=re.findall(r"\d",text) #any digits
print(re.findall(r"\d",text))  
print(re.findall(r"\D",text)) #any non digits
print(re.findall(r"\s",text)) #space match
print(re.findall(r"\w",text)) #any word match
print(re.findall(r"\W",text)) #non word match
print(re.findall(r"[abcd]",text)) #any of abcd
print(re.findall(r"[^abcd]",text)) #except abcd
print(re.findall(r"[XYa]",text))  #Any of XYa  follows original order from text
print(re.findall(r"[X$]",text))  #end of line

#quantifiers
text = "a ab abb abbb abbbb"
#? zero or 1 time
print(re.findall(r"ab?",text))  #b is previous char of ? should have one or zero match

#* 0 or more
print(re.findall(r"ab*",text))  # a,ab,abb,abbb,abbbb  b zero or more

#+ 1 or more
print(re.findall(r"ab+",text))  #b at least one or more times

#{n} exact n times
print(re.findall(r"ab{2}",text)) #b 2 two times 

#{n,} n or more times
print(re.findall(r"ab{2,}",text)) #b 2 or more times

#{n,m} between n and m 
print(re.findall(r"ab{2,4}",text)) #b 2 to 4 times

"""anchors"""
text = "hello world\nhello there\nsay hello"

# ^ - start of string/line
print(re.findall(r'^hello', text))  # ['hello'] - only first line

# $ - end of string/line
print(re.findall(r'hello$', text))  # []-no line ends with 'hello'-after end of the line and before \n.
                                    # so say hello end of the line -hello and before new line is none 

# \b - word boundary
print(re.findall(r'\bhello\b', text))  # ['hello', 'hello', 'hello'] - all 'hello' as whole words