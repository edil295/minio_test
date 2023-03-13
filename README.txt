### Настройки для settings

# Остаются также
# DEFAULT_FILE_STORAGE = "minio_storage.storage.MinioMediaStorage"
# STATICFILES_STORAGE = "minio_storage.storage.MinioStaticStorage"

# MINIO_STORAGE_ENDPOINT = хост где крутится minio сервер/хранилище \\\ example "192.168.0.102:9000"
# MINIO_STORAGE_ACCESS_KEY = Имя пользователя от хранилища  \\\ example 'minioadmin'
# MINIO_STORAGE_SECRET_KEY = Пароль от хранилища \\\ example 'minioadmin'
# MINIO_STORAGE_MEDIA_BUCKET_NAME = bucket/корзина или грубо говоря директория в minio сервере куда будут
# загружаться медиафайлы \\\ example 'local-media'
# MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True \\\ Доступ для создания новой корзины/bucket если указанного
# MINIO_STORAGE_MEDIA_BUCKET_NAME не существует.
# MINIO_STORAGE_STATIC_BUCKET_NAME = 'local-static' \\\ аналогично 10 строке, только для статикфайлов
# MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True \\\ аналогично 12 строке

# Остаются также
# MINIO_STORAGE_MEDIA_LOCATION = 'media'
# MINIO_STORAGE_STATIC_LOCATION = 'static'

# Url путь до медиа/статик файлов вместе с корзиной
# MINIO_STORAGE_MEDIA_URL = f'http://{"192.168.0.102:9000"}/local-media'
# MINIO_STORAGE_STATIC_URL = f'http://{"192.168.0.102:9000"}/local-static'
