from fastapi import APIRouter
router = APIRouter(prefix='/wallet')

@router.get('/create')
def create():
    return {'endpoint': 'wallet/create', 'status': 'simulated'}

@router.get('/balance')
def balance():
    return {'endpoint': 'wallet/balance', 'status': 'simulated'}

@router.get('/list')
def list():
    return {'endpoint': 'wallet/list', 'status': 'simulated'}

@router.get('/add-funds')
def add_funds():
    return {'endpoint': 'wallet/add-funds', 'status': 'simulated'}
