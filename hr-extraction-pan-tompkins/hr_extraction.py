"""
Creator: Tarek Hamid; hamidtarek3@gmail.com

Data sourced from PhysioNet:
Lugovaya T.S. Biometric human identification based on electrocardiogram. [Master's thesis] Faculty of Computing Technologies and Informatics, Electrotechnical University "LETI", Saint-Petersburg, Russian Federation; June 2005.
Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.

This script uses the Pan-Tompkins algorithm to extract the heart rate from an ECG waveform. 

The algorithm works as follows:
1. Use band-pass filter to filter out noise
2. Take derivative of time series
3. Square and take the mean of the result

Usage: python3 hr_extraction.py

"""
import os
import sys

import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot

def import_data(text_file):
    df = pd.read_csv(text_file, sep='\t')
    df = pd.DataFrame(df)
    return df

def main():
    person_1_data = import_data('person_1_rec.txt')
    print(person_1_data)

if __name__ == '__main__':
    main()


