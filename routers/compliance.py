from fastapi import APIRouter
router = APIRouter(prefix='/compliance')

@router.get('/screen')
def screen():
    return {'endpoint': 'compliance/screen', 'status': 'simulated'}