import tracemalloc

tracemalloc.start()


def create_list():
    return [i for i in range(100000)]


data = create_list()

snapshot = tracemalloc.take_snapshot()

top_stats = snapshot.statistics("lineno")

for stat in top_stats[:10]:
    print(stat)