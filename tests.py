import pytest
from main import BooksCollector

class TestBooksCollector:
    @pytest.fixture(autouse=True)
    def collector(self):
        self.collector = BooksCollector()

    @pytest.mark.parametrize(
        "book_name, expected_result",
        [
            ["Преступление и наказание", True],
            ["Горе от ума", True],
            ["", False],
            ["Очень длинное название книги которрое превышает 40 символов", False]

        ]
    )
    def test_add_new_book_add_books(self, book_name, expected_result):
        self.collector.add_new_book(book_name)
        assert (len(self.collector.get_books_genre()) == 1)  == expected_result


    def test_add_new_book_add_old_book(self):
        self.collector.add_new_book("Преступление и наказание")
        self.collector.add_new_book("Преступление и наказание")
        assert len(self.collector.get_books_genre()) == 1


    def test_set_book_genre_and_get_book_genre(self):
        self.collector.add_new_book("Преступление и наказание")
        self.collector.set_book_genre("Преступление и наказание", "Фантастика")
        assert self.collector.get_book_genre("Преступление и наказание") == "Фантастика"



    def test_get_books_with_specific_genre_get_two_books(self):
        self.collector.add_new_book("Преступление и наказание")
        self.collector.add_new_book("Горе от ума")
        self.collector.set_book_genre("Преступление и наказание", "Фантастика")
        self.collector.set_book_genre("Горе от ума", "Фантастика")
        assert self.collector.get_books_with_specific_genre("Фантастика") == ["Преступление и наказание", "Горе от ума"]


    def test_get_books_genre(self):
        self.collector.add_new_book("Преступление и наказание")
        self.collector.set_book_genre("Преступление и наказание", "Фантастика")
        assert self.collector.get_books_genre() == {"Преступление и наказание": "Фантастика"}


    @pytest.mark.parametrize("name, genre, expected_result", [["Чебурашка", "Мультфильмы", True],["Остров проклятых", "Ужасы", False]])
    def test_get_books_for_children_parametrize(self, name, genre, expected_result):
        self.collector.add_new_book(name)
        self.collector.set_book_genre(name, genre)
        assert (len(self.collector.get_books_for_children()) == 1) == expected_result


    def test_add_book_in_favorites_and_get_list_of_favorites_books(self):
        self.collector.add_new_book("Преступление и наказание")
        self.collector.add_book_in_favorites("Преступление и наказание")
        assert self.collector.get_list_of_favorites_books() == ["Преступление и наказание"]


    def test_delete_book_from_favorites_delete_books(self):
        self.collector.add_new_book("Преступление и наказание")
        self.collector.add_book_in_favorites("Преступление и наказание")
        self.collector.delete_book_from_favorites("Преступление и наказание")
        assert self.collector.get_list_of_favorites_books() == []

