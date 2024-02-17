from django.db import models

# Create your models here.
class CorpInfo(models.Model):
    corp_code = models.CharField(primary_key=True, max_length=8)
    stock_name = models.CharField(max_length=50, blank=True, null=True)
    stock_code = models.CharField(max_length=6, blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    gpt_comment = models.TextField(blank=True, null=True)
    sentiment_analysis_ratio = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_info'

class Top500(models.Model):
    종목명 = models.CharField(primary_key=True, max_length=50)
    기준 = models.CharField(max_length=10, blank=True, null=True)
    시장 = models.CharField(max_length=6, blank=True, null=True)
    자산총계 = models.IntegerField(blank=True, null=True)
    자본금 = models.IntegerField(blank=True, null=True)
    자본총계 = models.IntegerField(blank=True, null=True)
    매출액 = models.IntegerField(blank=True, null=True)
    영업이익 = models.IntegerField(blank=True, null=True)
    순이익 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'top500'