import markdown
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

#from comments.forms import CommentForm
from .models import Post, Category, Tag
from .visit_record import record_visit


def archives(request):
    date_list = Post.objects.dates('created_time', 'month', order='DESC')
    return render(request, 'archives.html', context={'date_list': date_list})


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'post_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context.get('paginator')
        page = context.get('page_obj')
        is_paginated = context.get('is_paginated')
        pagination_data = self.pagination_data(paginator, page, is_paginated)
        context.update(pagination_data)
        record_visit()
        return context

    def pagination_data(self, paginator, page, is_paginated):
        if not is_paginated:
            return {}
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        next = 0
        page_number = page.number
        total_pages = paginator.num_pages
        page_range = paginator.page_range
        if page_number == 1:
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page_number == total_pages:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page_number - 3) if (page_number - 3) > 0 else 0:page_number - 1]
            right = page_range[page_number:page_number + 2]
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        if page_number < total_pages:
            next = page_number + 1
        else:
            next = total_pages
        data = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'next': next,
        }

        return data

class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month)

    def get_context_data(self, **kwargs):
        context = super(ArchivesView, self).get_context_data(**kwargs)
        # title = '{} å¹´ {} æœˆ'.format(self.kwargs.get('year'), self.kwargs.get('month'))
        title = '{}年{}月'.format(self.kwargs.get('year'), self.kwargs.get('month'))
        context.update({
            'title': title
        })
        return context


class CategoryView(IndexView):
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        title = '{}'.format(get_object_or_404(Category, pk=self.kwargs.get('pk')))
        context.update({
            'title': title
        })
        return context


class TagView(IndexView):
    def get_queryset(self):
        ta = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=ta)

    def get_context_data(self, **kwargs):
        context = super(TagView, self).get_context_data(**kwargs)
        title = '{}'.format(get_object_or_404(Tag, pk=self.kwargs.get('pk')))
        context.update({
            'title': title
        })
        return context


class PostView(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        # markdown
        post = super(PostView, self).get_object(queryset=None)
        post.content = markdown.markdown(post.content,
                                        extensions=[
                                            'markdown.extensions.extra',
                                            'markdown.extensions.codehilite',
                                            'markdown.extensions.toc',
                                        ])
        return post

    # def get_context_data(self, **kwargs):
    #     # form and comment_list
    #     context = super(PostView, self).get_context_data(**kwargs)
    #     form = CommentForm()
    #     comment_list = self.object.comment_set.all()
    #     context.update({
    #         'form': form,
    #         'comment_list': comment_list,
    #     })
    #     return context


