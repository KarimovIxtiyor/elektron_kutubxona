# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from django.urls import reverse
# from .models import Book
#
#
# # Create your tests here.
# class BookTests(TestCase):
#
#     def setUp(self):
#         self.post = Book.objects.create(
#             title='Kitob nomi',
#             author='Familya',
#             genre='Janr',
#             slug='Kitob-nomi',
#             body='Kitob matni',
#         )
#
#     def test_string_representation(self):
#         title = Book(title='Kitob nomi')
#         self.assertEqual(str(title), Book.title)
#
#     def test_book_content(self):
#         self.assertEqual(f'{self.post.title}', 'Kitob nomi')
#         self.assertEqual(f'{self.post.author}', 'Familya')
#         self.assertEqual(f'{self.post.body}', 'Kitob matni')
#
#     def test_book_list_view(self):
#         response = self.client.get(reverse('book'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, 'Kitob matni')
#         self.assertTemplateUsed(response, 'book.html')
#
#     def test_book_detail_view(self):
#         response = self.client.get('/book/1/')
#         no_response = self.client.get('/book/100000/')
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, 'Yangi Kitob')
#         self.assertTemplateUsed(response, 'book_detail.html')
