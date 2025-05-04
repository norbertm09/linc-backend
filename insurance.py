from fastapi import APIRouter
router = APIRouter(prefix='/insurance')

@router.get('/simulate')
def simulate():
    return {'endpoint': 'insurance/simulate', 'status': 'simulated'}

@router.get('/subscribe')
def subscribe():
    return {'endpoint': 'insurance/subscribe', 'status': 'simulated'}

@router.get('/certificate')
def certificate():
    return {'endpoint': 'insurance/certificate', 'status': 'simulated'}

@router.get('/types')
def types():
    return {'endpoint': 'insurance/types', 'status': 'simulated'}