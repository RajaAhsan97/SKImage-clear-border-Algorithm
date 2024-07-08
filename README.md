This repossitory contains the algorithm to clear the border in the input image, as implemented in the skimage.segmentation clear_border function. The input to the algorithm is the 
binary image.

For identifying the borders in the image, first step is to point pixels at the border whose values are 1's, also referred as marker. Next step is the find the pixels which are connected 
with the markers (i.e. pixels with values 1's), which is accomplished by morphological dilation operation to the markers and mask the dilated image with the original image by applying bitwise_AND operation. By applying dilation operation the border in the image are expanded. For the applied mask, if all the expanded borders become equal to the masking image, then the final stage is to get the difference between the original and the expanded image. This results in the removed borders from the image.

*    Input image

![LP1](https://github.com/RajaAhsan97/SKImage-clear-border-Algorithm/assets/155144523/63b03190-24c8-4b4b-94d6-ef7562e0a14c)


*    Out image

![LP1_rslt](https://github.com/RajaAhsan97/SKImage-clear-border-Algorithm/assets/155144523/efaa0b45-e4b1-4976-bcc1-c050fc6336db)

