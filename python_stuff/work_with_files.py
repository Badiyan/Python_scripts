# Create file and write
file = open('test.txt','w') # w - write, a - append, x - create (error if exist)
file.write('Some text\n') # add new text
file.flush() # from buffer to file
file.close() # close file (+flush auto)


# read file

file = open('test.txt','r') # r - readonly
print('\n','_'*20,'\nFirst file\n', file.read(),'\n','_'*20)

# append text

file = open('test.txt','a') # w - write, a - append, x - create (error if exist)
file.write('One more text')
file.close() # close file (+flush auto)

# read file

file = open('test.txt','r') # r - readonly
print('\n','_'*20,'\nSecond file\n', file.read(),'\n','_'*20)


# utf-8

file = open('test.txt','a', encoding='utf-8')
file.write('\nТестовая надпись')
file.close() # close file

# read file

file = open('test.txt','r') # r - readonly
