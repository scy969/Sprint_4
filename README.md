# Реализованные тесты

Тестовый набор включает 19 тестов, покрывающих все методы класса `BooksCollector`.

### Тесты для метода `add_new_book`

1. **`test_add_new_book_book_added`** - проверка успешного добавления книги
2. **`test_add_new_book_invalid_name_not_added`** - проверка валидации имени книги (пустая строка и строка >40 символов)
3. **`test_add_new_book_duplicate_not_added`** - проверка невозможности добавления дубликата

### Тесты для метода `set_book_genre`

4. **`test_set_book_genre_valid_genre_set`** - проверка установки валидного жанра
5. **`test_set_book_genre_book_not_exists_not_set`** - проверка установки жанра для несуществующей книги
6. **`test_set_book_genre_invalid_genre_not_set`** - проверка установки невалидного жанра

### Тесты для метода `get_book_genre`

7. **`test_get_book_genre_returns_genre`** - проверка получения жанра книги
8. **`test_get_book_genre_book_not_exists_returns_none`** - проверка получения жанра для несуществующей книги

### Тесты для метода `get_books_with_specific_genre`

9. **`test_get_books_with_specific_genre_returns_correct_books`** - проверка фильтрации книг по жанру
10. **`test_get_books_with_specific_genre_invalid_genre_returns_empty`** - проверка фильтрации по несуществующему жанру

### Тесты для метода `get_books_genre`

11. **`test_get_books_genre_returns_all_books`** - проверка получения всех книг

### Тесты для метода `get_books_for_children`

12. **`test_get_books_for_children_excludes_age_rated_genres`** - проверка исключения книг с возрастным рейтингом
13. **`test_get_books_for_children_book_without_genre_not_included`** - проверка исключения книг без жанра

### Тесты для метода `add_book_in_favorites`

14. **`test_add_book_in_favorites_book_added`** - проверка добавления книги в избранное
15. **`test_add_book_in_favorites_book_not_exists_not_added`** - проверка добавления несуществующей книги
16. **`test_add_book_in_favorites_duplicate_not_added`** - проверка невозможности добавления дубликата в избранное

### Тесты для метода `delete_book_from_favorites`

17. **`test_delete_book_from_favorites_book_removed`** - проверка удаления книги из избранного
18. **`test_delete_book_from_favorites_book_not_in_favorites_no_error`** - проверка удаления несуществующей в избранном книги

### Тесты для метода `get_list_of_favorites_books`

19. **`test_get_list_of_favorites_books_returns_all_favorites`** - проверка получения всех избранных книг

## Особенности реализации тестов

### Параметризация

В тестах используется параметризация pytest для проверки граничных случаев с помощью декоратора `@pytest.mark.parametrize` (тестирование валидации длины имени книги с различными некорректными значениями).

### Фикстуры

Фикстура `collector` создает новый экземпляр `BooksCollector` перед каждым тестом, обеспечивая изоляцию тестов и чистоту тестового окружения.

### Best Practices

- Каждый тест проверяет одну конкретную функциональность
- Тесты независимы и не зависят от порядка выполнения
- Используются понятные и описательные имена тестов
- Покрыты как позитивные, так и негативные сценарии
- Используются assert для проверки ожидаемого поведения
