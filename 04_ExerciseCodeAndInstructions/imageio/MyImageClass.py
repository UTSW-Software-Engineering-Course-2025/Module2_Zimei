from re import L
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

#define an image class that has useful functions we can use!

class MyImgClass():
    """
    This is the custom class for our lesson 2.
    It contains all the methods to run the accompanying notebook.
    Many you will be implementing.

    """
    
    def __init__(self, arrImg, intLabel=None):
        """Initalize the MyImgClass object

        :param arrImg: a numpy array that contains the image
        :type arrImg: np.array
        :param intLabel: the label value, defaults to None
        :type intLabel: int, optional
        """
        self.arrImg = arrImg
        self.intLabel = intLabel
        self.shape = self.arrImg.shape
        
    def __add__(self, other):
        """
        operator overloading for the '+' operation 
        element wise addtion of two MyImgClass together.

        :param other: the other instance of arrImgClass
        :type other: arrImgClass
        :return: the addition of the two classes
        :rtype: MyImgClass
        """
        toReturn = MyImgClass(np.add(self.arrImg, other.arrImg), intLabel=None)
        return toReturn
    
    def __sub__(self, other):
        """
        operator overloading for the '-' operation 
        element wise subtraction of two MyImgClass together.

        :param other: the other instance of arrImgClass
        :type other: arrImgClass
        :return: the subtraction of the two classes
        :rtype: MyImgClass
        """

        return MyImgClass(np.subtract(self.arrImg, other.arrImg), intLabel=None)
        
    
    def fPixelwiseSqDif(self, other):
        """Find the square difference between two MyImgClass objects

        :param other: the other instance of arrImgClass
        :type other: arrImgClass
        :return: square difference of each pixel
        :rtype: MyImgClass
        """
        ### TO IMPLEMENT ###
        # Use the overloaded '-' from above
        diff = self - other

        return MyImgClass(np.square(diff.arrImg), intLabel=None)
    
    
    
    def fMSE(self, other):
        """Find the mean squared error between two images

        :param other: the other instance of arrImgClass
        :type other: arrImgClass
        :return: MSE
        :rtype: float
        """
        squared_diff_img_obj = self.fPixelwiseSqDif(other)
        return np.mean(squared_diff_img_obj.arrImg)

    
    def fPlot(self, ax, show_ticks=False, add_colorbar=False, imshow_kwargs={}):
        """Plotting method for the class

        :param ax: the axis to plot on
        :type ax: matplotlib.pyplot.ax
        :param show_ticks: display the x and y axis ticks/labels, defaults to False
        :type show_ticks: bool, optional
        :param add_colorbar: display a color bar, defaults to False
        :type add_colorbar: bool, optional
        :param imshow_kwargs: additional keywords, defaults to {}
        :type imshow_kwargs: dict, optional
        """
        img = ax.imshow(self.arrImg, interpolation='None', **imshow_kwargs)
        if not self.intLabel is None:
            ax.set_title(f'Label: {self.intLabel}')
        if show_ticks is False:
            ax.axes.xaxis.set_ticks([])
            ax.axes.yaxis.set_ticks([])
        if add_colorbar:
            divider = make_axes_locatable(ax)
            cax = divider.append_axes('right', size='5%', pad=0.05)
            plt.colorbar(img, cax=cax, orientation='vertical')        
        
    @staticmethod
    def fComputeMeanAcrossImages(lMyImgClass):
        """Calcualte the mean image from a list of images

        :param lMyImgClass: list of MyImgClass
        :type lMyImgClass: list (or 1D iterable)
        :return: The mean image
        :rtype: MyImgClass
        """
        npmean = np.mean([i.arrImg for  i in lMyImgClass],axis=0)
        return MyImgClass(npmean, intLabel=None)
        # raise NotImplementedError('You need to implement this method!')
    
    @staticmethod
    def fComputeStdAcrossImages(lMyImgClass):
        """Calcualte the std image from a list of images

        :param lMyImgClass: list of MyImgClass
        :type lMyImgClass: list (or 1D iterable)
        :return: The std image
        :rtype: MyImgClass
        """
        # image_arrays = []
        # first_shape = None
        # for i, img_obj in enumerate(lMyImgClass):
        #     if not isinstance(img_obj, MyImgClass): # MyImgClass should be in scope
        #         raise TypeError(f"All items in lMyImgClass must be MyImgClass instances. Found {type(img_obj)} at index {i}.")
            
        #     if i == 0:
        #         first_shape = img_obj.shape
        #     elif img_obj.shape != first_shape:
        #         raise ValueError("All images in the list must have the same dimensions to compute standard deviation across them.")
            
        #     image_arrays.append(img_obj.arrImg)

        # Calculate the standard deviation across the images (pixel-wise)
        # np.std will operate along the first axis (axis=0) of the stacked image arrays.
        # std_dev_array = np.std(image_arrays, axis=0)
        npstd = np.std([i.arrImg for  i in lMyImgClass],axis=0)
        # Wrap the resulting numpy array in a MyImgClass object
        return MyImgClass(npstd, intLabel=None)
        

    @staticmethod
    def fMeanMSE(lImg1, lImg2):
        """Calcualte the mean MSE across pairs of images
        e.g. mean(MSE(lImg1[0],lImg2[0]),MSE(lImg1[1],lImg2[1])...)

        :param lImg1: list of MyImgClass
        :type lImg1: list (or 1D iterable)
        :param lImg2: list of MyImgClass
        :type lImg2: list (or 1D iterable)
        :return: mean MSE
        :rtype: float
        """
        lista = [lImg1[i].fMSE(lImg2[i]) for i in range(len(lImg1))]        
        return np.mean(lista)


    @staticmethod
    def fMSEforEachPairCombination(lImg1, lImg2):
        """Calcaulte the MSE for all pairs between lImg1 and lImg2

        :param lImg1: list of MyImgClass
        :type lImg1: list (or 1D iterable)
        :param lImg2: list of MyImgClass
        :type lImg2: list (or 1D iterable)
        :return: mean MSE
        :rtype: float
        """
        lSE = []
        for imgI in lImg1:
            for imgJ in lImg2:
                if imgI != imgJ:
                    lSE.append(imgI.fMSE(imgJ))
                else:
                    lSE.append(np.nan)
        return lSE

