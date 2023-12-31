import numpy as np
from PIL import Image
from tensorflow.keras.applications import EfficientNetB0
from streamlit_app import load_model, preprocess_image, print_predictions


def test_load_model():
    model = load_model()
    err_msg = "Model loading failed, not instance of EfficientNetB0"
    assert isinstance(model, EfficientNetB0), err_msg


def test_preprocess_image():
    # создание тестового изображения
    data = np.random.randint(0, 256, (300, 300, 3), dtype=np.uint8)
    img = Image.fromarray(data)
    processed_image = preprocess_image(img)
    err_msg = "Preprocess image function is not working correctly"
    assert processed_image.shape == (1, 224, 224, 3), err_msg


def test_print_predictions():
    # для этого теста нам нужно проверить, работает ли функция без ошибок
    # так как мы не можем предсказать конкретный вывод функции
    predictions = np.random.rand(1, 1000)
    try:
        print_predictions(predictions)
        assert True, "Print predictions function works correctly"
    except Exception:
        assert False, "Print predictions function is not working correctly"
