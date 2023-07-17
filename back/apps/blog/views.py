
from django.core.validators import ip_address_validator_map
from django.utils.dateparse import postgres_interval_re
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.views import APIView

from apps.blog.models import Post, ViewCount
from apps.category import views
from apps.category.models import Category
from apps.blog.pagination import SmallSetPagination
from apps.blog.serilaizers import PostSerilaizer,PostListSerializer
from .pagination import SmallSetPagination, MediumSetPagination, LargetSetPagintation

from django.db.models.query_utils import Q

class BlogListView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request,  format=None):
        if Post.postobjects.all().exists():
            posts = Post.postobjects.all()
            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(posts, request)
            serializer = PostSerilaizer(results, many=True)

            return paginator.get_paginated_response({'posts': serializer.data})

        else:
            return Response({'error':'No post no found'}, status=status.HTTP_404_NOT_FOUND)

class ListPostsByCategory(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        if Post.postobjects.all().exists():
            slug = request.query_params.get('slug')
            category = Category.objects.get(slug=slug)
            posts = Post.postobjects.order_by('-published').all()

            if category.parent:
                posts = posts.filter(category=category)

            else:
                if not Category.objects.filter(parent=category).exists():
                    posts=posts.filter(category=category)

                else:
                    sub_category = Category.objects.filter(parent=category)
                    filter_category = [category]
                    for cat in sub_category:
                        filter_category.append(cat)
                    filter_category = tuple(filter_category)
                    posts = posts.filter(category__in=filter_category)

                paginator = SmallSetPagination()
                results = paginator.paginate_queryset(posts,request)
                serializer = PostSerilaizer(results,many=True)

                return paginator.get_paginated_response({'posts':serializer.data})
        else:
                return Response({'error': 'No posts found'}, status=status.HTTP_404_NOT_FOUND)


class BlogDetailView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self,request,slug,format=None):
        if Post.postobjects.filter(slug=slug).exists():

            post = Post.postobjects.get(slug=slug)
            serelaizer = PostSerilaizer(post)
            address = request.META.get('HTTP_X_FORWARDED_FOR')
            if address:
                ip = address.slipt(',')[-1].strip()
            else:
                ip = request.META.get('REMOTE_ADDR')

            if not ViewCount.objects.filter(post=post, ip_address=ip):
                view = ViewCount(post=post,ip_address=ip)
                view.save()
                post.views +=1
                post.save
            return Response({'post':serelaizer.data},status = status.HTTP_200_OK)
        else:
            return Response({'error':'Post doenst exist'}, status = status.HTTP_404_NOT_FOUND)

class BlogSearch(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        search_term = request.query_params.get("s")
        matches = Post.postobjects.filter(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term) |
            Q(content__icontains=search_term) |
            Q(category__name__icontains=search_term)

        )
        print(matches)
        paginator= SmallSetPagination()
        results = paginator.paginate_queryset(matches,request)

        content  = PostSerilaizer()
        serializer = PostListSerializer(results,many=True)

        return paginator.get_paginated_response({'filtered_posts':serializer.data})


class PostContent(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, format=None):
        if Post.postobjects.all().exists():
            posts = Post.postobjects.all()
            serializer = PostSerilaizer(posts,many=True)

            return Response({"posts": serializer.data})
        else:
            return Response({"error": "Post No found"})
