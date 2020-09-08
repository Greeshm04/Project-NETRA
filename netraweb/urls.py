from django.urls import path
from . import views
from netra import settings
from django.conf.urls.static import static
urlpatterns = [
    path("index",views.index,name="index"),
    path('change_det',views.change_det,name='change_det'),
    path('time_det',views.time_det,name='time_det'),
    path('change_detection',views.change_detection,name='change_detection'),
    path('change_detection2',views.change_detection2,name='change_detection2'),
    path('change_detection_result',views.change_detection_result,name='change_detection_result'),
    path('feature_extraction_result',views.feature_extraction_result,name='feature_extraction_result'),
    path('feature_extraction_result2',views.feature_extraction_result2,name='feature_extraction_result2'),
    path('feature_extraction',views.feature_extraction,name='feature_extraction'),
    path('feature_extraction2',views.feature_extraction2,name='feature_extraction2'),
    path('fea_ext',views.fea_ext,name='fea_ext'),
    path('surveillance',views.surveillance,name='surveillance'),
    path('alerts',views.alerts,name='alerts'),
    path('',views.new_login,name='new_login'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)