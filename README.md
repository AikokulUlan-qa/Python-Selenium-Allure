# Python-Selenium-Allure
## Автоматизированные тесты сайта
<p align="center">
  <img src="https://i.ytimg.com/vi/DeskeR8W_c4/maxresdefault.jpg" alt="Sublime's custom image"/>
</p>

![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Python+Selenium+Allure)

  ### ☞ Программы, которые следует установить: 
### - Настраиваем Visual Code 
### - Allure Report - установка для разных операционных систем разная
  #### Для MacOS выполнить команды:
```
brew install allure
```
  #### Для Linux (на базе Debian)
```
sudo apt-add-repository ppa:qameta/allure
sudo apt-get update
sudo apt-get install allure
```
  ####  Для Windows. Скачиваем [архив по ссылке](https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.19.0/allure-commandline-2.19.0.zip) и кладем **распакованный** каталог рядом с нашим проектом. Запуск allure прост: 
  #### - В Windows находим в каталоге *allure\bin* файл *allure.bat* и запускаем на выполнение
  #### - На Linux/Mac выполняем файл рядом *./allure*
  #### При возникновении ошибок, необходимо установить Java.
### **Selenium -** он многообразен и может использоваться в виде:
- Selenium WebDriver - фреймворк для программного взаимодействия с браузером
- Selenium IDE - расширение в браузере. Очень похоже на Cypress. Можно [поиграться](https://www.selenium.dev/selenium-ide/) на досуге
- Selenium Grid - кластер, включающий в себя несколько Selenium-серверов. Позволяет организовать распределённую сеть, позволяющую параллельно запускать много браузеров на разных машинах.
  
### Модули, которые необходимо установить:
```
pip install pytest
pip install selenium
pip install allure-pytest
```
### Для создания автотеста
#### - прописываем шаги на Python на установку модулей
#### - описываем опции запуска браузера
#### - устанавливаем webdriver в соответствии с версией используемого браузера
#### - определяем адрес страницы для теста и переходим на неё
#### - ищем по селектору элемент меню "ххх" и кликаем по нему
#### - ищем по селектору карточку "хy" и кликаем по нему, чтобы просмотреть детали
#### - ищем по имени класса артикул для "xy"
#### - проверяем соответствие
### Запускаем проверку
<img width="191" alt="Снимок экрана 2024-02-12 в 19 45 05" src="https://github.com/AikokulUlan-qa/Python-Selenium-Allure-/assets/154068607/cb5cd923-54e1-4d08-8b50-556c4fa92873">



  
### ☑︎Скачиваем файл-установщик с официального сайта https://www.python.org/downloads/

### ☞Затем настраиваем Visual Code
### ☞Нужно перейти в Extensions (Расширения), ввести Python и нажать Install.
### ☑︎Далее создать на компьютере папку, где будет хранится твой проект. Это можно сделать в Vs Code в проводнике, там же создать файл.
  ###   Теперь Python установлен на ваш компьютер, пора приступить к конкретному написанию первого кода.
###  - Для установки любых библиотек нужно открыть терминал VS Code и выполнить команду pip install название_библиотеки 
 ####   ☑︎ requests
