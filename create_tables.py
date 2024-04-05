from app.core.database import Database


if __name__ == "__main__":
    import asyncio
    
    database: Database = Database()
    asyncio.run(database.create_tables())
    