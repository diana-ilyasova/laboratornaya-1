# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
pages = 100
lines = 50
symbols = 25
size_of_symbol = 4

disk_size_byte = disk_size * 1024 * 1024
book_size = pages * lines * symbols * size_of_symbol
numbers_of_books = disk_size_byte // book_size

print("Количество книг, помещающихся на дискету:", int(numbers_of_books))
