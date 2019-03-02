from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class DefautlModel(models.Model):
    created = models.DateTimeField(auto_now=True)
    modified = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


class UserManager(BaseUserManager, models.Manager):
    def _create_user(self, correo, password,
                     is_staff, is_superuser, **extra_fields):
        if not correo:
            raise ValueError('El email debe ser obligatorio')
        correo = self.normalize_email(correo)

        user = self.model(correo=correo,
                          is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, correo, password=None, **extra_fields):
        return self._create_user(
            correo, password, False, False, **extra_fields)

    def create_superuser(self, correo, password, **extra_fields):
        return self._create_user(
            correo, password, True, True, **extra_fields)


class User(AbstractBaseUser,PermissionsMixin, models.Model):
	
    correo = models.EmailField(unique=True,verbose_name='Correo Electrónico')
    nombre = models.CharField(max_length=50, verbose_name='Nombres',blank=True,null=True)
    ap_paterno = models.CharField(max_length=50, verbose_name='Apellido paterno',blank=True,null=True)
    ap_materno = models.CharField(max_length=50, verbose_name='Apellido materno',blank=True,null=True)
    fecha_nacimiento = models.DateTimeField(blank=True,null=True)
    telefono_personal = models.CharField(max_length=20, verbose_name='Teléfono personal',blank=True,null=True)


    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'correo'

    def get_short_name(self):
        return self.nombre