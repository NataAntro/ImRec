## Привет, это Ната и моё приложение ImRec! <img src="https://media.giphy.com/media/hvRJCLFzcasrR4ia7z/giphy.gif" width="28px" height="28px">

<p>
<i>Выполнено в рамках проекта курса "Программная инженерия". </i>
<p>
<b>Приложение для распознавания изображений в облаке,</b> которое может классифицировать и комментировать изображения на основе загруженных файлов.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://nataantro-test-streamlit-app-b8fuko.streamlit.app/)
<p>
<img src = 'https://github.com/MarikIshtar007/MarikIshtar007/blob/master/images/matrix.gif' alt = 'Awesome Matrix Code' align='right'/>	
<p>
	
## Как это работает?
<p>

* Пользователь загружает изображение через интерфейс приложения.<br>
	
* Изображение предобрабатывается: изменяется его размер до необходимого для модели, изображение нормализуется, и добавляется дополнительная размерность для обработки в батче.<br>

* Предобработанное изображение подается на вход модели EfficientNetB0.<br>

* Модель производит предсказание, которое представляет собой вероятности того, что изображение относится к каждой из 1000 категорий.<br>

* Предсказания модели передаются в OpenAI в форматированном виде.<br>

* OpenAI генерирует текстовое описание изображения, которое затем выводится в пользовательский интерфейс.
<p>
	
## Технологии:
<p>
	
* Предварительно обученная нейронная модель <a href="https://keras.io/api/applications/efficientnet/" target="_blank">EfficientNetB0</a> для распознавания объектов на изображениях.<br>

* Библиотека Streamlit для создания веб-интерфейса приложения.<br> 

* Библиотека TensorFlow для работы с моделью глубокого обучения.<br>

* OpenAI API для генерации текстового описания классифицированного изображения на основе его предсказаний.
<p>


 [![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Efficient+Net+B0)](https://git.io/typing-svg)
 
 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

 ```python
 class WhoAmI:
    user = 'NataAntro'
    current_adventure = ('URFU Student', 'AI/ML Engineer', 'QA Specialist (Extyl-pro.ru)', 
			 'Metaverse Researcher', 'Digital artist')
    passions = [
        'Music',
        'Snowboarding',
        'Reading Pelevins books',
        'Gathering many good ideas into one great idea'
    ]

    @independent_method
    def home_base():
        return 'Moscow_Russia'

    @independent_method
    def on_agenda():
        return ['LearnAIandML', 'CreateStartUp', 'LiveinHappiness']
        # Assume 10 more awesome ambitions here  ;)

	
 ```

