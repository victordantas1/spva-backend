import os

from dotenv import load_dotenv

load_dotenv()

config = {
    'db_url': os.environ.get('DATABASE_URL', 'localhost:3306/spva'),
    'db_username': os.environ.get('DATABASE_USER', 'user'),
    'db_password': os.environ.get('DATABASE_USER_PASSWORD', 'senha123'),
    'minio_endpoint': os.environ.get('MINIO_ENDPOINT', 'localhost:9000'),
    'minio_access_key': os.environ.get('MINIO_ACCESS_KEY', 'user'),
    'minio_secret_key': os.environ.get('MINIO_SECRET_KEY', 'senha123'),
    'bucket_resumes': os.environ.get('BUCKET_RESUMES', 'resumes'),
}

auth_config = {
    'secret_key': os.environ.get('AUTH_SECRET_KEY', 'secret'),
    'algorithm': os.environ.get('AUTH_ALGORITHM', 'HS256'),
    'access_token_expires_minutes': int(os.environ.get('AUTH_TOKEN_EXPIRATION_MINUTES', 30))
}