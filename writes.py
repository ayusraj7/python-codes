lines_data=['Shivam\n','Gaurav\n','Kite\n']


with open('write_file.txt','w') as f:
    f.write('Anuj')
    f.writelines(lines_data)


with open('write_file.txt','a') as f:
    f.write('Anuj')
    f.writelines(lines_data)

