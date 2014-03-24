# -*- coding: utf-8 -*-
from django.db import models
from common.models import UpdateModel, UserModel
from django.contrib.auth.models import User
from chapter import Chapter
import re
import json

STYLE = (
        ('a', '注释'),
        ('l', '单线'),
        ('d', '双线'),
        )
class Annotation(UpdateModel):
    '批注'
    chapter=models.ForeignKey(Chapter,
            related_name='anotations',
            verbose_name='章节'
            )
    row=models.IntegerField(
            verbose_name='行号'
            )
    start=models.IntegerField(
            verbose_name='起始'
            )
    end=models.IntegerField(
            default=0,
            verbose_name='结束'
            )
    style = models.CharField(
            max_length=1,
            default='a',
            choices=STYLE,
            verbose_name='式样',
            )
    context=models.TextField(
            blank=True, null=True,
            verbose_name='正文',
            )

    def toJson(self):
        '转换成JSON字串'
        return json.dumps({
            'id': self.id,
            'row': self.row,
            'start': self.start,
            'end': self.end,
            'context': self.context,
            'style': self.style
            })

    @staticmethod
    def annotate(obj):
        '增加批注'
        if obj.chapter.anotations.filter(row=obj.row,
                start=obj.start, end=obj.end, style=obj.style).count() > 0:
            return '标注重复，请修改'
        obj.save()
        return obj

    def _select(self):
        row = self.chapter.context.split('\n')[self.row - 1]
        regex = re.compile("(?x) (?: [\w-]+ | [\x80-\xff]{3} )")
        ret = regex.findall(row.encode('utf-8'))
        for i in ['，', '。']:
            while i in ret:
                ret.remove(i)
        return ret

    def select(self):
        '显示批注的目标内容'
        return ''.join(self._select()[self.start - 1 : self.end])

    def __unicode__(self):
        return u'%s:%s:%d'%(self.chapter, self.create_by, self.id)

    class Meta:
        verbose_name = '批注'
        verbose_name_plural = '批注'
        ordering = ['row', 'start']
        unique_together = ('create_by', 'chapter', 'row', 'start', 'end', 'style')
        app_label = 'book'
