def verificar_presao(nivel_atual):
    """
      Verifica se a pressão da caldeira está dentro do limite de segurança.
      :param _________: float - O valor lido pelo sensor.
      :return: _________ - Retorna True se segura, False se perigosa.
      """
    if 10 <= nivel_atual <= 50:
        return True
    else:
        return False

sensor_pressao = 65

if not verificar_presao(sensor_pressao):
    print("🚨 ALERTA: Pressão fora dos limites!")
