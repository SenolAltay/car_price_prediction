
from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)

# Eğitilen modeli yükleyin
model = pickle.load(open("vot_reg.pkl", "rb"))

# Ana sayfa
@app.route('/')
def home():
    return render_template('index.html')

# Tahmin sayfası
@app.route('/predict', methods=['POST'])
def predict():
    # Form verilerini alın
    int_features = [int(x) for x in request.form.values()]
    # Girdileri bir DataFrame'e dönüştürün
    final_features = pd.DataFrame([int_features], columns=['seri', 'model', 'yil', 'yakit', 'vites', 'arac_durumu', 'km', 'kasa_tipi', 
                                                           'motor_gucu', 'motor_hacmi', 'agir_hasar_kayitli', 'kimden'])

    # Tahmin yapın
    prediction = model.predict(final_features)


    # Sonuçları döndürün
    return render_template('index.html', prediction_text='Araç değeri tahmini olarak: {} TL'.format(round(prediction[0])))

if __name__ == '__main__':
    app.run(debug=True)