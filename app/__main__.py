from app.infrastructure.dependencies.container import Config, Container


if __name__ == "__main__":
    import uvicorn
    from app.infrastructure.presentation.fastapi import router, app

    container = Container()
    config = Config()
    container.config.from_pydantic(config)
    config.set_env_vars()
    container.wire([router])
    uvicorn.run(app.app, host="0.0.0.0")
