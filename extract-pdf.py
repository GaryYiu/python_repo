import camelot
tables = camelot.read_pdf('foo.pdf',page='1')
print(tables)