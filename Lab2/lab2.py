from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

color_palette = 'Purples'

#100ms

#Load Dark Frames
darkframes = [fits.getdata(f'raw_data/Albireo_V_Dark_100ms_00{i}.FITS') for i in range(1,6)]
med_dark_frame = np.median(darkframes, axis=0)
low, high = np.percentile(med_dark_frame.flatten(), [1,99])
plt.imshow(med_dark_frame, cmap=color_palette, vmin=low, vmax=high)
plt.colorbar()
plt.savefig('dark_fields/100ms.png')
plt.clf()

dataframes = [fits.getdata(f'raw_data/Albireo_V_100ms_{i:03}.FITS') for i in range(1,11)]
i = 1
for df in dataframes:
    low, high = np.percentile(df.flatten(), [1,99])
    plt.imshow(df, cmap=color_palette, vmin=low, vmax=high)
    plt.colorbar()
    plt.savefig(f'data_fields/Albireo_V_100ms_00{i}.png')
    plt.clf()

    dark_sub = df - med_dark_frame
    low, high = np.percentile(dark_sub.flatten(), [1,99])
    plt.imshow(dark_sub, cmap=color_palette, vmin=low, vmax=high)
    plt.colorbar()
    plt.savefig(f'subtracted_fields/Albireo_V_100ms_00{i}.png')

    hdu = fits.PrimaryHDU(dark_sub)
    hdul = fits.HDUList([hdu])
    hdul.writeto(f'subtracted_fields/Albireo_V_100ms_00{i}.FITS')

    i += 1
