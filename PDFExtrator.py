import asyncio
from urllib.request import urlopen
from pdfminer.converter import TextConverter
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import resolve1
from io import BytesIO, StringIO

class PDF():
    '''
    filename : the path and filename of pdf
    '''
    def __init__(self, filename):
        self.filename = filename

    def getText(self):
        output = StringIO()
        with open(self.filename, 'rb') as fp:
            praser = PDFParser(fp)
            doc = PDFDocument(praser)
            if not doc.is_extractable:
                raise PDFTextExtractionNotAllowed

            pdfrm = PDFResourceManager()
            laparams = LAParams()
            device = PDFPageAggregator(pdfrm, laparams=laparams)
            interpreter = PDFPageInterpreter(pdfrm, device)
            for page in PDFPage.create_pages(doc):
                interpreter.process_page(page)
                layout = device.get_result()
                for x in layout:
                    if hasattr(x, "get_text"):
                        content = x.get_text()
                        output.write(content)
        content = output.getvalue()
        output.close()
        return(content)

    def getImgCount(self):
        import fitz
        import re
        checkIM = r"/Subtype(?= */Image)"
        doc = fitz.open(self.filename)
        imgcount = 0
        lenPDF = doc._getXrefLength()
        for i in range(1, lenPDF):
            text = doc._getXrefString(i)
            if re.search(checkIM, text):
                imgcount += 1
        return(imgcount)
    
    def getImg(self):
        pass

    async def downd_pdf(self, fp):
        data = fp.read()
        with open(self.filename + ".pdf", "wb") as code:
            code.write(data)
        code.close()

    def getPages(self):
        with open(self.filename, 'rb') as fp:
            parser = PDFParser(fp)
            doc = PDFDocument(parser)
            pages = resolve1(doc.catalog["Pages"])["Count"]
        return(pages)

    def textFromURL(self, url):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        f = urlopen(url).read()
        fp = BytesIO(f)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos = set()
        page_i = 0
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
            page_i+=1
            interpreter.process_page(page)
        asyncio.run(downd_pdf(fp, filename))
        fp.close()
        device.close()
        tx = retstr.getvalue()
        retstr.close()
        return(tx, page_i)