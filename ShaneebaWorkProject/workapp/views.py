
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework import status
from django.db.models import Q
class WorksGetPost(APIView):
    def get(self, request):
        res_data = list(Works.objects.all().values("str_title","txt_descrption","fk_project_id__str_name",
                                                   "jsn_attachment","dbl_estimatation","dat_start",
                                                   "dat_end","dat_created","fk_type_id__str_name","dat_approved",
                                                   "fk_work_status_id__str_name","dbl_taken","int_active"))
        return Response(res_data, status=status.HTTP_200_OK)

    def post(self, request):
        dict_data = request.data
        fk_project_id_id = dict_data["fk_project_id_id"] #oxgen digit
        project=Project.objects.filter(str_name=fk_project_id_id).get()
        int_project_id=project.id
        ins_project = Project.objects.get(id=int_project_id)
        fk_type_id_id = dict_data["fk_type_id_id"] #"bug"
        worktype=WorkType.objects.filter(str_name=fk_type_id_id).get()
        int_type_id=worktype.id
        ins_worktype = WorkType.objects.get(id=int_type_id)
        fk_work_status_id_id = dict_data["fk_work_status_id_id"]
        workstatus=WorkStatus.objects.filter(str_name=fk_work_status_id_id).get()
        int_workstatus_id=workstatus.id

        ins_work_status = WorkStatus.objects.get(id=int_workstatus_id)

        Works.objects.create(str_title=dict_data["str_title"], txt_descrption=dict_data["txt_descrption"],
                                         fk_project_id=ins_project,
                                         jsn_attachment=dict_data["jsn_attachment"],
                                         dbl_estimatation=dict_data["dbl_estimatation"],
                                         dat_start=dict_data["dat_start"],
                                         dat_end=dict_data["dat_end"], fk_type_id=ins_worktype,
                                         dat_approved=dict_data["dat_approved"], fk_work_status_id=ins_work_status,
                                         dbl_taken=dict_data["dbl_taken"],
                                         int_active=dict_data["int_active"])
        return Response('saved', status=status.HTTP_400_BAD_REQUEST)


class WorkUpdateDelete(APIView):
    def get(self, request, id):
        res_data = Works.objects.filter(id=id).values()
        print(res_data)
        return Response(res_data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        dict_data = request.data
        fk_project_id_id = dict_data["fk_project_id_id"]
        ins_project = Project.objects.get(id=fk_project_id_id)
        fk_type_id_id = dict_data["fk_type_id_id"]
        ins_worktype = WorkType.objects.get(id=fk_type_id_id)
        fk_work_status_id_id = dict_data["fk_work_status_id_id"]
        ins_work_status = WorkStatus.objects.get(id=fk_work_status_id_id)
        ins_works = Works.objects.get(id=id)
        ins_works.str_title=dict_data["str_title"]
        ins_works.text_descrption=dict_data["txt_descrption"]
        ins_works.fk_project_id=ins_project
        ins_works.jsn_attachment = dict_data["jsn_attachment"]
        ins_works.dbl_estimatation = dict_data["dbl_estimatation"]
        ins_works.dat_start = dict_data["dat_start"]
        ins_works.dat_end = dict_data["dat_end"]
        ins_works.fk_type_id = ins_worktype
        ins_works.dat_approved = dict_data["dat_approved"]
        ins_works.fk_work_status_id = ins_work_status
        ins_works.dbl_taken = dict_data["dbl_taken"]
        ins_works.int_active = dict_data["int_active"]
        ins_works.save()
        return Response("updated", status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        rst_data = Works.objects.get(id=id)
        rst_data.delete()
        return Response("deleted")

class ProjectView(APIView):
    def get(self, request):
        res_data = list(Project.objects.all().values("str_name"))
        return Response(res_data, status=status.HTTP_200_OK)

class WorkStatusView(APIView):
    def get(self, request):
        res_data = list(WorkStatus.objects.all().values("str_name"))
        return Response(res_data, status=status.HTTP_200_OK)

class WorkTypeView(APIView):
    def get(self, request):
        res_data = list(WorkType.objects.all().values("str_name"))
        return Response(res_data, status=status.HTTP_200_OK)

class DateFilter(APIView):
    def get(self,request):
        print(request.data)
        res_data = list(Works.objects.all().filter(Q(dat_start= "2021-08-20") & Q(dat_end="2021-08-30")).values("str_title","txt_descrption","fk_project_id__str_name",
                                                   "jsn_attachment","dbl_estimatation","dat_start",
                                                   "dat_end","dat_created","fk_type_id__str_name","dat_approved",
                                                   "fk_work_status_id__str_name","dbl_taken","int_active"))
        return Response(res_data, status=status.HTTP_200_OK)



class DeleteWork2(APIView):
    def put(self,request,id):

        ins_work=Works.objects.get(id=id)

        ins_work.int_active=-1
        ins_work.save()
        return Response('delete')
