from django.urls import path
from . import views

urlpatterns = [
    # path('welcome/', views.welcome),
    # path('find_book/<int:id>', views.find_by_id),
    # path('render/', views.my_render),
    # path('books/', views.book_list),
    # path('books/<int:pk>', views.book_detail),
    # path('authors/', views.author_list),
    # path('authors/<int:pk>', views.author_detail),

    #         this is class view
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>', views.BookDetail.as_view()),
    path('authors/', views.AuthorList.as_view()),
    path('authors/<int:pk>', views.AuthorDetail.as_view()),
]
