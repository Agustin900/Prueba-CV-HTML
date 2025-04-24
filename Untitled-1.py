import random
import time
from mcrcon import MCRcon

# Configuración del servidor
HOST = "192.168.194.1"
PORT = 25575
PASSWORD = "Agustin12!"

# Función: simula pasos acercándose
def pasos_acercandose(mcr):
    offsets = [3, 1.5, 0]
    for x in offsets:
        cmd = f'/execute as @r at @s run playsound minecraft:block.gravel.step master @s ~{x} ~ ~ 10 1'
        mcr.command(cmd)
        time.sleep(0.4)

# Función: simula bloques rompiéndose acercándose
def bloques_rompiendose_acercandose(mcr):
    offsets = [2, 1, 0]
    for x in offsets:
        cmd = f'/execute as @r at @s run playsound minecraft:block.stone.break master @s ~{x} ~ ~ 10 1'
        mcr.command(cmd)
        time.sleep(0.5)

# Función: rodear al jugador con pasos
def pasos_alrededor(mcr):
    posiciones = [
        '~2 ~ ~',     # frente
        '~-2 ~ ~',    # atrás
        '~ ~ ~2',     # derecha
        '~ ~ ~-2',    # izquierda
        '~1 ~ ~1',    # diagonal
        '~-1 ~ ~-1'   # diagonal opuesta
    ]
    for pos in posiciones:
        cmd = f'/execute as @r at @s run playsound minecraft:block.gravel.step master @s {pos} 10 1'
        mcr.command(cmd)
        time.sleep(0.3)

# Lista de comandos troll individuales
comandos_troll = [
    '/execute as @r at @s run playsound minecraft:entity.creeper.primed master @s ~ ~ ~ 10 1',
    '/execute as @r at @s run playsound minecraft:block.gravel.step master @s ~ ~ ~ 10 1',
    '/execute as @r at @s run playsound minecraft:block.stone.break master @s ~ ~ ~ 10 1',
    '/execute as @r at @s run playsound minecraft:entity.witch.celebrate master @s ~ ~ ~ 10 1',
    '/execute as @r at @s run playsound minecraft:entity.warden.listening master @s ~ ~ ~ 10 1',
    '/execute as @r at @s run playsound minecraft:entity.warden.step master @s ~ ~ ~ 10 1',
    '/execute as @r at @s run summon minecraft:lightning_bolt',
    '/execute as @r at @s run summon minecraft:bee ~ ~ ~ {NoAI:1b}',
    '/execute as @r at @s run playsound minecraft:entity.enderman.scream master @s ~ ~ ~ 10 0'
]

# Categorías de efectos
acciones = ['comando', 'pasos_acercandose', 'bloques_acercandose', 'pasos_alrededor']

# Bucle principal
try:
    with MCRcon(HOST, PASSWORD, port=PORT) as mcr:

        while True:
            accion = random.choice(acciones)

            if accion == 'comando':
                comando = random.choice(comandos_troll)
                mcr.command(comando)
                print(f"[TROLL] Ejecutado: {comando}")

            elif accion == 'pasos_acercandose':
                print("[TROLL] Pasos acercándose...")
                pasos_acercandose(mcr)

            elif accion == 'bloques_acercandose':
                print("[TROLL] Bloques rompiéndose cerca...")
                bloques_rompiendose_acercandose(mcr)

            elif accion == 'pasos_alrededor':
                print("[TROLL] Pasos alrededor del jugador...")
                pasos_alrededor(mcr)

            # Espera aleatoria entre efectos
            time.sleep(random.randint(30, 60))

except Exception as e:
    print(f"[ERROR] No se pudo conectar o ejecutar el comando: {e}")
