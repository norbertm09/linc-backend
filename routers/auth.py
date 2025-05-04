from fastapi import APIRouter
router = APIRouter(prefix='/auth')

@router.get('/register')
def register():
    return {'endpoint': 'auth/register', 'status': 'simulated'}

@router.get('/login')
def login():
    return {'endpoint': 'auth/login', 'status': 'simulated'}

@router.get('/verify-otp')
def verify-otp():
    return {'endpoint': 'auth/verify-otp', 'status': 'simulated'}

@router.get('/logout')
def logout():
    return {'endpoint': 'auth/logout', 'status': 'simulated'}