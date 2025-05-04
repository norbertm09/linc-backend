from fastapi import APIRouter
router = APIRouter(prefix='/admin')

@router.get('/users')
def users():
    return {'endpoint': 'admin/users', 'status': 'simulated'}

@router.get('/kyc')
def kyc():
    return {'endpoint': 'admin/kyc', 'status': 'simulated'}

@router.get('/roles')
def roles():
    return {'endpoint': 'admin/roles', 'status': 'simulated'}

@router.get('/commissions')
def commissions():
    return {'endpoint': 'admin/commissions', 'status': 'simulated'}

@router.get('/settings')
def settings():
    return {'endpoint': 'admin/settings', 'status': 'simulated'}