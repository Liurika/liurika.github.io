### Laura Lorenzo ### CA3

# Accessing file
getfile = raw_input('Please, enter file name: ')
file = open(getfile, 'r')

# Getting, cleaning and counting lines
lines = []
for line in file:
    line = line.strip()
    lines.append(line)
print 'This file contains',len(lines),'lines.'

sep = 72*'-'

# This class identifies every commit and the different relevant parts of each entry
class Entry(object):

    def __init__(self, revision = None, author = None, date = None, commentcount = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.commentcount = commentcount
        self.changes = changes
        self.comment = comment

    def getEntryComment(self):
        return 'Revision number:' + str(self.revision) + ' by ' + self.author + ' with the comment: ' + ','.join(self.comment)
        
    def getAuthors(self):
        return self.author
 
# This class gathers relevant info into lists or dicts and returns insights 
class Interesting(object):
    
    def __init__(self):
        self.authors = []
        self.dates = []
        self.entriesperAuthor = {}
        self.authorsperDate = ()
        
    def entriesByAuthor(self):
        return (len(self.entriesperAuthor[author]))
        
# Initializing list and variables
entries = []
entry = None
index = 0
authors = ()


# While loop to parse file and register every entry into the list we just created
while True:
    try:
        entry = Entry()
        inter = Interesting()
        details = lines[index + 1].split('|')
        entry.author = details[1].strip()
        if entry.author not in inter.authors:
            inter.authors.append(entry.author)
            inter.entriesperAuthor[entry.author] = []
            entry.revision = int(details[0].strip().strip('r'))
            if entry.revision not in inter.entriesperAuthor[entry.author]:
                inter.entriesperAuthor[entry.author].append(entry.revision)
        print 'done with gathering'
        entry.date = details[2].strip()
        entry.commentcount = int(details[3].strip().split(' ')[0])
        entry.changes = lines[index+2:lines.index('',index+1)]
        index = lines.index(sep, index + 1)
        entry.comment = lines[index-entry.commentcount:index]
        entries.append(entry)
    except IndexError:
        break

# Display number of entries in total
print 'And there are',len(entries),'entries.'

# Reversing order in list
entries.reverse()

# for index, entry in enumerate(entries):
    # print entry.getEntryComment()
author = entry.getAuthors()
print inter.entriesByAuthor()  ##gives none! Refer properly!!
