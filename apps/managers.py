from django.contrib.auth.base_user import BaseUserManager

class TeacherManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone_number, password, **extra_fields):
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, phone_number, 
                            password, **other_fields):
            other_fields.setdefault('is_staff', True)
            other_fields.setdefault('is_superuser', True)
            other_fields.setdefault('is_active', True)
            
            if other_fields.get('is_staff') is not True:
                raise ValueError('Superuser must be assigned to is_staff=True.')
            
            if other_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must be assigned to is_superuser=True.')
            
            return self.create_user(phone_number=phone_number,
                                    password=password,
                                    **other_fields)