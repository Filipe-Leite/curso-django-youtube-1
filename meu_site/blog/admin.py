from django.contrib import admin
from .models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display        = ('titulo', 'slug', 'autor', 'publicado','status')
    list_filter         = ('status', 'criado', 'publicado', 'autor')
    raw_id_fields       = ('autor',)
    date_hierarchy      = 'publicado'
    search_fields       = ('titulo', 'conteudo')
    prepopulated_fields = {'slug':('titulo',)}

"""
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
"""