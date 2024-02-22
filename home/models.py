from django.db import models

# Create your models here.
class CorpInfo(models.Model):
    corp_code = models.CharField(primary_key=True, max_length=8)
    stock_name = models.CharField(max_length=50, blank=True, null=True)
    stock_code = models.CharField(max_length=6, blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    gpt_comment = models.TextField(blank=True, null=True)
    sentiment_analysis_ratio = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    sentiment_analysis_ratio_prev_1 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    sentiment_analysis_ratio_prev_2 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    sentiment_analysis_ratio_prev_3 = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_info'