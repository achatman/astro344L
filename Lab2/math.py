import numpy as np

delta_alpha = 35.3
image_dims = np.asarray((765, 510))

pixel_scales = list()
num = 0
with open('coords.csv') as infile:
    with open('distance.csv', mode='w') as outfile:
        outfile.write('delta_pix, pixel_scale\n')
        infile.readline()
        for line in infile:
            num += 1
            arr = line.split(',')
            delta_pix = ( (float(arr[0]) - float(arr[2]))**2 +
                          (float(arr[1]) - float(arr[3]))**2 )**0.5
            pixel_scale = delta_alpha / delta_pix
            pixel_scales.append(pixel_scale)
            outfile.write(str(delta_pix) + ',' + str(pixel_scale) + '\n')

pixel_scale_avg = (1/num)*sum([a for a in pixel_scales])
pixel_scale_stdev = ( (1/(num-1))*sum([(a - pixel_scale_avg)**2 for a in pixel_scales]) )**0.5

print('pixel_scale_avg:', pixel_scale_avg)
print('pixel_scale_stdev:', pixel_scale_stdev)

fov = image_dims*pixel_scale_avg
fov_err = fov * (pixel_scale_stdev / pixel_scale_avg)

print(fov[0] * (pixel_scale_stdev / pixel_scale_avg))

print('fov:', fov)
print('fov_err:', fov_err)
