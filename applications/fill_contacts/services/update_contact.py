from django.shortcuts import render, get_object_or_404
from applications.fill_contacts.models import PhoneUser
from django.utils import timezone


def update_user(request, user_id, new_name, new_number):
    phoneuser = get_object_or_404(PhoneUser, id=user_id)
    if new_name:
        phoneuser.name = new_name

    if new_number:
        phoneuser.phone_number = new_number

    phoneuser.is_auto_generated = False
    phoneuser.date_update = timezone.now()
    phoneuser.save()
    return render(request, "delete_user.html", {"phoneuser": phoneuser})
