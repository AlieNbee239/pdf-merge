from PyPDF2 import PdfFileMerger
print("number of PDF ... you want to merge")
number=input()
pdfs=[]
i=1
while True:  
    
  x =input('type your name with extension ' ) #name of those pdfs 
  #put those pdfs in right  path ....else  the code is not working
  if(".pdf"in x):
    pdfs.append(x)
    mergePdf = PdfFileMerger()
    i = i + 1  
    if(i > int(number)):  
        break  

  else:
    print("extension error..... xxxxxx@#$ \n------- TRY AGAIN -------- ")
  
    i=i 
    if(i <int( number)):
        continue
print (pdfs )

for pdf in pdfs:
    mergePdf.append(pdf) ## adding the element 
    """mergePdf.append(pdf,pages=(0,1))
    #if you want print only 1st page
    """
    
mergePdf.write("alienbee239pdfmerge.pdf")
mergePdf.close()
#code by myself supratik----- alien bee 239
# follow me on instagram myself_supratik

