from django.urls import path, include
from final_exam.web.views import index, dashboard_page, create_profile, details_profile, edit_profile, delete_profile, \
    create_event, details_event, edit_event, delete_event

urlpatterns = (
    path('', index, name='index'),
    path('dashboard', dashboard_page, name='dashboard page'),

    path('create/', create_event, name='create event'),
    path('details/<int:pk>/', details_event, name='details event'),
    path('edit/<int:pk>/', edit_event, name='edit event'),
    path('delete/<int:pk>/', delete_event, name='delete event'),

    path('profile/', include([
        path('create/', create_profile, name='create profile'),
        path('details/', details_profile, name='details profile'),
        path('edit/', edit_profile, name='edit profile'),
        path('delete/', delete_profile, name='delete profile'),
    ])),
)