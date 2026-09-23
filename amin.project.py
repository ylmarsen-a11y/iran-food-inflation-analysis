
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"کتاب '{book.title}' با موفقیت اضافه شد.")

    def list_books(self):
        if not self.books:
            print("کتابخانه‌ای خالی است.")
            return
        print("\n--- لیست کتاب‌ها ---")
        for book in self.books:
            book.display_info()
        print("------------------\n")

    # متد جدید برای جستجوی کتاب
    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower(): # مقایسه بدون حساسیت به بزرگی و کوچکی حروف
                return book
        return None # اگر کتابی پیدا نشد، None برمی‌گرداند

# --- کد قبلی برای کلاس Book ---
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display_info(self):
        print(f"عنوان: {self.title}")
        print(f"نویسنده: {self.author}")
        print(f"تعداد صفحات: {self.pages}")
        print("-" * 20)

# --- کد نمونه برای استفاده ---
if __name__ == "__main__":
    # ساختن چند کتاب
    book1 = Book("ارباب حلقه‌ها", "جی. آر. آر. تالکین", 1200)
    book2 = Book("هری پاتر و سنگ جادو", "جی. کی. رولینگ", 300)
    book3 = Book("شازده کوچولو", "آنتوان دو سنت اگزوپری", 100)

    # ساختن کتابخانه
    my_library = Library()

    # اضافه کردن کتاب‌ها به کتابخانه
    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    # نمایش همه کتاب‌ها
    my_library.list_books()

    # جستجوی یک کتاب
    search_title = "هری پاتر و سنگ جادو"
    found_book = my_library.search_book(search_title)

    if found_book:
        print(f"کتاب '{search_title}' پیدا شد:")
        found_book.display_info()
    else:
        print(f"کتاب '{search_title}' در کتابخانه یافت نشد.")

    search_title_not_found = "کیمیاگر"
    found_book_not_found = my_library.search_book(search_title_not_found)
    if found_book_not_found:
        print(f"کتاب '{search_title_not_found}' پیدا شد:")
        found_book_not_found.display_info()
    else:
        print(f"کتاب '{search_title_not_found}' در کتابخانه یافت نشد.")

