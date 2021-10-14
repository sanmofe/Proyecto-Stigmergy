from ..models import Usuario

def get_all_usuarios():
    users = Usuario.objects.all()
    return users

def get_usuario(identificador: int):
    user = Usuario.objects.filter(pk= identificador)
    return user

def delete_usuario(identificador: int):
    usuarioDel= get_usuario(identificador)
    usuarioDel.delete()
    return usuarioDel