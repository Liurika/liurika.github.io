
################################
#### Laura Lorenzo 10345882 ####      # For best results, run program on CMD with window fitted to screen #
################################

# Accessing file
file = open('changes_python.txt', 'r')

# Getting, cleaning and counting lines
lines = []
for line in file:
    line = line.strip()
    lines.append(line)

sep = 72*'-' # This will allow the search for each new entry

# Initializing list, dicts and variable

entries = []
index = 0
authors = {}
fulldates = []
changes = {}
adds = []
rems = []
enbs = []
mods = []
fixes = []
hours = {}

# While loop to parse file, register every entry into the dicts we just created, and classify interesting
# info from every one

while True:
    try:
        details = lines[index + 1].split('|')
        for info in details:                  # To find the authors
            authors[details[1].strip()] = authors.get(details[1].strip(), 0) + 1
            fulldates.append(details[2].strip())
            comment_line_count = int(details[3].strip().split(' ')[0])
            change = lines[index-comment_line_count:index]
            change = str(change).lower().strip('[').strip("'").strip(',').strip("'")
            word = change.split()
            if word[0] == 'added':
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
        
# To find dates and times

for date in fulldates:   
    parts = date.split()
    time = parts[1]
    hour = time[:2]
    hours[hour] = hours.get(hour, 0) + 1
    
# Display number of entries in total
print ' '
print sep
print ' '
print "   The file 'changes_python.txt' contains",len(lines),'lines and',len(entries),'entries.'
print ' '
print sep
print ' '
print 'The following is a list of facts about the information contained in this file: '
print ' '

# Sort and display author with most entries

order = []
for key,value in authors.items():
    order.append((value,key))
order.sort(reverse=True)
for value, key in order[0:1]:
    print '1. The person who contributed the most to the app is <<',key,'>> with',value,'entries between July and November 2015. That is,',value/100,'contributions per day! What a hard-working fella.'
print ' '

# Sort and display most popular hours for contributing

sorter = []
for key,value in hours.items():
    sorter.append((value,key))
sorter.sort(reverse=True)
for value,key in sorter[0:1]:
    print "2. The most popular hour for this App's contributions is",key,'with',value,"entries. Interestingly enough, it is the last hour of work for people"
    print "   with ordinary working hours. So you can easily picture them submitting whatever work they did that morning and going out for lunch straight away."

# Display comment count and sorting
print ' '
print "3. From a total of",len(changes),"changes, the most popular type of change was 'Adding' with",len(adds),"comments starting with the word 'added'."
print "   The second most popular was 'removed' with",len(rems),"ocurrences. So, yes, a programmer's work is basically adding or removing"
print "   characteristics to and from a program. For contrast, we can see that there were only",len(mods),"modifications,",len(fixes),"fixes, and",len(enbs),"comments starting with 'enabled'."