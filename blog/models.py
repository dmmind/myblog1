from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField
# 导入django自带用户模块


# Create your models here.
# 分类表结构设计：
# 表名：Category、分类名：name
class Category(models.Model):
    # 字符串字段  单行输入，用于较短的字符串，
    # 如要保存大量文本,使用TextField。
    # 必须max_length参数，
    # django会根据这个参数在数据库层和校验层限制该字段所允许的最大字符数。
    name = models.CharField('博客分类', max_length=100)
    # 整形 用于保存一个整数，default，数据库中字段的默认值
    index = models.IntegerField(default=999, verbose_name='分类排序')

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField('文章标签', max_length=100)

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 推荐位
class Tui(models.Model):
    name = models.CharField('推荐位', max_length=100)

    class Meta:
        verbose_name = '推荐位'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章表结构设计：
# 表名：Article、标题：title、摘要：excerpt、分类：category、标签：tags、推荐位、内容：body、
# 创建时间：created_time、作者：user、文章封面图片img
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.DO_NOTHING,
        verbose_name='分类',
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d', verbose_name='文章图片', blank=True, null=True)
    # 字符串 = longtext，一个容量很大的文本字段，
    # admin 管理界面用<textarea>多行编辑框表示该字段数据。
    body = UEditorField('内容', width=800, height=500,
                        toolbars='full', imagePath='upimg/', filePath='upfile',
                        settings={}, command=None, blank=True
                        )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    """
        文章作者，这里User是从django.contrib.auth.models导入的。
        这里我们通过 ForeignKey 把文章和 User 关联了起来。
    """
    # 正Integer，类似IntegerField，但取值范围为非负整数（这个字段应该是允许0值的…可以理解为无符号整数）
    views = models.PositiveIntegerField('阅读量', default=0)
    tui = models.ForeignKey(Tui, on_delete=models.DO_NOTHING, verbose_name='推荐位', blank=True,null=True)
    # 日期类型，datetime，同DateField的参数
    # DateField---日期类型，date，
    # 对于参数，auto_now = True，则每次更新都会更新这个时间；
    # auto_now_add，则只是第一次创建添加，之后的更新不再改变。
    created_time = models.DateTimeField('发布时间', auto_now_add=True)
    modified_time = models.DateTimeField('发布时间', auto_now=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __str__(self):
        return self.title


# Banner
class Banner(models.Model):
    text_info = models.CharField('标题', max_length=50, default='')
    img = models.ImageField('轮播图', upload_to='banner/')
    link_url = models.URLField('图片链接', max_length=100)
    # 布尔类型 = tinyint(1)不能为空，Blank = True
    is_active = models.BooleanField('是否是active', default=False)

    def __str__(self):
        return self.text_info

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = '轮播图'


# 有情链接
class Link(models.Model):
    name = models.CharField('连接名称', max_length=20)
    # 字符串，地址正则表达式,用于保存URL。
    # 若verify_exists参数为True(默认)，
    # 给定的URL会预先检查是否存在(即URL是否被有效装入且没有返回404响应)
    linkurl = models.URLField('网址', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = '友情链接'




