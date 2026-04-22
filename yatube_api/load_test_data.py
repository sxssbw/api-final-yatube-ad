from django.contrib.auth import get_user_model
from posts.models import Group, Post, Comment, Follow

User = get_user_model()

Follow.objects.all().delete()
Comment.objects.all().delete()
Post.objects.all().delete()
Group.objects.all().delete()
User.objects.filter(is_superuser=False).delete()

user = User.objects.create_user(username='TestUser', password='1234567')
user_2 = User.objects.create_user(username='TestUser2', password='1234567')
another_user = User.objects.create_user(username='TestUserAnother',
                                        password='1234567')

group_1 = Group.objects.create(title='Группа 1', slug='group_1')
group_2 = Group.objects.create(title='Группа 2', slug='group_2')

post = Post.objects.create(text='Тестовый пост 1', author=user, group=group_1)
post_2 = Post.objects.create(text='Тестовый пост 12342341', author=user,
                             group=group_1)
another_post = Post.objects.create(text='Тестовый пост 2', author=another_user,
                                   group=group_2)

Comment.objects.create(author=user, post=post, text='Коммент 1')
Comment.objects.create(author=another_user, post=post, text='Коммент 2')
Comment.objects.create(author=user, post=another_post, text='Коммент 12')

Follow.objects.create(user=user, following=another_user)
Follow.objects.create(user=user_2, following=user)
Follow.objects.create(user=user_2, following=another_user)
Follow.objects.create(user=another_user, following=user)
Follow.objects.create(user=user, following=user_2)
