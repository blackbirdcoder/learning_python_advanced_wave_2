from django.http import HttpRequest, HttpResponse
from .utils import password_check, string_generation


def index(request):
    html = "<div style='width:270px;background:blue;'>" \
           "<h1 style='font-size:40px;color:yellow;'>Welcome home</h1></div>"
    return HttpResponse(html)


def article(request, article_id, title):
    html = f"<div style='background:silver;width:800px;margin:0 auto;text-align:center;'>" \
           f"<b style='font-size:30px;'>" \
           f"<span style='color:blue;'>{article_id}</span><span style='color:maroon;'>:</span>" \
           f"<span style='color:indigo;'>{title}</span><b></div>"
    return HttpResponse(html)


def password(request, symbols):
    answer = password_check(symbols)
    color, key = "red", "failure"
    if "success" in answer.keys():
        color, key = "blue", "success"
    html = f"<div style='width:400px;border:2px solid {color}; margin:0 auto;text-align:center;'>" \
           f"<span style='font-size:40px; color:{color};'>{answer.get(key)}</span></div>"
    return HttpResponse(html)


def password_generator(request, length):
    symbols = string_generation(length)
    html = f"<div style='width:800px;font-size:30px; margin:0 auto;word-wrap:break-word;'>" \
           f"<span>Your password:</span>" \
           f"<span style='color:blue;'>{symbols}</span></div>"
    return HttpResponse(html)


