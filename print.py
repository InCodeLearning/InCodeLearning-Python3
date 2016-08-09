# This is a summary of python print command based on the book "Learn Python the hardway". 
# This is most useful for people from other script languages

  
print "Mary had a little lamb."                 # 1. Normal print doesn't have a ; 
print "Its fleece was white as %s." % 'snow'    # 2. printf corresponding 
print "And everywhere that Mary went."
print "." * 10 # print 10 .                     # 3. print multiplication 

end1 = "C"                              
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print end1 + end2 + end3 + end4 + end5 + end6,    # 4. print on multiple line using ','
print end7 + end8 + end9 + end10 + end11 + end12  # 5. print summation

days = "Mon Tue Wed Thu Fri Sat Sun"              # 6. print contatination using ","
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

                                                    # 7 print mulitiple lines
print """                                       
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""                                                 #8. print multiple lines 

print "Double quote " + 'single quote'              #9. Single quote is preferred over double quote. 
print 'This is a double quote " by single quote'    #10. Single quote and double quote

#  %[flags][width][.precision]type 
# flags: #: oxX,  0 : 0 padded,   - : left justed   : no sign,  +:+/- sign  "space": space
# width: 
# digit:

print "Art: %5d, Price per Unit: %8.2f " % (453, 59.058) 
print "Art: %+5d, Price per Unit: %8.2f " % (453, 59.058) 
print "Art: %-5d, Price per Unit: %8.2f " % (453, 59.058) 
print "Art: %5d, Price per Unit: %8.4f " % (453, 59.058) 
print "Art: %  5d, Price per Unit: %8.2f " % (453, 59.058) 
print "Art: %#5X, Price per Unit: %8.2f " % (453, 59.058) 
