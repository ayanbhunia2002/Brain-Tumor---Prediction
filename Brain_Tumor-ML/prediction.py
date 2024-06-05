from fastapi import File, HTTPException
import numpy as np
import pickle
import tensorflow as tf
import input_preprocess

def get_CNN_model():
    # Load the Keras model without compiling
    cnn_model = tf.keras.models.load_model('brain_tumor1_CNN.h5', compile=False)
    # Manually compile the model
    cnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return cnn_model

def get_SVM_model():
    with open('brain_tumor1_SVM.pkl', 'rb') as file:
        svm_model = pickle.load(file)
    return svm_model

def get_KNN_model():
    with open('brain_tumor1_KNN.pkl', 'rb') as file:
        knn_model = pickle.load(file)
    return knn_model

def pred_from_SVM(file_content):
    try:
        processed_image = input_preprocess.preprocess_image_2(file_content)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    model = get_SVM_model()
    return model.predict(np.expand_dims(processed_image, axis=0))


def pred_from_CNN(file_content):
    try:
        processed_image = input_preprocess.preprocess_image_1(file_content)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    model = get_CNN_model()
    return model.predict(np.array([processed_image]))


def pred_from_KNN(file_content):
    try:
        processed_image = input_preprocess.preprocess_image_2(file_content)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    model = get_KNN_model()
    return model.predict(np.expand_dims(processed_image, axis=0))


def get_prediction(file_content):
    SVM_predict_value = pred_from_SVM(file_content)
    print(SVM_predict_value[0])
    print("###############################")
    KNN_predict_value = pred_from_KNN(file_content)
    print(KNN_predict_value[0])
    print("###############################")
    CNN_predict_value = pred_from_CNN(file_content)
    print(CNN_predict_value[0][0])
    print("###############################")
    
    SVM_predict = SVM_predict_value[0] != 0
    KNN_predict = KNN_predict_value[0] != 0
    CNN_predict = CNN_predict_value[0][0] > 0.5

    print(SVM_predict, KNN_predict, CNN_predict)

    predictions = [SVM_predict, KNN_predict, CNN_predict]
    ans = max(set(predictions), key=predictions.count)
    print(ans)

    return ans