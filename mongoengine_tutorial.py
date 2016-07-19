#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Xiang Wang @ 2016-06-22 14:06:25

from mongoengine import *
connect('tumblelog')    # 链接到 tumblelog 这个数据库


class User(Document):
    name = StringField()
    email = StringField()
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Book1(Document):
    name = StringField(required=True)
    author = ReferenceField(User)


class User_embeded(EmbeddedDocument):
    name = StringField(required=True)


class Book2(Document):
    name = StringField(required=True)
    author = EmbeddedDocumentField(User_embeded)

w = User_embeded(name='王祥2')
b = Book2(name="第二本书2", author=w)
b.save()
w.name= '王祥4'
w.save()


class Comment(EmbeddedDocument):
    content = StringField()
    name = StringField(max_length=120)


class Post(Document):
    title = StringField(max_length=120, required=True)
    author = ReferenceField(User, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    comments = ListField(EmbeddedDocumentField(Comment))
    
    meta = {'allow_inheritance': True}


class TextPost(Post):
    content = StringField()


class ImagePost(Post):
    image_path = StringField()


class LinkPost(Post):
    link_url = StringField()





# ross = User(email='ross@example.com',
#             first_name='Ross',
#             last_name='Lawley').save()
# post1 = TextPost(title='Fun with MongoEngine', author=john)
# post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
# post1.tags = ['mongodb', 'mongoengine']
# post1.save()

# post2 = LinkPost(title='MongoEngine Documentation', author=ross)
# post2.link_url = 'http://docs.mongoengine.com/'
# post2.tags = ['mongoengine']
# post2.save()