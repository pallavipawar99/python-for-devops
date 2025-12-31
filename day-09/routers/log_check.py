from fastapi import APIRouter, HTTPException
from services.log_check_service import *

router = APIRouter()

@router.get("/logs_check",status_code=200)
def get_logs():

    try:
        data = check_log()
        return {"message":data}
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )