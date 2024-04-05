from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    AsyncEngine
)
from app.core.config import settings


class Database:
    def __init__(self):
        self.engine: AsyncEngine = create_async_engine(settings.DB_URL)

    async def get_session(self) -> AsyncSession:
        __async_session: sessionmaker = sessionmaker(
            autocommit=False,
            autoflush=False,
            expire_on_commit=False,
            class_=AsyncSession,
            bind=self.engine
        )
        
        session: AsyncSession = await __async_session()
        return session
    
    async def create_tables(self) -> None:
        import app.models.__all_models
        
        print('Criando as tabelas no banco de dados')
        async with self.engine.begin() as conn:
            await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
            await conn.run_sync(settings.DBBaseModel.metadata.create_all)
        print('Tabelas criadas com sucesso')
