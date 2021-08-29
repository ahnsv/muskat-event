from fastapi import APIRouter

router = APIRouter(prefix="/orders")


@router.post("/")
def create_order():
    pass


@router.get("/")
def get_order():
    pass


@router.delete("/{order_id}")
def cancel_order():
    pass


@router.patch("/{order_id}")
def update_order():
    pass
