text = "X-DSPAM-Confidence:    0.8475"; #input your text here
find_0 = text.find('0')
slice = text[find_0:]
ftext = float(slice)
print(ftext)
