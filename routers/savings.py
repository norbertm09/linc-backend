from fastapi import APIRouter
router = APIRouter(prefix='/savings')

@router.get('/create')
def create():
    return {'endpoint': 'savings/create', 'status': 'simulated'}

@router.get('/plans')
def plans():
    return {'endpoint': 'savings/plans', 'status': 'simulated'}

@router.get('/history')
def history():
    return {'endpoint': 'savings/history', 'status': 'simulated'}

@router.get('/auto-debit')
def auto-debit():
    return {'endpoint': 'savings/auto-debit', 'status': 'simulated'}