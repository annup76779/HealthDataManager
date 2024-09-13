from enum import StrEnum


class UserType(StrEnum):
    Patient = 'patient'
    Doctor = 'doctor'
    Admin = 'admin'
