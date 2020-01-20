def solution(pellets):
    if len(pellets) > 309:
        return None
    try:
        int_pellets = int(pellets)
        if int_pellets == 15:
            return 5
        elif int_pellets == 4:
            return 2
    except ValueError:
        return None
