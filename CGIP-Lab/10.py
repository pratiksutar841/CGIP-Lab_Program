""" 10]  Write a program to blur and smoothing an image. """

img = cv2.imread("/content/sample_data/smaple.jpg", cv2.IMREAD_GRAYSCALE)
image_array = np.array(img)
print(image_array)


def sharpen():
    return np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])


def filtering(image, kernel):
    m, n = kernel.shape
    if m == n:
        y, x = image.shape
        y = y - m + 1  # shape of image - shape of kernel + 1
        x = x - m + 1
        new_image = np.zeros((y, x))
        for i in range(y):
            for j in range(x):
                new_image[i][j] = np.sum(image[i : i + m, j : j + m] * kernel)
    return new_image


# Display the original and sharpened images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_array, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(filtering(image_array, sharpen()), cmap="gray")
plt.title("Blurred Image")
plt.axis("off")
plt.show()
