from django.db import models
from apps.core.models import CreatedUpdatedAbstractModel
from apps.authentication.models import User

class Region(CreatedUpdatedAbstractModel):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class TreatmentType(CreatedUpdatedAbstractModel):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name

class Treatment(CreatedUpdatedAbstractModel):
    patient = models.ForeignKey(
        User,
        on_delete = models.SET_NULL,
        related_name = 'patient_treatments',
        limit_choices_to = {'role':User.Roles.PATIENT},
        blank = True,
        null = True,
    )
    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name = 'doctor_treatments',
        limit_choices_to = {'role':User.Roles.DOCTOR},
        blank = True,
        null = True,
    )
    treatment_type = models.ForeignKey(
        TreatmentType,
        on_delete=models.SET_NULL,
        related_name = 'treatments',
        blank = True,
        null = True,
    )

    total_treatment_cost = models.PositiveIntegerField()
    total_paid = models.PositiveIntegerField()
    visit_number = models.PositiveIntegerField()

    tooth_number = models.PositiveIntegerField()
    start_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

class Service(CreatedUpdatedAbstractModel):
    name = models.CharField(max_length = 255)
    price = models.PositiveIntegerField()
    duration_minutes = models.PositiveIntegerField()
    treatment_type = models.ForeignKey(
        TreatmentType,
        on_delete=models.CASCADE,
        related_name='services'
    )
    is_active = models.BooleanField(default = True)

    def __str__(self):
        return self.name

class Material(CreatedUpdatedAbstractModel):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name='materials'
    )
    name = models.CharField(max_length = 255)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name





