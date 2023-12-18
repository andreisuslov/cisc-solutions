# fourier.py
# Andrei Suslov
# CISC 120-91

import math
import sys
import stdio
import stdarray
import stdaudio
import stddraw

def fourier_series(n, t):
    """ compute the value of the n-th fourier series at time t. """
    sum = 0.0
    for i in range(1, n + 1):
        sum += math.cos(i * t)
    return sum / n

def tone(frequency, duration, sps=44100):
    """ generate a tone of a given frequency and duration. """
    n = int(sps * duration)
    a = stdarray.create1D(n, 0.0)
    for i in range(n):
        a[i] = math.sin(2.0 * math.pi * i * frequency / sps)
    return a

def main():
    n = int(sys.argv[1])

    t_min, t_max, t_samples = -10, 10, 500
    t_step = (t_max - t_min) / (t_samples - 1)

    # Prepare arrays for plotting
    t_values = stdarray.create1D(t_samples, 0.0)
    series_values = stdarray.create1D(t_samples, 0.0)

    for i in range(t_samples):
        t_value = t_min + i * t_step
        series_value = fourier_series(n, t_value)
        t_values[i] = t_value
        series_values[i] = series_value

    stddraw.setXscale(t_min, t_max)
    stddraw.setYscale(-2.0, +2.0)

    for i in range(t_samples - 1):
        stddraw.line(t_values[i], series_values[i], t_values[i+1], series_values[i+1])

    stdio.writeln("The image of the plotted values will be generated and saved in the current directory.")
    stddraw.save("fourier_series_plot.png")

    wave = stdarray.create1D(0, 0.0)
    for series_value in series_values:
        freq = 440 + series_value * 440
        wave_segment = tone(freq, 0.01)
        wave += wave_segment

    stdaudio.playSamples(wave)
    stdaudio.wait()

if __name__ == "__main__":
    main()
