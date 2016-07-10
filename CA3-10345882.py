
########################################################
################ Laura Lorenzo 10345882 ################      
########################################################

'''This program will read and parse the file 'changes_python.txt', identify
 different commits, their author, date and changes made in each entry and 
 display the found information as a list of facts.'''

# Creating functions

def displaySep():
    print ' '
    print sep
    print ' '
    
def emptyLine():
    print ' '
    
def firstDisplay():
    print "1. The person who contributed the most to the App is",key,"with", \
    value,"entries submitted between July and November 2015. That means",value/20, \
    "contributions per week! What a hard-working guy!"

def secondDisplay():
    print "2. The most popular hour for this App's contributions is " + key + \
    ":00 hours, with a total of",value,"entries submitted at this time.", \
    "Interestingly enough, it is the last hour of work for people with", \
    "ordinary working hours. So you can easily picture them submitting", \
    "whatever work they did that morning and going out for lunch straight", \
    "away. Or, at least, that would be the case in Spain!"

def thirdDisplay():
    print "3. Out of a total",len(changes),"changes, the most popular type of change was", \
    "'Adding' with",len(adds),"comments starting with the word 'added'. The second most", \
    "popular was 'removed' with",len(rems),"ocurrences. So, yes, a programmer's work is ", \
    "basically adding or removing characteristics to and from a program. For contrast,", \
    "we can see that there were only",len(mods),"modifications,",len(fixes),"fixes, and", \
    str(len(enbs)),"comments starting with the word 'enabled'."

    
# Accessing file
file = open('changes_python.txt')

# Getting, cleaning and counting lines
lines = []
for line in file:
    line = line.strip()
    lines.append(line)
    
# This will allow the search for each new entry
sep = 72*'-' 

# Initializing list, dicts and variable
entries = []
index = 0
authors = {}
dates = []
changes = {}
adds = []
rems = []
enbs = []
mods = []
fixes = []
hours = {}

# While loop to parse file, register every entry into the
# dicts we just created, and classify interesting info
# from every one
while True:
    try:
        details = lines[index + 1].split('|')
        for info in details:         # To find authors, dates and change comments
            authors[details[1].strip()] = authors.get(details[1].strip(), 0) + 1
            dates.append(details[2].strip())
            comment_line_count = int(details[3].strip().split(' ')[0])
            change = lines[index-comment_line_count:index]
            change = str(change).lower().strip('[').strip("'").strip(',').strip("'")
            word = change.split()
            if word[0] == 'added':    # Classifying commentaries by initial word
                adds.append(change)
            elif word[0] == 'removed':
                rems.append(change)
            elif word[0] == 'enabled':
                enbs.append(change)
            elif word[0] == 'modified':
                mods.append(change)
            elif word[0] == 'fixed':
                fixes.append(change)                
            changes[change] = changes.get(change, 0) + 1
        index = lines.index(sep, index + 1)
        entries.append(details[0])
    except IndexError:
        break
        
# Narrowing dates down to hours
for date in dates:   
    parts = date.split()
    time = parts[1]
    hour = time[:2]
    hours[hour] = hours.get(hour, 0) + 1
    
# Display number of entries in total
displaySep()
print "   The file 'changes_python.txt' contains {} lines and {} entries.".format(str(len(lines)),str(len(entries)))
displaySep()
print 'The following is a list of facts about the information contained in this file: '
emptyLine()

# Sort and display author with most entries
order = []
print "0. The contributors to this App are: "
for key,value in authors.items():
    order.append((value,key))
    print "-->",key
emptyLine()
order.sort(reverse=True)
for value, key in order[0:1]:
    firstDisplay()
emptyLine()

# Sort and display the most popular hour for contributions
sorter = []
for key,value in hours.items():
    sorter.append((value,key))
sorter.sort(reverse=True)
for value,key in sorter[0:1]:
    secondDisplay()

# Display comment count and sorting
emptyLine()
thirdDisplay()
