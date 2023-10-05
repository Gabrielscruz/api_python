from fastapi  import FastAPI
from tortoise import Tortoise, fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator

app = FastAPI()

class Usuario(Model):
    cod_usuario = fields.IntField(pk=True)
    cod_controle = fields.IntField()
    nome = fields.CharField(200)
    email = fields.CharField(200, unique=True)
    senha = fields.CharField(100)
    h_credor_hk = fields.JSONField()
    flg_requer_admin = fields.BooleanField(default=False)
    flg_requer_superadmin = fields.BooleanField(default=False)

Usuario_Pydantic = pydantic_model_creator(Usuario, name='usuario')
UsuarioEm_Pydantic = pydantic_model_creator(Usuario, name='usuarioEm', exclude_readonly=True)

@app.get("/")
def root():
    return {"text": "Hello World"}

@app.get("/v1/contatos")
async def fetch_users():

    connection = Tortoise.get_connection("default")
    result = await connection.execute_query(query)
    print(result)
    return result


def init_orm():
    Tortoise.init(config={

    "apps": {
        "models": {
            "models": ["server"],
            "default_connection": "default",
        },
    },
})
    Tortoise.generate_schemas()

    return Tortoise