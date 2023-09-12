from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "cat" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "name" VARCHAR(120) NOT NULL,
    "color" VARCHAR(120) NOT NULL,
    "image" VARCHAR(120) NOT NULL,
    "created_at" DATE NOT NULL
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSONB NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
