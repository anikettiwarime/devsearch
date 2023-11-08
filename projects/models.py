from django.db import models
import uuid
# Create your models here.
from users.models import Profile


class Project(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateField(auto_now_add=True)
    owner = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, blank=True, null=True)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_images = models.ImageField(
        null=True, blank=True, default="default.jpg")

    tags = models.ManyToManyField('Tag', blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['-vote_total', '-vote_ratio', 'title']

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upvotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upvotes/totalVotes)*100

        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()


class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    VOTE_TYPE = (
        ('up', 'up vote'),
        ('down', 'down vote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = [['owner', 'project']]

    def __str__(self) -> str:
        return str(self.owner.name) + " " + str(self.value)


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
