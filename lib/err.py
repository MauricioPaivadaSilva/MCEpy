#
#   Inicio do código
#

class Err:
    def __init__(self) -> None:
        pass

    def ErroGenerico(self):
        return("\n      \033[1;31;40mERRO!\033[m   \n")
    
    def FuncaoNaoImplementada(self):
        return("\n      \033[1;31;40mERRO!\033[m \033[3;33mFunção não implementada\033[m   \n")
    
    def ValorInseridoIncorretamente(self):
        return("\n      \033[1;31;40mERRO!\033[m \033[0;31;40mValor inserido de forma incorreta.\033[m\n")