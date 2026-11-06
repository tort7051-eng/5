import colorama
from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.GREEN + "Назва бібліотеки:", colorama.__name__)

print(Fore.RED + "Червоний текст")
print(Fore.GREEN + "Зелений текст")
print(Fore.BLUE + "Синій текст")

print(Back.YELLOW + "Текст із жовтим фоном")
print(Style.BRIGHT + "Яскравий текст")
