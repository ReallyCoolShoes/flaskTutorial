class BooksApiResponse:
    def __init__(self, bookId, volumeInfo, saleInfo, accessInfo):
        self.bookId = bookId
        self.volumeInfo = volumeInfo
        self.saleInfo = saleInfo
        self.accessInfo = accessInfo
