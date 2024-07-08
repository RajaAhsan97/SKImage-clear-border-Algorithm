This repossitory contains the algorithm to clear the border in the input image, as implemented in the skimage.segmentation clear_border function. The input to the algorithm is the 
binary image.

For identifying the borders in the image, first step is to point pixels at the border whose values are 1's, also referred as marker. Next step is the find the pixels which are connected 
with the markers, which is accomplished by morphological dilation operation to the markers and mask the dilated image with the original image by applying bitwise_AND operation. By applying
dilation operation the border in the image are expanded. for the applied mask, if all the expanded borders become equal to the masking image, then the final stage is to get the difference 
between the original and the expanded image. This results in the removed borders from the in image.
