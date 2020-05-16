from blog.models import User, Board, Post
import factory


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    nickname = factory.Faker('name')
    password = factory.Faker('password')


class BoardFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Board

    title = factory.Faker('sentence')
    desc = factory.Faker('sentence')


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    writer = factory.SubFactory(UserFactory)
    # board_id = factory.SubFactory(BoardFactory)
    board_id = Board.objects.get(id=1)
    title = factory.Faker('sentence')
    body = factory.Faker('paragraph')
    view_count = 0
    ip = factory.Faker('ipv4')
    modify_password = factory.Faker('password')