import io
from typing import Annotated
from config import config
from fastapi import UploadFile, File
from minio import Minio

from repository.minio_repository import MinioRepository


class MinioService:
    def __init__(self, repository: MinioRepository):
        self.repository = repository

    async def upload_resume(self, resume: Annotated[UploadFile, File()], user_id: int):
        bucket_name = config['bucket_resumes']
        destination_file = f'{user_id}/{resume.filename}'

        # Garante que o bucket existe
        if not self.repository.client.bucket_exists(bucket_name):
            self.repository.client.make_bucket(bucket_name)

        # Lê o conteúdo do arquivo enviado
        contents = await resume.read()

        binary_stream = io.BytesIO(contents)

        self.repository.save_resume(binary_stream, bucket_name, destination_file, contents, resume)
