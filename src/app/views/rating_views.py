from rest_framework import generics
from rest_framework.response import Response
import datetime
from app import models, schemas
from app.auth import custom_permissions, auth_exceptions



class RatingPostViewSet(generics.CreateAPIView):
    queryset = models.Rating.objects.all()
    serializer_class = schemas.PostRatingSerializer
    permission_classes = [custom_permissions.StudentPermission]

class RatingUpdateView(generics.UpdateAPIView):
    queryset = models.Rating.objects.all()
    serializer_class = schemas.PutRatingSerializer
    permission_classes = [custom_permissions.StudentPermission]

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            date_created = instance.date_created


            r = datetime.datetime.today() - datetime.datetime(
                                                        year=date_created.year,
                                                        month=date_created.month,
                                                        day=date_created.day,
                                                        hour=date_created.hour,
                                                        minute=date_created.minute)

            if r <= datetime.timedelta(days=1):
                serializer = self.get_serializer(instance, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
            else: 
                raise auth_exceptions.PermissionException(code=404, detail=[{'msg': 'sua permissão de avaliação expirou'}])
        
        except Exception as e:
            raise e

class RatingGetViewset(generics.RetrieveAPIView):
    queryset = models.Rating.objects.all()
    serializer_class = schemas.RatingSerializer
    permission_classes = [custom_permissions.StudentPermission]

