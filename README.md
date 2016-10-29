<h1 align="center">Python3</h1>

+ [Простейший TCP echo сервер](#simple_TCP_echo_server)
+ [Скриншоты](#screenshot)


**Программирование на Python - Bioinformatics Institute(Stepic 67)**


+ [3.4 Файловый ввод/вывод](https://github.com/LLlKuIIeP/Python3/tree/master/stepic-67/module_3/lesson_4)

___

<a name="simple_TCP_echo_server"></a>
### Простейший TCP echo сервер

Запускается на __IP__ адресе __0.0.0.0__ и __TCP__ порту __2222__. Получает сообщения длинной не более __1024__ байт и отправляет обратно клиенту. Закрывает соединение при получении сообщения с текстом __close__.
</br>Файл [simple_tcp_echo_server_1.py](simple_tcp_echo_server_1.py)

Измените ваш __echo сервер__ так, что бы он работать одновременно с 10 клиентами.
</br>Файл [simple_tcp_echo_server_2.py](simple_tcp_echo_server_2.py)

</br></br></br>
<a name="screenshot"></a>
### Скриншоты
```
apt-get install python3-pip
apt-get install python3-tk
apt-get install scrot
pip3 install python3_xlib
pip3 install pyautogui
```
[Сайт библиотеки](http://pyautogui.readthedocs.io/en/latest/screenshot.html)

```
import pyautogui
pyautogui.screenshot('my_screenshot.png')
```

