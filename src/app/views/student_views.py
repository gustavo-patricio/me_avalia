from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import datetime
from app import models, schemas, auth
from me_avalia import CLASS_RATING_EXPIRATION


class JsonResponse(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = {'aluno': data[0], 'aula': data[1]}
        return super().render(response, accepted_media_type, renderer_context)

class StudentViewSet(generics.RetrieveAPIView):
    queryset = models.Student.objects.all()
    renderer_classes = [JsonResponse]

    def retrieve(self, request, *args, **kwargs):
        try:
            user_id = self.request.user.pk
            aluno = models.Student.objects.filter(user=user_id)
            classroomstudent = models.ClassroomStudent.objects.all()
            classroomstudent = classroomstudent.filter(student_id=aluno.first().uuid)
            data = schemas.StudentSerializer(aluno, many=True)
            for classroom in classroomstudent:
                universityclasses = models.UniversityClass.objects.filter(classroom_id=classroom.classroom_id.uuid)
                if universityclasses:
                    universityclass = universityclasses.order_by('-final').first()
                    duration = datetime.datetime.now() - universityclass.final
                    if (duration < datetime.timedelta(minutes=CLASS_RATING_EXPIRATION)) :
                        aula = schemas.UniversityClassSerializer(universityclass)
                        response = [data.data[0], aula.data]

                        return Response(response)
                    
            response = [data.data[0], {}]
        
            return Response(response)
        except Exception as e:
            raise e

 
class StudentRetrieve(views.APIView):
    permission_classes = [auth.StudentPermission]
    def get(self, request, format=None):

        try:
            user_id = self.request.user.pk
            aluno = models.Student.objects.filter(user=user_id)
            classroomstudent = models.ClassroomStudent.objects.all()
            classroomstudent = classroomstudent.filter(student_id=aluno.first().uuid)
            data = schemas.StudentSerializer(aluno, many=True)
            for classroom in classroomstudent:
                universityclasses = models.UniversityClass.objects.filter(classroom_id=classroom.classroom_id.uuid)
                if universityclasses:
                    universityclass = universityclasses.order_by('-final').first()
                    duration = datetime.datetime.now() - universityclass.final
                    if (duration < datetime.timedelta(minutes=CLASS_RATING_EXPIRATION)) :
                        aula = schemas.UniversityClassSerializer(universityclass)
                        response = [data.data[0], aula.data]

                        return Response(response)
                    
            response = [data.data[0], {}]
        
            return Response(response)
        except Exception as e:
            raise e



    
    


