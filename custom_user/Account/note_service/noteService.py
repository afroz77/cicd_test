from .models import NoteModel, Account
from django.core.exceptions import ObjectDoesNotExist

class noteService:

    def get_note(self, note_id):
        try:
            return NoteModel.objects.get(id=note_id)
        except ObjectDoesNotExist as e:
            return False

    def collaborate_note(self, email, note_id):

        note_obj = NoteModel.objects.get(id=note_id)
        user_ubj = Account.objects.get(email=email)

        for i in note_obj.collaborator:
            if i is user_ubj:
                return False
        if user_ubj == note_obj.created_by:
            return False
        note_obj.collaborator.add(user_ubj)

        return True