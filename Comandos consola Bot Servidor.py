import random
import time
from mcrcon import MCRcon

# Configuración del servidor
HOST = "192.168.194.1"
PORT = 25575
PASSWORD = "Agustin12!"

# Función: simula pasos acercándose
def pasos_acercandose(mcr):
    offsets = [3, 2.5, 2, 1.5, 1, 0.5, 0]
    for x in offsets:
        cmd_sonido = f'/execute as @r at @s run playsound minecraft:block.gravel.step master @s ~{x} ~ ~ 10 1'
        cmd_particula = f'/execute as @r at @s run particle minecraft:block minecraft:gravel ~{x} ~ ~ 0.3 0.3 0.3 0.01 5 force'
        mcr.command(cmd_sonido)
        mcr.command(cmd_particula)
        time.sleep(0.4)

# Función: simula bloques rompiéndose acercándose
def bloques_rompiendose_acercandose(mcr):
    offsets = [4, 3, 2.5, 2, 1.5, 1, 0.5, 0]
    for x in offsets:
        cmd_sonido = f'/execute as @r at @s run playsound minecraft:block.stone.break master @s ~{x} ~ ~ 10 1'
        cmd_particula = f'/execute as @r at @s run particle minecraft:block minecraft:stone ~{x} ~ ~ 0.3 0.3 0.3 0.01 5 force'
        mcr.command(cmd_sonido)
        mcr.command(cmd_particula)
        time.sleep(0.3)

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

# Función: efectos sensoriales y psicológicos tétricos
def efectos_terror_psicologico(mcr):
    efectos = [
        # Sonidos extraños
        '/execute as @r at @s run playsound minecraft:entity.illusioner.mirror_move master @s ~ ~ ~ 5 0.8',
        '/execute as @r at @s run playsound minecraft:entity.witch.ambient master @s ~ ~ ~ 4 0.6',
        '/execute as @r at @s run playsound minecraft:entity.villager.no master @s ~ ~ ~ 3 0.5',

        # Partículas raras
        '/execute as @r at @s run particle minecraft:soul ~ ~1 ~ 0.5 0.5 0.5 0 15 force',
        '/execute as @r at @s run particle minecraft:ash ~ ~1 ~ 0.3 0.3 0.3 0.01 10 force',
        '/execute as @r at @s run particle minecraft:dripping_obsidian_tear ~ ~1 ~ 0.3 0.5 0.3 0 20 force',

        # Efectos breves
        '/effect give @r minecraft:blindness 3 0 true',
        '/effect give @r minecraft:nausea 5 0 true',
        '/effect give @r minecraft:slowness 4 1 true',

        # Mensajes tétricos
        '/tellraw @r {"text":"¿Estás solo realmente?","color":"dark_red","italic":true}',
        '/tellraw @r {"text":"Te están mirando.","color":"gray","italic":true}',
    ]

    # Cambio sutil de dirección de cámara
    yaw = random.randint(-180, 180)
    pitch = random.randint(-20, 20)
    mcr.command(f'/execute as @r at @s run tp @s ~ ~ ~ {yaw} {pitch}')

    # Elegir aleatoriamente 2 efectos
    seleccionados = random.sample(efectos, 2)
    for efecto in seleccionados:
        mcr.command(efecto)
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
    '/execute as @r at @s run summon minecraft:zombie ~ ~ ~',
    '/execute as @r at @s run playsound minecraft:entity.enderman.death master @s ~ ~ ~ 10 0',
    '/execute as @r at @s run playsound minecraft:entity.warden.emerge master @a ~ ~ ~ 10 0'
]

# Categorías de efectos
acciones = [
    'comando',
    'pasos_acercandose',
    'bloques_acercandose',
    'pasos_alrededor',
    'efectos_terror'
]

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

            elif accion == 'efectos_terror':
                print("[TROLL] Efectos psicológicos y sensoriales...")
                efectos_terror_psicologico(mcr)

            # Espera aleatoria entre efectos
            time.sleep(random.randint(30, 180))

except Exception as e:
    print(f"[ERROR] No se pudo conectar o ejecutar el comando: {e}")