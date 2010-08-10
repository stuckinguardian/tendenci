from django.forms import ModelForm

from perms.fields import UserPermissionField, user_perm_queryset, users_with_perms

class TendenciBaseForm(ModelForm):
    """
        Base form that adds user permission fields
    """
    user_perms = UserPermissionField()

    def __init__(self, user=None, *args, **kwargs):

        print 'user:', user

        self.user = user
        super(TendenciBaseForm, self).__init__(*args, **kwargs)
        if 'instance' in kwargs:
            instance = kwargs['instance']
            # pull all users except for the creator and the owner
            query_set =  user_perm_queryset([instance.creator, instance.owner])
            self.fields['user_perms'].queryset = query_set
            self.fields['user_perms'].initial = users_with_perms(instance)  
        else:
            # pull all users except for the current one viewing the form
            self.fields['user_perms'].queryset = user_perm_queryset(self.user)