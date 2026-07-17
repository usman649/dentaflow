from apps.core.exceptions import ObjectNotFoundException
from apps.authentication.models import User

class PatientRepository:
    def get_patients(self):
        patients = User.objects.filter(role=User.Roles.PATIENT)
        return patients


    def get_patient(self,user_id):
        patient = User.objects.filter(id=user_id,role=User.Roles.PATIENT).first()
        if not patient:
            raise ObjectNotFoundException(
                message="Patient not found",
                message_key="patient_not_found",
            )
        return patient


