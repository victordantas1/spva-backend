from typing import List, Optional, cast

from sqlalchemy.orm import Session

import src.schemas as schemas
from src.model import UserJob


class UserJobRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_jobs(self) -> List[UserJob]:
        user_jobs = cast(List[UserJob], self.session.query(UserJob).all())
        return list(user_jobs)

    def get_user_job_by_id(self, user_id: int, job_id: int) -> Optional[UserJob]:
        return self.session.get(UserJob, (user_id, job_id))

    def save_user_job(self, user_job: UserJob) -> UserJob:
        try:
            self.session.add(user_job)
            self.session.commit()
            return user_job
        except:
            self.session.rollback()
            raise

    def delete_user_job_by_id(self, user_id: int, job_id: int) -> Optional[UserJob]:
        try:
            user_job = self.get_user_job_by_id(user_id, job_id)
            self.session.delete(user_job)
            self.session.commit()
            return user_job
        except:
            self.session.rollback()
            raise

    def update_user_job_by_id(self, user_id: int, job_id: int, user_job: schemas.UserJob) -> UserJob:
        try:
            user_job_to_update = self.get_user_job_by_id(user_id, job_id)
            user_job_to_update.update_user_job(user_job)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        return user_job_to_update