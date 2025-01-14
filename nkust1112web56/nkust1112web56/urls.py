from django.contrib import admin
from django.urls import path
from mysite import views   # 引入views.py中所有的函式

urlpatterns = [
    path('', views.index),      # 設定執行首頁顯示的功能由index函式負責
    path('nkustnews/', views.nkustnews),
    path('all/', views.all_data),         #顯示所有的站台資訊
    path('filter/', views.filtered_data), #只顯示超過5台可用自行車的站台資訊
    path('admin/', admin.site.urls),
]
