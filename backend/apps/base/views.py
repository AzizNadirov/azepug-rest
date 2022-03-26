from django.db.models.expressions import F
from django.contrib.contenttypes.models import ContentType

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from apps.blog.models import Blog
from apps.event.models import Event
from apps.news.models import News
from apps.vacancy.models import Vacancy
from apps.forum.models import Question, Answer



def increment_view(post, request):
    """ view incerementer. An user can increment just once"""
    if request.user not in post.viewers.all():
        post.views = F('views') + 1
        post.save()
        post.refresh_from_db()

        post.viewers.add(request.user)
        


def get_model_by_appname(app_name:str):
    app_list = ['blog', 'event', 'news', 'vacancy', 'question', 'answer']
    if app_name not in app_list:
        return None
    if app_name == 'blog': return Blog
    elif app_name == 'event': return Event
    elif app_name == 'news': return News
    elif app_name == 'vacancy': return Vacancy
    elif app_name == 'question': return Question
    elif app_name == 'answer': return Answer


class LikeView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def increment_like(self, app_name, pk, decrement = False):
        """ like incerementer """
        post = get_model_by_appname(app_name).objects.get(pk = pk)
        if not decrement:
            print('\n-----Like Incrementer--------------\n')
            post.like_count = F('like_count') + 1
        else:
            print('\n-----Like Decrementer--------------\n')
            post.like_count = F('like_count') - 1
        post.save()
        post.refresh_from_db()
    
    def post(self, request, pk):
        app_name  = request.POST.get('app_name')
        value = request.POST.get('value')
        if app_name not in ['blog', 'event', 'news', 'vacancy']:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        if value == "+":
            code = f"request.user.liked_{app_name}.add(pk)"
            eval(code)
            self.increment_like(app_name, pk)
        elif value == '-':
            code = f"request.user.liked_{app_name}.remove(pk)"
            eval(code)
            self.increment_like(app_name, pk, decrement = True)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={f'message': f"incorrecy value: '{value}' "})
        return Response(status=status.HTTP_200_OK)

class SupportView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def increment_support(self, app_name, pk, decrement = False):
        """ support incerements / decrements support count """
        post = get_model_by_appname(app_name).objects.get(pk = pk)
        if not decrement:
            post.supports_count = F('supports_count') + 1
        else:
            post.supports_count = F('supports_count') - 1
        post.save()
        post.refresh_from_db()


        def post(self, request, pk):
            app_name  = request.POST.get('app_name')
            value = request.POST.get('value')
            if app_name not in ['answer', 'question']:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if value == "+":
                code = f"request.user.supported_{app_name}.add(pk)"
                eval(code)
                self.increment_like(app_name, pk)
            elif value == '-':
                code = f"request.user.supported_{app_name}.remove(pk)"
                eval(code)
                self.increment_support(app_name, pk, decrement = True)
            return Response(status=status.HTTP_200_OK)
        

class SaveView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request, pk):
        app_name  = request.POST.get('app_name')
        value = request.POST.get('value')
        if app_name not in ['blog', 'event', 'news', 'vacancy', 'question']:
            return Response(status = status.HTTP_400_BAD_REQUEST)
        if value == "+":
            code = f" request.user.treasure.{app_name}.add(pk)"
            eval(code)
        elif value == '-':
            code = f" request.user.treasure.{app_name}.remove(pk)"
            eval(code)
        return Response(status = status.HTTP_200_OK)



# class UpiView(View):
#     def get(self, request, upi_code):
#         post = search_by_upi(upi_code)
#         if post:
#             return redirect(post)
#         else:
#             return render(request, 'not_found.html')




