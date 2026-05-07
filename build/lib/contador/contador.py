def contar(contador):
    conteo = 0

    for i in range(1, len(contador)):
        x, y, w, h, area = contador[i]

        if 100 < area < 5000:
            conteo = conteo + 1

    return conteo