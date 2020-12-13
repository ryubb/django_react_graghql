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
    @graphene.resolve_only_args
    def resolve_users(self):
        return UserModel.objects.all()


schema = graphene.Schema(query=Query)
