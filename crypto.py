from fastapi import APIRouter
router = APIRouter(prefix='/crypto')

@router.get('/sell')
def sell():
    return {'endpoint': 'crypto/sell', 'status': 'simulated'}

@router.get('/wallet')
def wallet():
    return {'endpoint': 'crypto/wallet', 'status': 'simulated'}

@router.get('/history')
def history():
    return {'endpoint': 'crypto/history', 'status': 'simulated'}

@router.get('/rates')
def rates():
    return {'endpoint': 'crypto/rates', 'status': 'simulated'}