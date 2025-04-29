from fastapi import Depends
from minio import Minio
from config import config
from repository import MinioRepository
from services import MinioService


def get_minio_client() -> Minio:
    client = Minio(
        config['minio_endpoint'],
        access_key=config['minio_access_key'],
        secret_key=config['minio_secret_key'],
        secure=False
    )
    return client

def get_minio_repository(client: Minio = Depends(get_minio_client)) -> MinioRepository:
    return MinioRepository(client)

def get_minio_service(repository: MinioRepository = Depends(get_minio_repository)) -> MinioService:
    return MinioService(repository)
