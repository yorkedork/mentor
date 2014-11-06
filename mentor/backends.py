from arcutils.ldap import ldapsearch, parse_profile, escape
from djangocas.backends import CASBackend
from mentor.users.models import User
from django.conf import settings
from django.core.exceptions import PermissionDenied

class PSUBackend(CASBackend):
    def get_or_init_user(self, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            results = ldapsearch("(uid=" + escape(username) + ")")
            user = User.objects.create_user(username,'')
            # get the user's first and lastname
            dn, entry = results[0]
            profile = parse_profile(entry)
            user.first_name = profile['first_name']
            user.last_name = profile['last_name']
            user.email = profile['email']
            user.save()

        return user
