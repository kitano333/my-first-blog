
# ここでやっていることはデータベースの設定。

from django.db import models 
# これは「django.db」の「models」をインポートするという意味。
from django.utils import timezone # 
# ただ「django.utils」とあるけど、settings.pyのTIME_ZONEからとってきているみたい

class Post(models.Model):  # PostというTableを宣言する、頭文字が大文字が流儀
#classはオブジェクトを定義してますよ、ということを示すキーワード。Ｐｏｓｔというオブジェクト。
#models.Model はポストがDjango Modelだという意味で、
#Djangoが、これはデータベースに保存すべきものだと分かるようにしています。
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

#models.CharField – 文字数が制限されたテキストを定義するフィールド
#models.TextField – これは制限無しの長いテキスト用です。
#models.DateTimeField – 日付と時間のフィールド
#models.ForeignKey – これは他のモデルへのリンク
#モデルの定義ttps://docs.djangoproject.com/ja/2.0/ref/models/fields/#field-types

    def publish(self):
        self.published_date = timezone.now()
        self.save()

#publish はメソッド(関数)の名前で、 変えることもできます。


    def __str__(self):
        return self.title
#return self.titleのselfがないとエラーになる。
