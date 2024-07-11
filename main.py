from PyPDF2 import PdfFileReader, PdfFileWriter, PdfReader, PdfWriter

#open pdf file
pdf_file = PdfReader('sample.pdf')
add_file=PdfWriter()
password = "Hello@123"
print(pdf_file)
print(pdf_file.pages)
print(type(pdf_file.pages[0]))
page_count  = len(pdf_file.pages)
for page in range(page_count):
    page_details= pdf_file.pages[page]
    add_file.add_page(page_details)
    print(page_details)
add_file.encrypt(password)
with open("encyptedfile.pdf", "wb") as filename:
    add_file.write(filename)