from django.db import models

class Project(models.Model):
    str_name=models.CharField(max_length=50,null=False)
    str_code=models.CharField(max_length=5,null=False)
    choices=[(int_number,int_number) for int_number in range(2)]
    int_status=models.IntegerField(choices=choices,null=False,default=1)

    def __str__(self):
        return self.str_name

class WorkType(models.Model):
    str_name = models.CharField(max_length=50, null=False)
    int_order=models.IntegerField(null=False)

    def __str__(self):
        return self.str_name

class WorkStatus(models.Model):
    choices=(
        ('new','new'),
        ('developed','developed'),
        ('tested','tested'),
        ('deployed','deployed')
    )
    str_name = models.CharField(choices=choices,max_length=50, null=False)
    str_code = models.CharField(max_length=50, null=False)
    int_order = models.IntegerField(null=False)

    def __str__(self):
        return self.str_name

class Works(models.Model):
    str_title=models.CharField(max_length=300,null=False)
    txt_descrption=models.TextField(null=False)
    fk_project_id=models.ForeignKey(Project,on_delete=models.CASCADE,null=False)
    jsn_attachment=models.JSONField(null=True,blank=True)
    dbl_estimatation=models.FloatField(null=True,blank=True)
    dat_start=models.DateField(null=True,blank=True)
    dat_end=models.DateField(null=True,blank=True)
    dat_created=models.DateField(auto_now=True)
    fk_type_id=models.ForeignKey(WorkType,on_delete=models.CASCADE)
    dat_approved=models.DateTimeField(null=True,blank=True)
    fk_work_status_id=models.ForeignKey(WorkStatus,on_delete=models.CASCADE)
    dbl_taken=models.FloatField(default=0)
    int_active=models.IntegerField(default=0)

    def __str__(self):
        return self.str_title

