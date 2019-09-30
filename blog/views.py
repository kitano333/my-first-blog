from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})
#みてのとおり、post_list という関数（def から始まる部分のことです）を作りました。これは request を引数に取り、blog/post_list.htmlテンプレートを表示する （組み立てる）render 関数を return しています。

# Create your views here.
