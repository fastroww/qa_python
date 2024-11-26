# qa_python
1. test_add_new_book_add_books
Этот тест проверяет, что книга добавляется в коллекцию, если её название подходит по условиям (не пустое и не слишком длинное). Если книга не подходит, она не добавляется, и коллекция остаётся пустой.

2. test_add_new_book_add_old_book
Этот тест проверяет, что если книгу уже добавили в коллекцию, ее нельзя еще раз добавить в коллекцию. Коллекция остаётся с одной книгой.

3. test_set_book_genre_and_get_book_genre
Этот тест проверяет, что если мы задаём жанр для книги, то при запросе жанра этой книги он возвращается правильно. Например, если мы установим жанр “Фантастика” для книги, то метод получения жанра должен вернуть именно “Фантастика”.

4. test_get_books_with_specific_genre_get_two_books
Этот тест проверяет, что метод get_books_with_specific_genre правильно возвращает список книг с указанным жанром.

5. test_get_books_genre
Этот тест проверяет, что метод get_books_genre возвращает правильный словарь с книгами и их жанрами. После добавления книги и установки жанра, метод должен вернуть словарь с правильной книгой и жанром.

6. test_get_books_for_children_parametrize
Этот тест проверяет, что метод get_books_for_children возвращает правильный список книг, подходящих для детей. В зависимости от жанра книги

7. test_add_book_in_favorites_and_get_list_of_favorites_books
Этот тест проверяет, что метод add_book_in_favorites корректно добавляет книгу в список избранных, и что метод get_list_of_favorites_books возвращает правильный список избранных книг.

8. test_delete_book_from_favorites_delete_books
Этот тест проверяет, что метод delete_book_from_favorites корректно удаляет книгу из избранных, и что после удаления книга больше не находится в списке избранных книг.
