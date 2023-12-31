from django.urls import path
from rest_framework.routers import DefaultRouter

from main.apps import MainConfig
from main.views.course import CourseViewSet
from main.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView,\
LessonDestroyAPIView

app_name = MainConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'), # Создание
    path('lessons/', LessonListAPIView.as_view(), name='lesson_list'), #
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'), # один урок
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'), # изменение
    path('lessons/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'), # удаление
] + router.urls



#print(router.urls)
