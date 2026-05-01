from import_export import resources
from apps.users.models import User

class UserResources(resources.ModelResource):
    class Meta:
        model = User