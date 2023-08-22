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

    return signal + noiseVolts

def generateSignals(frequencies, amplitudes, phases, start, stop, samplePeriod, SNR=None):
    '''
    generateSignals(frequencies, amplitudes, phases, duration, samplePeriod, SNR)

    Returns an array of times and amplitudes for a signal. The signal is generated as a superimposed list of cos waves based on the
    frequencies, amplitudes and starting phases given.
    
    Optional Key Word Arguments:
    
    '''
    times = np.linspace(start, stop, math.floor((stop - start)/samplePeriod)) #could change floor to just int
    signal = np.zeros(len(times)) 
    for (f, a, p) in zip(frequencies, amplitudes, phases):
        signal = signal + (a * np.cos(2*np.pi*f*times))
    if SNR == None: return times, signal
    else:
        return addNoise(times, signal, SNR)

