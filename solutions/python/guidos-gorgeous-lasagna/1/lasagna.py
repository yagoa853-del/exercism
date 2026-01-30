# Tempo total esperado de forno em minutos
EXPECTED_BAKE_TIME = 40

# Tempo necessário para preparar uma camada em minutos
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """
    Calcula quantos minutos de forno ainda restam.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """
    Calcula o tempo total de preparo com base no número de camadas.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """
    Calcula o tempo total decorrido do preparo.
    Isso inclui o tempo de preparo e o tempo já passado no forno.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
