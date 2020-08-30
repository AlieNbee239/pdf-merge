from PyPDF2 import PdfFileMerger
pdfs = ['pdf1.pdf', 'pdf2.pdf','pdf3.pdf'] #name of those pdfs 
#put those pdfs in right  path ....else  the code is not working
mergePdf = PdfFileMerger()

for pdf in pdfs:
    mergePdf.append(pdf) #print the hole pdf
    """mergePdf.append(pdf,pages=(0,1))
    #if you want print only 1st page
    """
    
mergePdf.write("result1stpage.pdf")
mergePdf.close()
#code by myself supratik----- alien bee 239
# follow me on instagram myself_supratik