import pytest
from books_collector import BooksCollector

class TestBooksCollector:

    # Тесты для add_new_book
    def test_add_new_book_book_added(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()

    @pytest.mark.parametrize('book_name', ['', 'a' * 41])
    def test_add_new_book_invalid_name_not_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_add_new_book_duplicate_not_added(self, collector):
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

    # Тесты для set_book_genre
    def test_set_book_genre_valid_genre_set(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_set_book_genre_book_not_exists_not_set(self, collector):
        collector.set_book_genre('Несуществующая книга', 'Фантастика')
        assert 'Несуществующая книга' not in collector.get_books_genre()

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Несуществующий жанр')
        assert collector.get_book_genre('Книга') == ''

    # Тесты для get_book_genre
    def test_get_book_genre_returns_genre(self, collector):
        collector.add_new_book('Метро 2033')
        collector.set_book_genre('Метро 2033', 'Фантастика')
        assert collector.get_book_genre('Метро 2033') == 'Фантастика'

    def test_get_book_genre_book_not_exists_returns_none(self, collector):
        assert collector.get_book_genre('Неизвестная книга') is None

    # Тесты для get_books_with_specific_genre
    def test_get_books_with_specific_genre_returns_correct_books(self, collector):
        books = ['Книга 1', 'Книга 2', 'Книга 3']
        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, 'Фантастика')

        collector.add_new_book('Другая книга')
        collector.set_book_genre('Другая книга', 'Комедии')

        result = collector.get_books_with_specific_genre('Фантастика')
        assert set(result) == set(books)

    def test_get_books_with_specific_genre_invalid_genre_returns_empty(self, collector):
        result = collector.get_books_with_specific_genre('Несуществующий жанр')
        assert result == []

    # Тесты для get_books_genre
    def test_get_books_genre_returns_all_books(self, collector):
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        books = collector.get_books_genre()
        assert len(books) == 2
        assert 'Книга 1' in books
        assert 'Книга 2' in books

    # Тесты для get_books_for_children
    def test_get_books_for_children_excludes_age_rated_genres(self, collector):
        # Добавляем книги с разными жанрами
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Мультфильмы')

        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', 'Ужасы')

        collector.add_new_book('Детектив')
        collector.set_book_genre('Детектив', 'Детективы')

        collector.add_new_book('Фантастика')
        collector.set_book_genre('Фантастика', 'Фантастика')

        result = collector.get_books_for_children()
        assert 'Детская книга' in result
        assert 'Фантастика' in result
        assert 'Страшная книга' not in result
        assert 'Детектив' not in result

    def test_get_books_for_children_book_without_genre_not_included(self, collector):
        collector.add_new_book('Книга без жанра')
        result = collector.get_books_for_children()
        assert 'Книга без жанра' not in result

    # Тесты для add_book_in_favorites
    def test_add_book_in_favorites_book_added(self, collector):
        collector.add_new_book('Любимая книга')
        collector.add_book_in_favorites('Любимая книга')
        assert 'Любимая книга' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_not_exists_not_added(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert 'Несуществующая книга' not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate_not_added(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.add_book_in_favorites('Книга')
        assert collector.get_list_of_favorites_books().count('Книга') == 1

    # Тесты для delete_book_from_favorites
    def test_delete_book_from_favorites_book_removed(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_not_in_favorites_no_error(self, collector):
        collector.add_new_book('Книга')
        # Не должно вызывать ошибку
        collector.delete_book_from_favorites('Книга')
        assert True

    # Тесты для get_list_of_favorites_books
    def test_get_list_of_favorites_books_returns_all_favorites(self, collector):
        books = ['Книга 1', 'Книга 2', 'Книга 3']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        favorites = collector.get_list_of_favorites_books()
        assert set(favorites) == set(books)

    @pytest.fixture
    def collector(self):
        return BooksCollector()