text = 'sample text to save\nNew line!'

saveFile = open('exampleFile.txt','w')
saveFile.write(text)
saveFile.close()
