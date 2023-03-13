from django.db import models
from PIL import Image
import os
import datetime
from datetime import datetime
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as storage
from django.conf import settings
from pathlib import Path
from django.core.files import File
import subprocess


class ModelToTest(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField()
    image = models.ImageField(upload_to='images/avatar')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тестовая модель'
        verbose_name_plural = 'Тестовые модели'

    def save(self, *args, **kwargs):
        ### переписанный метод save для корректной работы с minio
        super().save(*args, **kwargs)
        image_read = storage.open(self.image.name, "r")
        print(image_read)
        image = Image.open(image_read)
        if image.height > 200 or image.width > 200:
            output_size = (200, 200)
            imageBuffer = BytesIO()
            image.thumbnail(output_size)
            image.save(imageBuffer, image.format)
            self.image.save(self.image.name.split('/')[-1], ContentFile(imageBuffer.getvalue()))
        image_read.close()


def file_pfx_directory_path(instance, filename):
    return f'PFX/{instance.username}/{filename}'


def file_pem_directory_path(instance, filename):
    return f'PEM/{instance.username}/{filename}'


def convert_pfx_to_pem(pfx_path, pfx_password, pem_path):
    cmd = f"openssl pkcs12 -in {pfx_path} -out {pem_path} -nodes -password pass:{pfx_password}"
    subprocess.call(cmd, shell=True)


class Certificate(models.Model):
    username = models.CharField(max_length=25, verbose_name='Имя пользователя КИБ')
    password = models.CharField(max_length=25, verbose_name='Пароль от учетной записи КИБ')
    password_to_cert = models.CharField(max_length=25, verbose_name='Пароль для сертификата')
    cert_file_pfx = models.FileField(upload_to=file_pfx_directory_path, verbose_name='Сертификат: PFX')
    cert_file_pem = models.FileField(upload_to=file_pem_directory_path, verbose_name='Сертификат: PEM',
                                     blank=True)


# рабочий метод save с CRM. Но с minio пока что не работает


    def save(self, *args, **kwargs):
        # path = os.path.exists(f'files/PEM/{self.username}_{datetime.now().strftime("%Y-%m-%d_%H-%M")}')
        # if not path:
        #     os.makedirs(f'files/PEM/{self.username}_{datetime.now().strftime("%Y-%m-%d_%H-%M")}')
        # pem_path = f'files/PEM/{self.username}_{datetime.now().strftime("%Y-%m-%d_%H-%M")}/cert_file.pem'
        # super().save(*args, **kwargs)
        # convert_pfx_to_pem(f'files/{str(self.cert_file_pfx)}', self.password_to_cert,
        #                    f'{pem_path}')
        # self.cert_file_pem = pem_path[6:]
        # super().save(*args, **kwargs)