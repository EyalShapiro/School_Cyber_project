import PyPDF2


def pdf_file(file_name):
    # creating a pdf file object
    pdfFileObj = open(file_name, 'rb')

    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    # printing number of pages in pdf file
    print(pdfReader.numPages)
    for i in range(pdfReader.numPages()):
        pageObj = pdfReader.getPage(i)
        # extracting text from page
        print(pageObj.extractText())

    # closing the pdf file object
    pdfFileObj.close()


def main():
    file = 'code\\fins\\test.pdf'

    pdf_file(file)


if __name__ == '__main__':
    main()
