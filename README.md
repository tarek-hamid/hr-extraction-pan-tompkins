# Pan Tompkins HR extraction

## Background

The Pan Tompkins algorithm is a useful and widely used algorithm to extract heart rate from an EKG waveform. The methodology is as follows: 

1. Filter the EKG to a passband of 5-15hz
2. Derive the resultant signal using a derivative filter
3. Square the resulting signal
4. Use moving window integration to smooth the signal.

An in-depth explanation of my personal implementation can be found on my personal porfolio:

https://tarek-hamid.github.io/ecg-heart-rate/index.html

Seminal work:

Pan, Jiapu; Tompkins, Willis J. (March 1985). "A Real-Time QRS Detection Algorithm". IEEE Transactions on Biomedical Engineering. BME-32 (3): 230–236. doi:10.1109/TBME.1985.325532. PMID 3997178.

I found the Wiki article on the topic to be extremely helpful in understanding background and algorithm implementation: 

https://en.wikipedia.org/wiki/Pan%E2%80%93Tompkins_algorithm


## Repository lay-out

There are two main files of interest in the repository: 

1. pantompkins.py - Python script with methods used to implement the Pan Tompkins algorithm
2. test_pan_tompkins.pynb - Jupyter notebook with the algorithm implemented on data sourced from PhysioNet (https://physionet.org/content/mitdb/1.0.0/).

## TODO

1. Create Python package
2. Create 200ms delay if a peak is detected (lockout time due to physiological refractory period in which vertricular depolarization cannot occur)
3. Create adaptive thresholds based on surrounding noise
4. Search for missed QRS complexes based on adaptive threshold
5. Check for T wave discrimination

## Questions?

Please reach out to me at hamidtarek3@gmail.com
