import PyPDF2


def pdf_info_extractor(file_name, file_page):
    f = open(file_name, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(f)
    # pdf_reader.numPages
    page_one = pdf_reader.getPage(file_page)
    page_one_text = page_one.extractText()
    f.close()
    return page_one_text

print(pdf_info_extractor('Working_Business_Proposal.pdf', 0))


f = open('Working_Business_Proposal.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
print(type(first_page))
pdf_writer.addPage(first_page)
pdf_output = open('A New PDF File.pdf', 'wb')
pdf_writer.write(pdf_output)
f.close()
pdf_output.close()