import graphene
from graphene_django import DjangoObjectType
from .models import UserModel


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel


class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    user = graphene.Field(
        UserType,
        id=graphene.Int(),
    )

    # @graphene.resolve_only_args
    def resolve_users(self, info, **kwargs):
        return UserModel.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        return UserModel.objects.get(pk=id)


class CreateUser(graphene.Mutation):
    id = graphene.Int()
    email = graphene.String()
    name = graphene.String()
    name_kana = graphene.String()
    tel_number = graphene.String()

    user = graphene.Field(UserType)

    class Arguments:
        email = graphene.String()
        name = graphene.String()
        name_kana = graphene.String()
        tel_number = graphene.String()

    def mutate(self, info, email, name, name_kana, tel_number):
        user = UserModel.objects.create(
            email=email, name=name, name_kana=name_kana, tel_number=tel_number)
        return CreateUser(
            email=email, name=name, name_kana=name_kana, tel_number=tel_number
        )


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
)
