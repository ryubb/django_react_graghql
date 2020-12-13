import graphene
from graphene_django import DjangoObjectType
from .models import UserModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class UserQuery(graphene.ObjectType):
    users = graphene.List(User)


class Query(UserQuery,
            graphene.ObjectType):
    pass


schema = graphene.Schema(
    query=Query,
)
