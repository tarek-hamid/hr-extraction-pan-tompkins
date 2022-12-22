import numpy as np
from scipy.signal import butter, sosfilt, find_peaks
from scipy.ndimage import uniform_filter1d

'''

The following functions are used to compute heart rate using the Pan-Tompkins algorithm. 
Please find more background information here: www.github.com/tarek-hamid/hr-extraction-pan-tompkins

Derivative and square functions are separated into their own functions despite using numpy packages as additional measures can be used to make the
calculations more robust.

Seminal work: 
    Pan, Jiapu; Tompkins, Willis J. (March 1985). "A Real-Time QRS Detection Algorithm". IEEE Transactions on Biomedical Engineering. BME-32 (3): 230–236. doi:10.1109/TBME.1985.325532

'''

def compute_hr(unfiltered_ecg_signal, fs):
    """
        Computes heart rate from an ECG signal based on the Pan Tompkins algorithm.

        Args: 
            unfiltered_ecg_signal (1D array): array data with ECG voltage values. 
            fs (integer): sampling frequency of the signal
        Returns:
            heart_rate (integer): calculated heart_rate from the ECG sample
    """

    # Compute integrated signal per Pan Tompkins methodology
    filtered_signal = filter_signal(unfiltered_ecg_signal, fs)
    derivative_signal = derivative(filtered_signal)
    squared_signal = square_signal(derivative_signal)
    integrated_signal = moving_window_integration(squared_signal, fs)

    # Find peaks using scipy find peaks function with fixed prominence 
    peaks = len(find_peaks(integrated_signal, prominence=0.0005)[0])

    # Calculate heart rate by dividing peaks by time period of sample and multiplying by 60
    heart_rate = int((peaks / (len(unfiltered_ecg_signal)/fs)) * 60)

    return heart_rate

def filter_signal(unfiltered_ecg_signal, fs):
    """
        Filters signal using second order Butterworth Filter with a bandpass of 5-15hz. 
        
        Args: 
            unfiltered_ecg_signal (1D array): array data with ECG voltage values. 
            fs (integer): sampling frequency of the signal
        
        Returns:
            filtered_signal (1D array): array data with filtered ECG voltage values. 
    """
    
    nyquist = 0.5 * fs
    low_cutoff = 5 / nyquist
    high_cutoff = 15 / nyquist
    coeff = butter(2, [low_cutoff, high_cutoff], analog=False, btype='band', output='sos')
    filtered_signal = sosfilt(coeff, unfiltered_ecg_signal) 
    return filtered_signal

def derivative(filtered_ecg):
    """
        Computes derivative of filtered ECG signal

        Args: 
            ecg (1D array): array data with filtered ECG voltage values. 
        Returns:
            derivative (1D array): array data with derivative of filtered ecg values.
    """

    derivative = np.diff(filtered_ecg)
    return derivative

def square_signal(derivative_ecg_signal):
    """
        Computes square of derivative of filtered ECG signal

        Args: 
            derivative_ecg_signal (1D array): array data with derivative of filtered ECG voltage values. 
        Returns:
            squared_signal (1D array): array data with derivative of filtered ecg values, squared.
    """

    squared_signal = np.square(derivative_ecg_signal)
    return squared_signal

def moving_window_integration(squared_ecg_signal, fs):
    """
        Computes moving window integrated ECG signal.

        Args: 
            squared_ecg_signal (1D array): array data with derivative of filtered ECG voltage values, squared. 
        Returns:
            integrated_signal (1D array): moving window integrated ECG signal.
    """

    # Window size is 150ms per Pan Tompkins implementation
    window_size = int(0.15 * fs)

    # Moving window integration can be computed in two ways

    # Slower way -> convolve signal with constant convolution kernel
    # integrated_signal = np.convolve(ecg, np.ones(window_size), 'same') / window_size

    # Faster way -> uniform_filter1d function
    integrated_signal = uniform_filter1d(squared_ecg_signal, window_size)

    return integrated_signal    
