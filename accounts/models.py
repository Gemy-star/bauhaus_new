from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(
            self, email, first_name, last_name, phone, address,password=None,
            commit=True):
        """
        Creates and saves a User with the given email, first name, last name
        and password.
        """
        if not email:
            raise ValueError(_('Users must have an email address'))
        if not first_name:
            raise ValueError(_('Users must have a first name'))
        if not last_name:
            raise ValueError(_('Users must have a last name'))

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,

        )

        user.set_password(password)
        user.is_customer = False
        user.is_active = True
        user.is_admin = False
        user.is_staff = False
        user.is_engineer = False
        if commit:
            user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password, address, phone, ):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            address=address,
            phone=phone,

            commit=False,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.user_type = 1
        user.save(using=self._db)
        return user

    def create_customeruser(self, email, first_name, last_name, phone, address, password):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_customer = True
        user.is_admin = False
        user.is_engineer = False
        user.is_active = True
        user.user_type = 3
        user.save(using=self._db)
        return user

    def create_engineeruser(self, email, first_name, last_name, password, phone, address):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_admin = False
        user.is_engineer = True
        user.is_active = True
        user.is_staff = False
        user.is_customer = False
        user.user_type = 2
        user.save(using=self._db)
        return user

    def create_outdoor_engineeruser(self, email, first_name, last_name, password, phone, address):
        """
        Creates and saves a superuser with the given email, first name,
        last name and password.
        """
        user = self.create_user(
            email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            address=address,
            commit=False,
        )
        user.is_admin = False
        user.is_engineer = False
        user.is_active = True
        user.is_staff = False
        user.is_customer = False
        user.user_type = 4
        user.is_outdoor_engineer = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_('email address'), max_length=255, unique=True
    )
    # password field supplied by AbstractBaseUser
    # last_login field supplied by AbstractBaseUser
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    address = models.CharField(_('Address'), max_length=255, null=True, blank=True)
    is_customer = models.BooleanField(_('Customer'), default=False, help_text=_(
        'Designates whether this user should be treated as a Customer. '
    ), )
    is_engineer = models.BooleanField(_('Engineer'), default=False, help_text=_(
        'Designates whether this user should be treated as an Engineer. '
    ))
    is_admin = models.BooleanField(_('Admin'), default=False, help_text=_(
        'Designates whether this user should be treated as an Admin. '
    ))
    is_outdoor_engineer = models.BooleanField(_('outdoor engineer'), default=False, help_text=_(
        'Designates whether this user should be treated as an Outdoor Engineer. '
    ))
    USER_TYPE_CHOICES = (
        (1, 'admin'),
        (2, 'engineer'),
        (3, 'customer'),
        (4, 'outdoor_engineer'),

    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, verbose_name=_('User Type'),
                                                 help_text=_(
                                                     'User Role in A system '
                                                 ))

    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'
        ),
    )

    # is_superuser field provided by PermissionsMixin
    # groups field provided by PermissionsMixin
    # user_permissions field provided by PermissionsMixin

    date_joined = models.DateTimeField(
        _('date joined'), default=timezone.now
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', 'address']

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return '{} <{}>'.format(self.get_full_name(), self.email)

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
