from fastapi import APIRouter
router = APIRouter(prefix='/scoring')

@router.get('/evaluate')
def evaluate():
    return {'endpoint': 'scoring/evaluate', 'status': 'simulated'}

@router.get('/profile')
def profile():
    return {'endpoint': 'scoring/profile', 'status': 'simulated'}

@router.get('/alerts')
def alerts():
    return {'endpoint': 'scoring/alerts', 'status': 'simulated'}

@router.get('/update_rules')
def update_rules():
    return {'endpoint': 'scoring/update_rules', 'status': 'simulated'}