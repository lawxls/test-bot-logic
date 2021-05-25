### Интерфейс библиотек с абстрактными методами для Logic Executor
#### Объекты nn, nlu, nv 

Используется в python-language-server как внешняя библиотека, установленная в текущий env через pip

Установка pip пакета:

    python3 setup.py install

или

    pip3 install libneuro-interface-master.tar.gz

Скачать архив libneuro-interface-master.tar.gz можно из gitlab:

https://git.neuro.net/neurov2/libneuro-interface/-/archive/master/libneuro-interface-master.tar.gz 


Пример использования в скрипте логики:

    
    if __name__ == '__main__':
        import libneuro

        nn = libneuro.NeuroNetLibrary()
        nlu = libneuro.NeuroNluLibrary()
        nv = libneuro.NeuroVoiceLibrary()
        InvalidCallStateError = libneuro.InvalidCallStateError
        check_call_state = libneuro.check_call_state
    
    def main():
        nn.call(nn.dialog['msisdn'], '2020-05-20 14:20:00', entry_point='main_online)

    def main_online():
        pass