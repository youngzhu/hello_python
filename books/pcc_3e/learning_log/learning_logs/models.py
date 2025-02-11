from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """
    A topic the user is learning about.
    主题
    """
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """
    Something specific learned about a topic.
    条目
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    # 我们在 Entry 类中嵌套了 Meta 类。
    # Meta 存储⽤于管理模型的额外信息。
    # 在这⾥，它让我们能够设置⼀个特殊属性，让 Django 在需要时使⽤ Entries 表⽰多个条⽬。
    # 如果没有这个类，Django 将使⽤ Entrys表⽰多个条⽬
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."