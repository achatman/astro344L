from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

color_palette = 'Purples'

def save_image(data_frame, filepath, low=None, high=None):
    print('Saving', filepath)
    if low == None:
        low, _ = np.percentile(data_frame.flatten(), [0.5,99.5])
    if high == None:
        _, high = np.percentile(data_frame.flatten(), [0.5,99.5])
    plt.imshow(data_frame, cmap=color_palette, vmin=low, vmax=high)
    plt.colorbar()
    plt.savefig(filepath)
    plt.clf()

def save_fits(data_frame, filepath):
    print('Saving', filepath)
    hdu = fits.PrimaryHDU(data_frame)
    hdul = fits.HDUList([hdu])
    hdul.writeto(filepath, overwrite=True)



#100ms

#Load Dark Frames
darkframes = [fits.getdata(f'raw_data/Albireo_V_Dark_100ms_{i:03}.FITS') for i in range(1,6)]
med_dark_frame = np.median(darkframes, axis=0)
save_image(med_dark_frame, 'dark_fields/100ms.png')

#V Band
for i in range(1,11):
    df = fits.getdata(f'raw_data/Albireo_V_100ms_{i:03}.FITS')
    save_image(df, f'data_fields/Albireo_V_100ms_{i:03}.png')
    dark_sub = df - med_dark_frame
    save_image(dark_sub, f'subtracted_fields/Albireo_V_100ms_{i:03}.png', low=0)
    save_fits(dark_sub, f'subtracted_fields/Albireo_V_100ms_{i:03}.FITS')

#I Band
for i in range(1,4):
    df = fits.getdata(f'raw_data/Albireo_I_100ms_{i:03}.FITS')
    save_image(df, f'data_fields/Albireo_I_100ms_{i:03}.png')
    dark_sub = df - med_dark_frame
    save_image(dark_sub, f'subtracted_fields/Albireo_I_100ms_{i:03}.png', low=0)
    save_fits(dark_sub, f'subtracted_fields/Albireo_I_100ms_{i:03}.FITS')

#B Band
for i in range(1,4):
    df = fits.getdata(f'raw_data/Albireo_B_100ms_{i:03}.FITS')
    save_image(df, f'data_fields/Albireo_B_100ms_{i:03}.png')
    dark_sub = df - med_dark_frame
    save_image(dark_sub, f'subtracted_fields/Albireo_B_100ms_{i:03}.png', low=0)
    save_fits(dark_sub, f'subtracted_fields/Albireo_B_100ms_{i:03}.FITS')


#200 ms

#Load Dark Frames
darkframes = [fits.getdata(f'raw_data/Albireo_V_Dark_200ms_{i:03}.FITS') for i in range(1,6)]
med_dark_frame = np.median(darkframes, axis=0)
save_image(med_dark_frame, 'dark_fields/200ms.png')

for i in range(1,4):
    df = fits.getdata(f'raw_data/Albireo_V_200ms_{i:03}.FITS')
    save_image(df, f'data_fields/Albireo_V_200ms_{i:03}.png')
    dark_sub = df - med_dark_frame
    save_image(dark_sub, f'subtracted_fields/Albireo_V_200ms_{i:03}.png', low=0)
    save_fits(dark_sub, f'subtracted_fields/Albireo_V_200ms_{i:03}.FITS')

#300 ms

#Load Dark Frames
darkframes = [fits.getdata(f'raw_data/Albireo_V_Dark_300ms_{i:03}.FITS') for i in range(1,6)]
med_dark_frame = np.median(darkframes, axis=0)
save_image(med_dark_frame, 'dark_fields/300ms.png')

for i in range(1,4):
    df = fits.getdata(f'raw_data/Albireo_V_300ms_{i:03}.FITS')
    save_image(df, f'data_fields/Albireo_V_300ms_{i:03}.png')
    dark_sub = df - med_dark_frame
    save_image(dark_sub, f'subtracted_fields/Albireo_V_300ms_{i:03}.png', low=0)
    save_fits(dark_sub, f'subtracted_fields/Albireo_V_300ms_{i:03}.FITS')
