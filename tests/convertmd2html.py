import marko

file = r'source_documents\Read Aloud.md'
with open(file, 'r') as f:
    test = marko.convert(f.read())
with open('text.html','w') as f:
    f.write(test)