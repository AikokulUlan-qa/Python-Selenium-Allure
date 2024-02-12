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
### Прогоняем тесты
<img width="191" alt="Снимок экрана 2024-02-12 в 19 45 05" src="https://github.com/AikokulUlan-qa/Python-Selenium-Allure-/assets/154068607/cb5cd923-54e1-4d08-8b50-556c4fa92873">
#### Тесты с меткой ```@pytest.mark.xfail(reason="Wait for fix bug")``` означают, что они заведомо упадут. Однако независимо от нее, тесты пройдут проверку.
### После прогонов тестов следует запустить сервер отчетов командой:
```
cd <путь до каталог allure\bin> (первая команда)
.\allure.bat (вторая)
.\allure serve <путь до каталога с результатами> (третья)
```

#### Для MacOS (если установил allure через brew)
```
allure serve /Users/gdolnikov/projects/selenium.qa.studio/my_allure_results
```
#### my_allure_results — это ты сам создаешь или выбираешь в какую папку смотреть allure-у для создания красивого дашборда

### Итогом выполнения последней команды будет запуск и открытие в браузере страницы с отчетами
<p align="center">
  <img src="https://assets-global.website-files.com/610bfc91018da0bc815264aa/6203c5b616ae640ffd351bb3_5b3LRXxIjWi43mVQNkGhtmzHJVDjnLnQv95f89rBnL8HM01gB7xCKxjuHLlgkofFq98p-oqxGxKeLgRxcTnqB24MEoybxiNd_VCKRgIcgQRF4vMDZhtzqlc0JguqSI6-2IxsBGOz.png"/>
</p>

  

