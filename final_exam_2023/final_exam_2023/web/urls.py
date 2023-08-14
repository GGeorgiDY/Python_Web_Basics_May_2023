from django.urls import path, include

from final_exam_2023.web.views import index, details_fruit, edit_fruit, dashboard_page, create_fruit, delete_fruit, \
    create_profile, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', include([
        path('', index, name='index'),
        path('dashboard/', dashboard_page, name='dashboard page'),
        path('create/', create_fruit, name='create fruit'),
        path('<int:pk>/details/', details_fruit, name='details fruit'),
        path('<int:pk>/edit/', edit_fruit, name='edit fruit'),
        path('<int:pk>/delete/', delete_fruit, name='delete fruit'),

        path('profile/create/', create_profile, name='create profile'),
        path('profile/details/', details_profile, name='details profile'),
        path('profile/edit/', edit_profile, name='edit profile'),
        path('profile/delete/', delete_profile, name='delete profile'),
    ])),
)