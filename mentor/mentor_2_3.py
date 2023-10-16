# записати імена в список і посортувати по довжині

def sort():
    imena = []
    # imena_dovjyna = {}
    for i in range(5):
        imena.append(input('Enter names: '))
    # for name in imena:
    #     dovjyna = len(name)
    #     imena_dovjyna.update({name : dovjyna})
    imena.sort(key=len)
    return imena

print(sort())
