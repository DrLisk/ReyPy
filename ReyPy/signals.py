import math
import numpy as np

def addNoise(signal, SNR):
    '''
    addNoise(signal, SNR)

    Takes an array of points of a signal, and an SNR in dB.

    Returns the signal with guassian white noise added to a defined Signal to Noise ratio by signal power.
    '''
    signalAveragePower = 10 * np.log10(np.mean(signal**2))  #find the power of the signal in dB 
    noiseToAddWatts = 10 ** ((signalAveragePower - SNR)/10) #find the power of the noise to add in watts 
    noiseVolts = np.random.normal(0, np.sqrt(noiseToAddWatts), len(signal)) # signal might need to be signalAveragePower. mean is 0 for the noise
    
    signal = signal + noiseVolts
    return signal

def generateSignals(frequencies, amplitudes, phases, start, stop, samplePeriod, SNR=None):
    '''
    generateSignals(frequencies, amplitudes, phases, duration, samplePeriod, SNR)

    Returns an array of times and amplitudes for a signal. The signal is generated as a superimposed list of cosines based on the
    frequencies, amplitudes and starting phases given.
    
    Optional Key Word Arguments:
    
    '''
    times = np.linspace(start, stop, math.floor((stop - start)/samplePeriod)) #could change floor to just int
    signal = np.zeros(len(times))
    for (f, a, p) in zip(frequencies, amplitudes, phases):
        signal = signal + (a * np.cos(2*np.pi*f*times + p))
    if SNR == None: return times, signal
    else:
        return times, addNoise(signal, SNR)

def FFT(signal, timestep):
    '''
    
    '''
    if timestep is None:
        timestep = 1
        t = np.arange(0, signal.shape[-1])
    else:
        t = np.arange(0, signal.shape[-1]) * timestep

    if signal.shape[0] %2 != 0:
        warnings.warn("Signal preffered to be even in shape, dropping last sample")
        t = t[0:-1]
        signal = signal[0:-1]

    complexes = np.fft.fft(signal) / t.shape[0] #divide by size t to get correct amplitude
    frequencies = np.fft.fftfreq(t.shape[0], d=timestep)

    return frequencies, complexes 

def realFFT(signal, timestep):
    frequencies, complexes = FFT(signal, timestep)

    firstNegInd = np.argmax(frequencies<0) # remove negative values since we are looking at real FFT
    freqAxisPos = frequencies[0:firstNegInd]
    sigFFTPos = 2 * complexes[0:firstNegInd] # we * 2 here because we are looking at the magnitude of an analytical signal

    magnitudes = np.abs(sigFFTPos)
    angles = np.angle(sigFFTPos)

    return freqAxisPos, magnitudes, angles
