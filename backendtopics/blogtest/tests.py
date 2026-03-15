from django.test import TestCase
from django.contrib.auth.models import User
from blogtest.models import Post
from django.urls import reverse
from .forms import PostForm

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Shared, never modified — created once
        cls.user = User.objects.create_user(username='alice', password='pass')
        cls.published_post = Post.objects.create(
            title='Public', content='hello', author=cls.user, published=True
        )
    # def setUp(self):
    #     self.user = User.objects.create(username='John', password='pas123')
    #     self.post = Post.objects.create(title='How to make pancakes on weekends', content='Browse the web for how',
    #                                     author=self.user)

    def test_post_str_returns_title(self):
        self.assertEqual(self.published_post.title, 'How to make pancakes on weekends')

    def test_post_published_default(self):
        self.assertEqual(self.published_post.published, False)

    def test_word_count(self):
        self.assertEqual(self.published_post.word_count(), 5)

    def test_default_published_is_false(self):
        draft = Post.objects.create(
            title='Draft', content='x', author=self.user)
        self.assertFalse(draft.published)


# class PostViewTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='bob', password='pass')
#         self.post = Post.objects.create(title='How to create Enums in Python',
#                                         content='Subclass the Enum class', author=self.user, published=True)
#         self.draft = Post.objects.create(title='How to use GeoDjango', content='Use pip to install the package',
#                                          author=self.user, published=False)

#     def test_delete_non_author_fail(self):
#         self.client.login(username='Jamil', password='pass234')
# #       response = self.client.post(reverse('delete_post', args=[self.post.pk]))
#         response = self.client.post(reverse('delete_post', args=[self.post.pk]))
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Post.objects.filter(pk=self.post.pk).exists(), True)


#     def test_post_flow(self):
#         self.other_user = User.objects.create_user(username='Bart', password='bart123')
#         self.client.login(username='Bart', password='bart123')
#         response = self.client.post(reverse('create_post'), {'title': 'A new post', 'content': 'Some content goes here'})
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Post.objects.filter(title='A new post').exists(), True)

    # def test_post_list_success_anonymous(self):
    #     url = reverse('post_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_post_list_published(self):
    #     url = reverse('post_list')
    #     response = self.client.get(url)
    #     self.assertIn(self.post, response.context['posts'])
    #     self.assertNotIn(self.draft, response.context['posts'])

    # def test_anonymous_user_redirect(self):
    #     self.user = User.objects.create(username='Bilal', password='bilal123')
    #     response = self.client.get(reverse('create_post'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, '/accounts/login/?next=/post/create/')

    # # anonymous access
    # def test_post_list_status_200(self):
    #     url = reverse('post_list')
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    # def test_post_list_only_shows_published(self):
    #     response = self.client.get(reverse('post_list'))
    #     self.assertIn(self.post, response.context['posts'])
    #     self.assertNotIn(self.draft, response.context['posts'])

    # def test_post_list_uses_correct_template(self):
    #     response = self.client.get(reverse('post_list'))
    #     self.assertTemplateUsed(response, 'post_list.html')

    # --- login-required views ---
    # def test_create_post_redirects_anonymous(self):
    #     response = self.client.get(reverse('create_post'))
    #     self.assertEqual(response.status_code, 302)   # redirect to login

    # def test_create_post_accessible_when_logged_in(self):
    #     self.client.login(username='bob', password='pass')
    #     response = self.client.get(reverse('create_post'))
    #     self.assertEqual(response.status_code, 200)

    #   # --- POST request ---
    # def test_delete_post_forbidden_for_non_author(self):
    #     other = User.objects.create_user(username='eve', password='pass')
    #     self.client.login(username='eve', password='pass')
    #     response = self.client.post(reverse('delete_post', args=[self.post.pk]))
    #     self.assertEqual(response.status_code, 403)


class PostFormTest(TestCase):
    form = PostForm(data={'title': 'shor', 'content': 'This is a short content!'})

    # def test_title_greater_5(self):
    #     self.assertIn('Title must be at least 5 characters.', self.form.errors['title'])

    # def test_valid_form(self):
    #     form = PostForm(data={'title': 'My Great Post',
    #                     'content': 'Some content here.'})
    #     self.assertTrue(form.is_valid())

    # def test_missing_title(self):
    #     form = PostForm(data={'content': 'No title here.'})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('title', form.errors)

    # def test_title_too_short(self):
    #     form = PostForm(data={'title': 'Hi', 'content': 'Body text here.'})
    #     self.assertFalse(form.is_valid())
    #     self.assertIn('Title must be at least 5 characters',
    #                   str(form.errors['title']))
