"""This code tests all classes and methods from QuoteEngine."""

from QuoteEngine.QuoteEngine import PdfInterface
from QuoteEngine.QuoteEngine import TxtInterface
from QuoteEngine.QuoteEngine import CsvInterface
from QuoteEngine.QuoteEngine import DocxIntefrace
from QuoteEngine.QuoteEngine import Ingestor
from QuoteEngine.QuoteEngine import QuoteModel

def test_pdfinterface():
    """Test parsing method for pdf files."""
    pdf_path = "./src/_data/DogQuotes/DogQuotesPDF.pdf"

    quote_list = PdfInterface.parse(pdf_path)
    ingestor_list = Ingestor.parse(pdf_path)

    assert isinstance(quote_list[0], QuoteModel), "PdfInterface does not list quotes."
    assert len(quote_list) == len(ingestor_list), "Ingestor encapsulation is not correct for pdf"

def test_txtinterface():
    """Test parsing method for txt files."""
    txt_path = "./src/_data/DogQuotes/DogQuotesTXT.txt"

    quote_list = TxtInterface.parse(txt_path)
    ingestor_list = Ingestor.parse(txt_path)

    assert isinstance(quote_list[0], QuoteModel), "TxtInterface does not return a list."
    assert len(quote_list) == len(ingestor_list), "Ingestor not correct for txt file."

def test_csvinterface():
    """Test the parsing method for .csv files."""
    csv_path = "./src/_data/DogQuotes/DogQuotesCSV.csv"
    csv_quote_list = CsvInterface.parse(csv_path)
    ingestor_list = Ingestor.parse(csv_path)

    assert isinstance(csv_quote_list[0], QuoteModel), "CsvInterface does not return a list."
    assert len(ingestor_list) == len(csv_quote_list), "Ingestor not correct for csv file."

def test_docxinterface():
    """Test the parsing method for .docx file"""
    docx_path = "./src/_data/DogQuotes/DogQuotesDOCX.docx"
    docx_quote_list = DocxIntefrace.parse(docx_path)
    ingestor_list = Ingestor.parse(docx_path)

    assert isinstance(docx_quote_list[0], QuoteModel), "DocxInterface did not return a list."
    assert len(docx_quote_list) == len(ingestor_list), "Ingestor is wrong on docx files."
