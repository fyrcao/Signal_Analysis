weight1, height1, age1 = 60, 1.75, 20
weight2, height2, age2 = 50, 1.61, 18
ratio_weight = weight1/weight2
if ratio_weight > 1:
    print ('вес 1 пациента превышает вес второго в' ratio_weight 'раз')
    else:
        ratio_weight = weight2/weight1
        print ('вес 1 пациента превышает вес второго в' ratio_weight 'раз')
        ratio_height = height1/height2
if ratio_height > 1:
    print ('вес 1 пациента превышает вес второго в' ratio_height 'раз')
    else:
        ratio_height = height2/height1
        print ('вес 1 пациента превышает вес второго в' ratio_height 'раз')
imb1 = weight1 / height1**2
imb2 = weight2 / height2**2
file_name = input()
parts = file_name.split('_')
if len(parts) != 5:
    print('Некорректное название файла')
id_str = parts[0] [:2]
id = int(id_str)
channel_str = parts[1] [:2]
channel = int(channel_str)
frequency_str = parts[2] [:1]
frequency = float(frequency_str)
amplitude_str = parts[3] [:1]
amplitude = float(amplitude_str)
noise_str = parts[4] [:1]
noise = float(noise_str)
print('Идентификатор пациента: ' id)
print('Номер канала: ' channel)
print('Частота: ' frequency)
print('Амплитуда: ' amplitude)
print('Шум:' noise)


         
