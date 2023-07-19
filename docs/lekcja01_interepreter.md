
Lekcja 1.:

1.1 O pythonie
Python, język ogólnego przeznaczenia o rozbudowanaymm systemie
bibliotek, jego ideą jest czytelność kodu
właśnie wyróżnia się tym że formatowanie kodu jest 
częścią składni

Python wspiera różne paradygmaty programowania,
obiektory, impoeratywny, funkcyjny
ma dynamiczny system typów oraz zarzącdzanie pamięcią

Jest językiem skryptowym więc posiada interpreter, nie kompiluje się
kompiluje się do kodu pośredniego który jest wykonywany przez interpreter
Interpretery pythona są dostępne na wiele systemów operacyjnych

https://pl.wikipedia.org/wiki/Python

Python jest językiem opensource więc mamy wgląd do kodu źródłowego języka
zarządzany przez Python Software Foundation,
Standardową implementacją języka jest CPython (napisany w C), ale istnieją też inne, np. Jython (napisany w Javie), CLPython napisany w Common Lisp, IronPython (na platformę .NET) 

Głównym Twórcą języka jest Guido van Rossum, zapaczątkował go w latach 90tych
Język można pobrać tu : https://github.com/python/cpython


Pobierz pythona,
install
uruchom go
uruchom python3 / python w terminalu


1.2 Pokaż interpreter jak go się uruchamia

2. Czym jest range?



# Interpreter
1. Python sprawdza czy składnia jest poprawna, analiza lexograficzna, interpreter idzie do fazy II
czyli generacji Byte-codeu
https://godbolt.org/

Interpreter generuje AST Abstract Syntax tree i zapisuje w pliku pyc

do disassemble służy import dis.dis(funkcja)

2. Interpreter inicjalizuje PVM, python virtual machine - konwertuje bajtkon na kod binarny