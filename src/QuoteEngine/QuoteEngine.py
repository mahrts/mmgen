"""This module encapsulate parsing strategies from different file extensions."""

import os
from abc import ABC
from abc import abstractmethod
import csv
import subprocess
import docx

class QuoteModel():
    """Quotes which will be later added to memes."""

    def __init__(self, author: str, body: str) -> None:
        """Build a quote

        Arguments:
            author {str} -- quote's author.
            body {str} -- the actual quote message.
        """
        self.author = author
        self.body = body

    def __repr__(self):
        """Pretty print oneself."""
        return f'{self.body} - {self.author}'


class IngestorInterface(ABC):
    """
    This baseclass encapsulate different strategies to parse quotes from files
    of various extensions such as pdf, docx, txt, ...
    """

    extensions = []

    @classmethod
    def can_ingest(cls, path: str):
        """This method checks if a file extension is supported by the given strategy.
        
        Args:
        path: path to the file

        Returns:
            If the file can be ingested by the chosen method.
        """
        return path.split(".")[-1] in cls.extensions

    @classmethod
    @abstractmethod
    def parse(cls, path):
        """This method parse the content of the path file."""


class PdfInterface(IngestorInterface):
    """This interface is designed to parse contents from .pdf files."""

    extensions = ["pdf"]

    @classmethod
    def parse(cls, path: str):
        """This method returns list of quotes from .pdf file.
        
        Args:
            path: Path to a pdf file.

        Returns:
            List of quotes in the input.

        Raises:
            ValueError: If the path does not contain .pdf file.
        """
        if not cls.can_ingest(path):
            raise Exception("PdfInterface called on non-pdf filepath.")

        temp = "tempfile.txt"
        subprocess.call(["pdftotext", path, temp])

        with open(temp, "r", encoding = "utf-8") as f:
            file = "".join(f.readlines()).split("\n")
            quotes_list = list(filter(lambda x: len(x) > 3, file))

        os.remove("tempfile.txt")
        models = []
        for _, quote in enumerate(quotes_list):
            if "-" in quote:
                body, author = tuple(quote.split("-"))
                models.append(QuoteModel(author.strip(), body.strip()))
        return models


class TxtInterface(IngestorInterface):
    """This interface is designed to parse contentx from .txt files."""

    extensions = ['txt']

    @classmethod
    def parse(cls, path: str):
        """This method return list of quotes from .txt file.
        
        Args:
        path: Path to a .txt file

        Returns:
            List of quotes in the file.

        Raises:
            ValueError: If the path does not contain txt file extension.
        """
        if not cls.can_ingest:
            raise Exception("TxtInterface called on non .txt filepath.")
        with open(path, 'r', encoding = "utf-8") as f:
            file = f.read().split("\n")

        quotes_list = list(filter(lambda x: len(x) != 0, file))
        models = []
        for _, quote in enumerate(quotes_list):
            if "-" in quote:
                body, author = tuple(quote.split("-"))
                models.append(QuoteModel(author.strip(), body.strip()))
        return models


class CsvInterface(IngestorInterface):
    """This interface is designed to parse quotes from .csv files."""

    extensions = ["csv"]

    @classmethod
    def parse(cls, path: str):
        """This method returns list of quotes from csv file.
        
        Args:
        path: Path to a csv file.

        Returns:
            List of quotes in the file.

        Raises:
            ValueError: If the path does not lead to a .csv file.
        """
        if not cls.can_ingest:
            raise Exception("CsvInterface called on non .csv file.")

        quote_list = []
        with open(path, 'r', encoding = "utf-8") as f:
            file = csv.reader(f)
            next(file)
            for row in file:
                if len(row) > 0:
                    quote_list.append(row)

        quotes_list = list(map(lambda x: x[0] + " - " + x[1], quote_list))
        models = []
        for _, quote in enumerate(quotes_list):
            if "-" in quote:
                body = quote.split("-")[0]
                author = quote.split("-")[1]
                models.append(QuoteModel(author.strip(), body.strip()))
        return models


class DocxIntefrace(IngestorInterface):
    """This interface is designed to parse quotes from Docx files."""

    extensions = ["docx"]

    @classmethod
    def parse(cls, path):
        """This method returns list of quotes from a docx file.
        
        Args:
        path: Path to a .docx file

        Returns:
            List of quotes in the file.

        Raises:
            ValueError: If the path does not lead to a docx file.
        """
        if not cls.can_ingest:
            raise Exception("Docx interface called on non .docx file.")

        quotes_list = []
        doc = docx.Document(path)
        for l in doc.paragraphs:
            line = l.text
            if "-" in line:
                body = line.split("-")[0].strip()
                author = line.split("-")[1].strip()
                quotes_list.append(QuoteModel(author, body))
        return quotes_list


class Ingestor(IngestorInterface):
    """Tiis class encapsulate parsing method for all file extensios: txt, csv, docx and pdf."""

    interfaces = [PdfInterface, TxtInterface, CsvInterface, DocxIntefrace]

    @classmethod
    def parse(cls, path: str):
        quote_list = []
        for parser in cls.interfaces:
            if parser.can_ingest(path):
                quote_list = parser.parse(path)
        return quote_list


if __name__ == "__main__":
    #pdf
    PDF_PATH = "./src/_data/DogQuotes/DogQuotesPDF.pdf"
    pdf_quote_list = PdfInterface.parse(PDF_PATH)
    print(pdf_quote_list, "\n ++++++++++++++++\n")

    #text
    TXT_PATH = "./src/_data/DogQuotes/DogQuotesTXT.txt"
    txt_quote_list = TxtInterface.parse(TXT_PATH)
    print(txt_quote_list, "\n+++++++++++++++++++\n")

    #csv
    CSV_PATH = "./src/_data/DogQuotes/DogQuotesCSV.csv"
    csv_quote_list = CsvInterface.parse(CSV_PATH)
    print(csv_quote_list, "\n+++++++++++++++")

    #docx
    DOCX_PATH = "./src/_data/DogQuotes/DogQuotesDOCX.docx"
    docx_quote_list = DocxIntefrace.parse(DOCX_PATH)
    print(docx_quote_list)
