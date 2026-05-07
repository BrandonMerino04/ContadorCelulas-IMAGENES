def contar(stats):
    conteo = 0

    for i in range(1, len(stats)):
        x, y, w, h, area = stats[i]

        if 100 < area < 5000:
            conteo += 1

    return conteo