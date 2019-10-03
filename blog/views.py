from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
#models.py のモデルを、インクルード


#def post_list(request):
#    return render(request, 'blog/post_list.html', {})
#みてのとおり、post_list という関数（def から始まる部分のことです）を作りました。これは request を引数に取り、blog/post_list.htmlテンプレートを表示する （組み立てる）render 関数を return しています。

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
#render関数では、既にパラメータとして requestとテンプレートファイル 'blog/post_list.html'が渡されています。
#リクエストというのは、インターネットを介してユーザから受け取った全ての情報が詰まったものです。最後のパラメータに注目してください。 {}こんな風に書かれていますね。この中に指定した情報を、テンプレートが表示してくれます。{} の中に引数を記述する時は、名前と値をセットにしなくてはなりません。 表示させたいのはクエリセットのデータなので、 posts を指定しましょう。 :) {'posts': posts}という具合に、記述します。 注意して欲しいのは、シングルクォートです。 :（コロン） で区切られた、前の方の posts は、 シングルクォート で囲まれて、 'posts' になっていますよね。こちらが名前で、後ろの方の posts は値、クエリセットのことです。
#クエリセットが何かと言うと、モデルのオブジェクトのリストのことです。クエリセットを使って、データベースからデータを読み込んだり、抽出したり、並べ替えたりできます。
