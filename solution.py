import pandas as pd
import numpy as np


chat_id = 297211248 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    conv1=x_success/x_cnt
    conv2=y_success/y_cnt
    conv_delta=conv2-conv1
    delta=2.58*((conv1*(1-conv1)/x_cnt) + (conv2*(1-conv2)/y_cnt))**0.5
    mn= conv_delta - delta
    mx=conv_delta + delta
    if (mx*mn)<0:
        res=False
    else:
        res=True
        
    return res # Ваш ответ, True или False
