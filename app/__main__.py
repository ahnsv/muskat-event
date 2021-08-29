from app.infrastructure.dependencies.container import Container


if __name__ == "__main__":
    import uvicorn
    from app.infrastructure.presentation.fastapi import router, app

    container = Container()
    container.wire([router])
    uvicorn.run(app.app, host="0.0.0.0")
