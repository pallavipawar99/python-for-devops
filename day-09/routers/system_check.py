from fastapi import APIRouter, HTTPException
from services.system_check_service import *
from services.log_check_service import *

router = APIRouter()

@router.get("/system_health",status_code=200)
def get_instances():

    try:
        data = get_system_info()
        return {"message":data}
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
    

