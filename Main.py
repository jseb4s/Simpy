import simpy
import pandas as pd




# Salida a excel

import simpy
import pandas as pd

def cliente(env, cliente_id, cajeros, registro):
    registro.append([cliente_id, 'Llegada', env.now, None])
    
    with cajeros.request() as req:
        yield req
        cajero_idx = cajeros.users.index(req)
        tiempo_atencion = cajero_tiempos[cajero_idx]  # Tiempo de atención específico del cajero
        registro.append([cliente_id, 'Comienzo de atención', env.now, cajero_idx])
        # Simulamos que el cajero atiende al cliente durante el tiempo específico
        yield env.timeout(tiempo_atencion)
        registro.append([cliente_id, 'Fin de atención', env.now, cajero_idx])

env = simpy.Environment()
cajeros = simpy.Resource(env, capacity=2)  # Solo 2 cajeros disponibles
cajero_tiempos = [5, 10]  # Tiempos de atención para cada cajero
registro = []

for i in range(8):
    env.process(cliente(env, f'Cliente {i}', cajeros, registro))

env.run()

# Crear un DataFrame a partir del registro
df = pd.DataFrame(registro, columns=['Cliente ID', 'Evento', 'Tiempo', 'Cajero'])

# Exportar el DataFrame a un archivo Excel
df.to_excel('registro_simulacion.xlsx', index=False)


import simpy
import pandas as pd

"""
def cliente(env, cliente_id, cajeros, registro):
    registro.append([cliente_id, 'Llegada', env.now, None])
    
    with cajeros.request() as req:
        yield req
        cajero_idx = cajeros.users.index(req)
        tiempo_atencion = cajero_tiempos[cajero_idx]  # Tiempo de atención específico del cajero
        registro.append([cliente_id, 'Comienzo de atención', env.now, cajero_idx])
        # Simulamos que el cajero atiende al cliente durante el tiempo específico
        yield env.timeout(tiempo_atencion)
        registro.append([cliente_id, 'Fin de atención', env.now, cajero_idx])

env = simpy.Environment()
cajeros = simpy.Resource(env, capacity=2)  # Solo 2 cajeros disponibles
cajero_tiempos = [5, 10]  # Tiempos de atención para cada cajero
registro = []

def generar_clientes(env, cajeros, registro):
    for i in range(8):
        yield env.timeout(1)  # Genera un nuevo cliente cada 1 unidad de tiempo
        env.process(cliente(env, f'Cliente {i}', cajeros, registro))

env.process(generar_clientes(env, cajeros, registro))

env.run(until=20)  # Simula hasta el tiempo 20

# Crear un DataFrame a partir del registro
df = pd.DataFrame(registro, columns=['Cliente ID', 'Evento', 'Tiempo', 'Cajero'])

# Exportar el DataFrame a un archivo Excel
df.to_excel('registro_simulacion.xlsx', index=False)
"""