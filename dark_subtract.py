from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt
import sys

color_palette = 'Purples'



def save_image(data_frame, filepath):
    print('Saving', filepath)
    low, high = np.percentile(data_frame.flatten(), [0.5,99.5])
    plt.imshow(data_frame, cmap=color_palette, vmin=low, vmax=high)
    plt.colorbar()
    plt.savefig(filepath)
    plt.clf()

def save_fits(data_frame, filepath):
    print('Saving', filepath)
    hdu = fits.PrimaryHDU(data_frame)
    hdul = fits.HDUList([hdu])
    hdul.writeto(filepath, overwrite=True)

def median_dark(path, ext):
    paths = [f'{path}{i:03}{ext}' for i in range(1,6)]
    frames = [fits.getdata(path) for path in paths]
    return np.median(frames, axis=0)


ext = sys.argv[1]
if not '.' in ext:
    ext = '.' + ext
datapath = sys.argv[2]
darkpath = sys.argv[3]
med_dark = median_dark(darkpath, ext)
save_image(med_dark, darkpath + 'median' + '.png')
save_fits(med_dark, darkpath+ 'median' + ext)
for i in range(1,6):
    path = f'{datapath}{i:03}{ext}'
    df = fits.getdata(path)
    dark_sub = df - med_dark
    save_image(df, f'{datapath}subbed_{i:03}.png')
    save_fits(df, f'{datapath}subbed_{i:03}{ext}')
