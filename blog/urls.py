from django.urls import path
from . import views
#これはDjangoの path 関数と、blog アプリの全ての ビュー（といっても、今は一つもありません。すぐに作りますけど！）をインポートするという意味です。

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
#見てのとおり、post_list という名前の ビュー をルートURLに割り当てています。 このURLパターンは空の文字列に一致し、Django URLリゾルバーはURLのフルパスの前半にくっつくドメイン名（つまり、http://127.0.0.1:8000/ の部分）を無視します。 このパターンは誰かがあなたのWebサイトの 'http://127.0.0.1:8000/' というアドレスにアクセスしてきたら views.post_list が正しい行き先だということをDjangoに伝えます。
