if __name__ == "__main__":
    import uvicorn
    from app.infrastructure.presentation.fastapi.app import app

    uvicorn.run(app, host="0.0.0.0")
