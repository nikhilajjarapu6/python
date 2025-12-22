from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.wallet import Wallet
from app.schemas.wallet import WalletResponse
from app.services.wallet_service import WalletService

wallet_router=APIRouter(prefix="/wallet")
def get_service(db:Session=Depends(get_db))->WalletService:
    return WalletService(db)

@wallet_router.get("/find/{id}")
def find_by_id(id:int,service:WalletService=Depends(get_service),db:Session=Depends(get_db)):
    return service.find_wallet_by_id(id)

@wallet_router.get("/find_wallet_user/{id}")
def find_by_user_id(id:int,service:WalletService=Depends(get_service),db:Session=Depends(get_db)):
    return service.find_wallet_by_user_id(id)

@wallet_router.get("/check_balance/{id}")
def find_by_id(id:int,service:WalletService=Depends(get_service),db:Session=Depends(get_db)):
    return service.check_balance(id)