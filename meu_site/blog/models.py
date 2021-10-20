from django.db                       import models
from django.dispatch                 import receiver                
from django.db.models.fields.related import create_many_to_many_intermediary_model
from django.db.models.signals        import post_save
from django.utils                    import timezone
from django.urls                     import reverse
from django.utils.text               import slugify
from django.contrib.auth.models      import User


# Create your models here.

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset()\
                                           .filter(status='publicado')

class Post(models.Model):
    STATUS    = (
        ('rascunho', 'Rascunho'),
        ('publicado', 'Publicado'),
    )
    titulo    = models.CharField(max_length=250)
    slug      = models.SlugField(max_length=250)
    autor     = models.ForeignKey(User,
                               on_delete=models.CASCADE)
    conteudo  = models.TextField()
    publicado = models.DateTimeField(default=timezone.now)
    criado    = models.DateTimeField(auto_now_add=True)
    alterado  = models.DateTimeField(auto_now=True)
    status    = models.CharField(max_length=10,
                                choices=STATUS,
                                default='rascunho')
    
    objects   = models.Manager()
    published = PublishedManager()

    def get_absolute_url(self):
        return reverse('post_detail',args=[self.pk])

    def get_absolute_url_update(self):
        return reverse('post_edit',args=[self.pk])

    class Meta:
        ordering = ('-publicado',)

    def __str__(self):
        return self.titulo

@receiver(post_save,sender=Post)
def insert_slug(sender,instance,**kwargs):
    if kwargs.get('created',False):
        print('Criado slug')
    if not instance.slug:
        instance.slug = slugify(instance.titulo)
        return instance.save()