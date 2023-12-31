## Модуль 7 от SkyPro. Django REST framework

## 24.1 Вьюсеты и дженерики. Домашнее задание 
### (ветка 24.1_HW_ViewSet_Generic)

### Реализовано в проекте:

#### 1. Создан новый Django-проект, настроено виртальное окружение - venv, подключен и настроен - DRF.
        - pip install djangorestframework
        - config.settings.py: INSTALLED_APPS = ['rest_framework',]

#### 2. Создано два приложения - main, users. Созданы следующие модели:
        - Main. Model Course, поля: name, preview, description, user (ForeignKey, settings.AUTH_USER_MODEL)
                Model Lesson, поля: name, description, image, link_video, user (ForeignKey, settings.AUTH_USER_MODEL)

        - Users. Model User, поля: email (unique=True), name, phone, city, avatar.

#### 3. Созданы сериализаторы, CRUD для моделей Course (ViewSets), Lesson (Generic-классы)
        - Сериализаторы: CourseSerializer, LessonSerializer.
        - ViewSets: CourseViewSet
        - Generic: LessonCreateAPIView, LessonRetrieveAPIView, LessonListAPIView, LessonUpdateAPIView, LessonDestroyAPIView