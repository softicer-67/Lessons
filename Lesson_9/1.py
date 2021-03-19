'''
Сорри, понимаю что можно сделать просто через таймер в цикле,
будет намного меньше кода,
но хочется прикольнее ))
'''
import time
from colorama import Fore, Style


def timer(count):
    while count != 0:
        print(count, end=' ')
        count -= 1
        time.sleep(1)
    print(count)


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print(f'{Fore.RED} {TrafficLight.__color[0]} {Style.RESET_ALL}')
        timer(7)

        print(f'{Fore.YELLOW} {TrafficLight.__color[1]} {Style.RESET_ALL}')
        timer(2)

        print(f'{Fore.GREEN} {TrafficLight.__color[2]} {Style.RESET_ALL}')
        timer(5)


TrafficLight = TrafficLight()
TrafficLight.running()
