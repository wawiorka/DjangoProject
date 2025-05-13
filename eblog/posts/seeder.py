from .models import Post
from django_seed import Seed
import random

seeder = Seed.seeder()

seeder.add_entity(Post, 10, {
    'author': lambda x: random.randint(1,3),
    'title': lambda x: seeder.faker.title(),
    'text': lambda x: seeder.faker.text(max_nb_chars=20),
    'created_at': lambda x: seeder.faker.past_datetime(),
    'published_at': lambda x: seeder.faker.past_datetime(),
    'updated_at': lambda x: seeder.faker.past_datetime()
})

inserted_pks = seeder.execute()


#
# import os
# import django
#
# os.environ.setdefault('DJANGO_SETTING_MODULE', 'eblog.settings')
# django.setup()
#
# from faker import Faker
# from .models import Post
#
# fake = Faker()
#
# def seed_posts(number=10):
#     for _ in range(number):
#         title = fake.title()
#         text = fake.test()
#
#         Post.objects.create(title=title, text=text)
#
# if __name__ == '__main__':
#     seed_posts(100)

