from django.test import TestCase
from django.contrib.auth.models import User
from blogtest.models import Post
from django.urls import reverse
from .forms import PostForm


class PostModelTest(TestCase):

    def setUp(self):
        # setUp() runs before EVERY test method in this class
        self.user = User.objects.create_user(username='alice', password='pass')
        self.post = Post.objects.create(
            title='Hello World',
            content='one two three four five',
            author=self.user,
            published=True,
        )

    def test_str_returns_title(self):
        self.assertEqual(str(self.post), 'Hello World')

    def test_word_count(self):
        self.assertEqual(self.post.word_count(), 5)

    def test_default_published_is_false(self):
        draft = Post.objects.create(
            title='Draft', content='x', author=self.user)
        self.assertFalse(draft.published)


class PostViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='pass')
        self.post = Post.objects.create(title='How to create Enums in Python',
                                        content='Subclass the Enum class', author=self.user, published=True)
        self.draft = Post.objects.create(title='How to use GeoDjango', content='Use pip to install the package',
                                         author=self.user, published=False)

    # anonymous access
    def test_post_list_status_200(self):
        url = reverse('post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_list_only_shows_published(self):
        response = self.client.get(reverse('post_list'))
        self.assertIn(self.post, response.context['posts'])
        self.assertNotIn(self.draft, response.context['posts'])

    def test_post_list_uses_correct_template(self):
        response = self.client.get(reverse('post_list'))
        self.assertTemplateUsed(response, 'post_list.html')

    # --- login-required views ---
    def test_create_post_redirects_anonymous(self):
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 302)   # redirect to login

    def test_create_post_accessible_when_logged_in(self):
        self.client.login(username='bob', password='pass')
        response = self.client.get(reverse('create_post'))
        self.assertEqual(response.status_code, 200)

      # --- POST request ---
    def test_delete_post_forbidden_for_non_author(self):
        other = User.objects.create_user(username='eve', password='pass')
        self.client.login(username='eve', password='pass')
        response = self.client.post(reverse('delete_post', args=[self.post.pk]))
        self.assertEqual(response.status_code, 403)


class PostFormTest(TestCase):

    def test_valid_form(self):
        form = PostForm(data={'title': 'My Great Post', 'content': 'Some content here.'})
        self.assertTrue(form.is_valid())

    def test_missing_title(self):
        form = PostForm(data={'content': 'No title here.'})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)

    def test_title_too_short(self):
        form = PostForm(data={'title': 'Hi', 'content': 'Body text here.'})
        self.assertFalse(form.is_valid())
        self.assertIn('Title must be at least 5 characters', str(form.errors['title']))