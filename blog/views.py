from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment
from .forms import CommentForm
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.utils.text import slugify
from django.db.models import Q

# Create your views here.


class PostList(generic.ListView):
    """
    Returns all published posts in :model:`blog.Post`
    and displays them in a page of six posts. 
    **Context**

    ``queryset``
        All published instances of :model:`blog.Post`
    ``paginate_by``
        Number of posts per page.
        
    **Template:**

    :template:`blog/index.html`
    """
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display an individual :model:`blog.Post`.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`

    **Template:**

    :template:`blog/post_detail.html`
    """
    # By default only published posts are visible. Allow staff users
    # and the post's author to view unpublished drafts.
    if request.user.is_staff:
        queryset = Post.objects.all()
    elif request.user.is_authenticated:
        queryset = Post.objects.filter(Q(status=1) | Q(author=request.user))
    else:
        queryset = Post.objects.filter(status=1)

    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        if request.POST.get("comment_id"):
            # Edit existing comment
            comment = get_object_or_404(Comment, pk=request.POST["comment_id"])
            if comment.author != request.user:
                messages.add_message(request, messages.ERROR, "You cannot edit this comment.")
            else:
                comment_form = CommentForm(data=request.POST, instance=comment)
                if comment_form.is_valid():
                    edited = comment_form.save(commit=False)
                    edited.approved = False  # re-moderate after edit
                    edited.save()
                    messages.add_message(request, messages.SUCCESS, "Comment updated and awaiting approval.")
                else:
                    messages.add_message(request, messages.ERROR, "Invalid data while updating comment.")
            comment_form = CommentForm()
        else:
            # Create new comment
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user
                comment.post = post
                comment.save()
                messages.add_message(
                    request, messages.SUCCESS, "Comment submitted and awaiting approval"
                )
            comment_form = CommentForm()

    comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    ``comment_form``
        An instance of :form:`blog.CommentForm`
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, "Comment Updated!")
        else:
            messages.add_message(request, messages.ERROR, "Error updating comment!")

    return HttpResponseRedirect(reverse("post_detail", args=[slug]))

def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``post``
        An instance of :model:`blog.Post`.
    ``comment``
        A single comment related to the post.
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def create_post(request):
    """View to create a new Post. Only for authenticated users."""
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # Ensure new posts are saved as Draft by default. Admins can
            # change status from the admin panel to publish.
            post.status = 0
            # Auto-generate a unique slug from the title if not provided.
            base_slug = slugify(post.title) or "post"
            slug = base_slug
            counter = 1
            while Post.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            post.slug = slug
            post.save()
            # Drafts are not visible to the public post_detail view (which
            # only shows published posts). Redirect staff to the post, but
            # regular users to home with a message.
            if request.user.is_staff or post.status == 1:
                messages.success(request, "Post created successfully.")
                return redirect("post_detail", slug=post.slug)
            else:
                messages.success(request, "Post saved as draft. An admin can publish it from the admin panel.")
                return redirect("home")
        else:
            messages.error(request, "There was an error creating the post.")
    else:
        form = PostForm()

    return render(request, "blog/create_post.html", {"form": form})