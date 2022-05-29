from rest_framework import serializers

from ToDo_models.models import Task, Comment


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        read_only_fields = ("authors",)


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.SlugRelatedField(
        slug_field="username",  # указываем новое поле для отображения
        read_only=True,  # поле для чтения
        many=False
        )

    class Meta:
        model = Comment
        fields = ("author", "comment")


class TaskDetailSerializer(serializers.ModelSerializer):
    """ Одна статья блога """
    authors = serializers.SlugRelatedField(
        slug_field="username",  # указываем новое поле для отображения
        read_only=True,  # поле для чтения
        many=True
    )
    comments = CommentSerializer(many=True, read_only=True)  # one-to-many-relationships

    class Meta:
        model = Task
        fields = (
            'id', 'title', 'text', 'execution_time', "important", 'status', 'public',  # из модели
            'authors', 'comments',  # из сериализатора
        )
