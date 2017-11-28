#III sposob importowania modułów:
# * - wszystkie leementy w module beda zaimporotwane,
# dalej w kodzie podaje tylko nazwy funkcji z  modulu (bez calej sciezki)
# sa dwa ale:
#dalej mam wszystko zaimportowane
#po drugie jesli w taki sam sposob bym importowala innny modul i bylyby tam takie same nazwy,
#  to bylby konflki
#przy kazdym imporcie caly kod, ktory jest w module - caly kod zostanie wywolany
import shutil

from dzien7.moj_modul.odwracanie_stringa import *

odwrocny = odwroc_string("ola")

print(odwrocny)