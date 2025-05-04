from fastapi import APIRouter
router = APIRouter(prefix='/auth')

@router.get('/register')
def register():
    return {'endpoint': 'auth/register', 'status': 'simulated'}

@router.get('/login')
def login():
    return {'endpoint': 'auth/login', 'status': 'simulated'}

@router.get('/verify_otp')
def verify_otp():
    return {'endpoint': 'auth/verify_otp', 'status': 'simulated'}

@router.get('/logout')
def logout():
    return {'endpoint': 'auth/logout', 'status': 'simulated'}
