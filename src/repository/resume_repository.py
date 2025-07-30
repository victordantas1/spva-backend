from io import BytesIO

from fastapi import UploadFile
from minio import Minio


class ResumeRepository:

    def __init__(self, client: Minio):
        self.client = client

    def save_resume(self, binary_stream: BytesIO, bucket_name: str, destination_file: str, contents, resume: UploadFile):
        self.client.put_object(
            bucket_name=bucket_name,
            object_name=destination_file,
            data=binary_stream,
            length=len(contents),
            content_type=resume.content_type
        )
