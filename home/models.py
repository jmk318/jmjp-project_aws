from django.db import models

# Create your models here.
class CompanyInfo(models.Model):
    company_name = models.CharField(primary_key=True, max_length=50)
    gpt_comment = models.TextField(blank=True, null=True)
    sentiment_analysis_ratio = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)        
    company_code = models.CharField(max_length=10, blank=True, null=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    website = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company_info'