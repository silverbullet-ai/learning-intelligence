import gc

print("GC Enabled:", gc.isenabled())

collected = gc.collect()

print("Objects Collected:", collected)

print(gc.get_stats())