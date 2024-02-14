import math
from matplotlib import pyplot as plt
import numpy as np
from scipy.io.wavfile import write
from os.path import join as pjoin
from scipy.io import wavfile

def median_filt(signal, window_size):
    window = np.asarray(signal[0:window_size])
    filt = np.asarray(window[:window_size//2])

    for i in range(len(signal) - window_size):
        print(int(i/len(signal)*100), '%')
        temp = np.sort(window)
        median = temp[window_size//2]
        filt = np.append(filt, median)
        window = window[1:]
        window = np.append(window, signal[i+window_size])
    filt = np.append(filt, signal[len(signal) - window_size//2:])
    return filt

def arith_mean_filt(signal, window_size):
    window = np.asarray(signal[0:window_size])
    filt = np.asarray(window[:window_size//2])
    for i in range(len(signal) - window_size):
        print(int(i/len(signal)*100), '%')
        mean = np.sum(window) / window_size
        filt = np.append(filt, mean)
        window = window[1:]
        window = np.append(window, signal[i + window_size])
    filt = np.append(filt, signal[len(signal) - window_size//2:])
    return filt


wav_fname = pjoin('bad_pope.wav')
samplerate, data = wavfile.read(wav_fname)
# print(f"number of channels = {data.shape[1]}")
# data = data[:1050]
length = data.shape[0] / samplerate
time = np.linspace(0., length, data.shape[0])
filtered = median_filt(data, 10)
print('5')
write("example.wav", samplerate, filtered.astype(np.int16))
# print(len(time), len(data), len(filtered))
# plt.plot(time, filtered, label="filtered")
# plt.plot(time, data, label="signal")
# plt.legend()
# plt.xlabel("Time [s]")
# plt.ylabel("Amplitude")
# plt.show()

# from pydub import AudioSegment
# from pydub.playback import play
#
# sound_audio = AudioSegment.from_wav('example.wav')
# play(sound_audio)









# # https://habr.com/ru/articles/113239/
# # сайт, откуда взято чтение ваф файла
#
# def format_db(x, pos=None):
#     if pos == 0:
#         return ""
#     global peak
#     if x == 0:
#         return "-inf"
#
#     db = 20 * math.log10(abs(x) / float(peak))
#     return int(db)
#
# def format_time(x, pos=None):
#     global duration, nframes, k
#     progress = int(x / float(nframes) * duration * k)
#     mins, secs = divmod(progress, 60)
#     hours, mins = divmod(mins, 60)
#     out = "%d:%02d" % (mins, secs)
#     if hours > 0:
#         out = "%d:" % hours
#     return out
#
# wav = wave.open("bad_pope.wav", mode="r")
# (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
# content = wav.readframes(nframes)
# # чтение из файла сигнала с помощью методов библиотеки wave
#
# types = {
#     1: np.int8,
#     2: np.int16,
#     4: np.int32
# }
# samples = content
# # разбор сигнала по кодированию семплов, 8, 16 и 32-х битное соответственно
# duration = nframes / framerate #время потока в секундах
# w, h = 800, 300 #ширина и высота изображения
# DPI = 72 #разрешение пикселей на дюйм - константа для перевода пикселей в дюймы
# peak = 256 ** sampwidth / 2 # максимальное значение амплитуды сигнала
# k = int(nframes/w/32) #коэффициент прореживания канала, эмпирический
#
# plt.figure(1, figsize=(float(w)/DPI, float(h)/DPI), dpi=DPI) # здесь идет задание размеров изображения в дюймах, с кастованием int8/16/32  в float
#
# channel = samples[::k] # прореженный сигнал
# axes = plt.subplot(1, 1, 1)
# axes.plot(channel, "g")
# axes.yaxis.set_major_formatter(ticker.FuncFormatter(format_db))
# plt.grid(True, color="w")
# axes.xaxis.set_major_formatter(ticker.NullFormatter())
# axes.xaxis.set_major_formatter(ticker.FuncFormatter(format_time))
# plt.savefig("wave", dpi=DPI)
# plt.show()