TORTOISE_ORM = {
    "connections": {
         "default": "postgres://postgres:postgres@localhost:5433/cats"
    },
    "apps": {
        "code": {
            "models": [
                 "code.models", "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}