def FFT (): # Sprectro de Fourier
    import cv2
    import numpy as np

    # Assign image and transform to grey
    file = 'lenna.png'
    #file = 'lena2.jpg'
    img1 = cv2.imread(file)                             # Original image
    img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)       # Image in Greyscale
    img3 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)       # Image in Fast Fourier Transform
    img4 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)       # Image returned after FFT

    # Read all the image size and define 3rd image acc with the Fast Fourier Transform
    for y in range(len(img1)):                          # Count until max line
        for x in range(len(img1[0])):                   # Count until max column
            img3[y, x] = img2[y, x] * (-1)**(x + y)     # Shift the border to center

    # Fast Fourier Transform Img2
    img3 = np.fft.fft2(img3)
    R = 1                                              # Define the intensive of the pixel to ignore
    P = img3.real ** 2 + img3.imag ** 2                 # Complex number module
    P = np.log10(P + 1)
    b = np.max(P)                                       # Max intensity
    P = (P / b) * 255
    img3 = P

    # Localize the center pixel on the image
    xc = len(img2[0]) / 2
    yc = len(img2) / 2

    # Fast Fourier Transform Img3
    img4 = np.fft.irfft2(img3)

    # Filter values acc. to R
    for y in range(len(img1)):          # Count until max line
        for x in range(len(img1[0])):   # Count until max column
            d = ((x - xc)**2 + (y - yc)**2)**0.5
            # Filter lower frequencies
            #if d >= R:
            #    img4[y,x] = 0

    # Read all the image size and define 4th image return the transformation of image 3
    for y in range(len(img1)):          # Count until max line
        for x in range(len(img1[0])):   # Count until max column
            img4[y, x] = img4[y, x] / (-1)**(x + y)       # Shift the center to border

    # Format FFT images to print
    img3 = np.array(img3.real, dtype=np.uint8)
    img4 = np.array(img4.real, dtype=np.uint8)

    # Make the greyscale images have three channels in order to concatenate
    img2_3_channel = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
    img3_3_channel = cv2.cvtColor(img3, cv2.COLOR_GRAY2BGR)
    img4_3_channel = cv2.cvtColor(img4, cv2.COLOR_GRAY2BGR)

    # Resize the images to a percent of its original size in order to show in the screen
    siz = 300 / len(img1[0])
    img1 = cv2.resize(img1, (0, 0), None, siz, siz)
    img2 = cv2.resize(img2_3_channel, (0, 0), None, siz, siz)
    img3 = cv2.resize(img3_3_channel, (0, 0), None, siz, siz)
    img4 = cv2.resize(img4_3_channel, (0, 0), None, siz, siz)

    # Concatenate the 3 images
    numpy_horizontal_concat = np.concatenate((img1, img2, img3, img4), axis=1)

    # Show the images
    cv2.imshow('Original / Greyscale / FFT / Returned', numpy_horizontal_concat)

    # Wait a key to finish
    cv2.waitKey()
    cv2.destroyAllWindows()
FFT()