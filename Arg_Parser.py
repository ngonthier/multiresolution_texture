#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 

Arguments parser for the function

@author: nicolas
"""

import argparse

def get_parser_args():
    """
    Parser of the argument of the program
    Becareful there is an order to use the option in the command line 
    terminal :'(
    """
    desc = "TensorFlow implementation of 'High resolution neural texture synthesis with long range constraints'"  
    parser = argparse.ArgumentParser(description=desc)

    # Verbose argument
    parser.add_argument('-v','--verbose',action="store_true",
        help='Boolean flag indicating if statements should be printed to the console.')
        
    parser.add_argument('--debug',action="store_true",
        help='Boolean flag indicating if the debug statements should be printed to the console.')

        
    parser.add_argument('--saveMS',action="store_true",
        help='Boolean flag indicating if intermediate images with a MS strategy have to be saved.')
        
    parser.add_argument('--savedIntermediateIm',action="store_true",
        help='Boolean flag indicating if we save the intermediate reference images at a specific scale.')
    
    parser.add_argument('--iprint',  type=int,default=0,
        help='Number of iterations between optimizer print statements for the lbfgs algo only. (default %(default)s)')
        
    parser.add_argument('--print_iter',  type=int,default=0,
        help='Number of iterations between optimizer save the image or  print statements for the lbfgs algo only. (default %(default)s)')
        
    # Name of the Images
    parser.add_argument('-o','--output_img_name', type=str, 
        default='Pastiche',help='Filename of the output image.')
        
    parser.add_argument('-s','--texture_ref_name',  type=str,default='TilesOrnate0158_1_S',
        help='Filename of the texture reference image. It must be a .png image otherwise change the img_ext.')
          
    # Name of the folders 
    parser.add_argument('-f','--img_folder',  type=str,default='images/',
        help='Name of the images folder')
  
    parser.add_argument('--img_output_folder',  type=str,default='images_output/',
        help='Name of the images output folder, need to be in the format namefolder/')
  
    parser.add_argument('--data_folder', type=str,default='data/',
        help='Name of the data folder')
    
    # Extension of the image
    parser.add_argument('--img_ext',  type=str,default='png',
        choices=['jpg','png'],help='Extension of the image') 
    #TODO : remove the '.' that cannot be read in command line 
        
    # Infomartion about the optimization
    parser.add_argument('--optimizer',  type=str,default='lbfgs',
        choices=['lbfgs', 'adam', 'GD'],
        help='Loss minimization optimizer. (default|recommended: %(default)s)')
    
    parser.add_argument('--max_iter',  type=int,default=1000,
        help='Number of Iteration Maximum. (default %(default)s)')
           
    parser.add_argument('--maxcor',  type=int,default=20,
        help='The maximum number of variable metric corrections used to define the limited memory matrix in LBFGS method. (default %(default)s)')
        
    parser.add_argument('--learning_rate',  type=float,default=10.,
        help='Learning rate only for adam or GD method. (default %(default)s) We advised to use 10 for Adam and 10**(-10) for GD')  
        
    # Argument for clipping the value in the Adam or GD case
    parser.add_argument('--clip_var',  type=int,default=1,
        help='Clip the values of the variable after each iteration only for adam or GD method. Equal to 1 for true and 0 otherwise (default %(default)s)')  
    
    parser.add_argument('--clipping_type', type=str,choices=['ImageNet','ImageStyle','ImageStyleBGR'],
        default='ImageStyleBGR',help='Element that we use to compute clip values : ImageNet means, the image style or each channel of the iamge style. (default %(default)s)')  
    

    parser.add_argument('--init_noise_ratio',type=float,default=1.0,
        help='Propostion of the initialization image that is noise : 1 means  100 % of the image is noise. (default %(default)s)')
        
    parser.add_argument('--init',type=str,default='Gaussian',choices=['Uniform','smooth_grad','Gaussian','Cst'],
        help='Type of initialization for the image variable.')
        
    parser.add_argument('--init_range',type=float,default=127.5,
        help='Range for the initialialisation value')
        
    parser.add_argument('--start_from_noise',type=int,default=1,choices=[0,1],
        help='Start compulsory from the content image noised if = 1 or from the former image with the output name if = 0. (default %(default)s)')
    
    # About the way some of the thing are computed
    parser.add_argument('--GramLightComput',action="store_true",
        help='If True it will try to compute a light version of the Gram Matrix (default: %(default)s)')
    
    # if true we recompute the Gram precomputed and stored data
    parser.add_argument('--recomputePrepocess',action="store_true",
        help='If True we recompute the Gram and content precomputed and store data (default: %(default)s)')
    
    # VGG 19 info
    parser.add_argument('--pooling_type', type=str,default='avg',
        choices=['avg', 'max'],help='Type of pooling in convolutional neural network. (default: %(default)s)')
    
    parser.add_argument('--non_linearity_type', type=str,default='relu',
        choices=['relu', 'leaky_relu','id'],help='Type of non linearity in convolutional neural network. (default: %(default)s)')
    
    parser.add_argument('--padding', type=str,choices=['SAME','Circular','VALID'],
        default='SAME',help='Type of padding in the network. (default: %(default)s)')
        
    parser.add_argument('--vgg_name', type=str,
        choices=['normalizedvgg.mat','imagenet-vgg-verydeep-19.mat'],
        default='normalizedvgg.mat',
        help='Name of the network to use, it must be in the same place that the Run_synthesis script. (default: %(default)s)')
    
    # Info on the loss function 
    parser.add_argument('-l','--loss',nargs='+',type=str,default='Gram',
        choices=['Gram','autocorr','spectrum'],
        help='Choice the terms of the loss function. (default %(default)s)')
          
    parser.add_argument('--used_layers', nargs='+', type=str,
        default=['relu1_1','pool1','pool2','pool3','pool4'],
        help='VGG19 layers used for the Texture loss. (default: %(default)s)') 
        # Need to have config_layers = Custom to change that
    
    parser.add_argument('--texture_layer_weights', nargs='+', type=float, 
        default=[1.,1.,1.,1.,1.],
        help='Contributions (weights) of each texture layer to loss. (default: %(default)s)') # TODO change that to be able to choose only one number, the same weight for all
        
    parser.add_argument('--config_layers',type=str,default='Custom',choices=['PoolConfig','FirstConvs','GatysConfig','Custom','DCor'],
        help='Configuration already saved for the choice of the content and style layers and weights choosen, need to be None to allow user to change. (default: %(default)s)') 
        
    parser.add_argument('--beta_spectrum',  type=float,default=10**5,
        help='Value of the weight on the spectrum constraint [Gang 2017]. (default: %(default)s)')
        
    parser.add_argument('--eps',  type=float,default=10**(-16),
        help='Value of the epsilon value in the spectrum constraint. (default: %(default)s)')
    
    parser.add_argument('--gamma_autocorr',  type=float,default=1.,
        help='Value of the weight on the autocorr loss. (default: %(default)s)') 
        
    parser.add_argument('--MS_Strat',  type=str,default='',
		choices=['','Init','Constr'],
        help='Multi scale strategy, if none no use of the multiscale strategy. If Init use the lower scale as initialisation, Constr is a hard constraint. (default: %(default)s)')
         
    parser.add_argument('--K',  type=int,default=2,
        help='Number of scale for the multi scale strategy : this parameter have the priority on --MS_minscale. (default: %(default)s)') 
    
    parser.add_argument('--MS_minscale',  type=int,default=256,
        help='Minimum scale for the multi scale strategy used if K==-1. (default: %(default)s)') 

    parser.add_argument('--WLowResConstr', type=float,default=1.,
        help='Weight for the MultiScale strategy constraint. (default: %(default)s)') 

    # GPU Config :
    parser.add_argument('-g','--gpu_frac',  type=float,default=0.,
        help='Fraction of the memory for the GPU process, if <=0. then memoryground = True. And if > 1. then normal behaviour ie 0.95%% of the memory is allocated without error. (default %(default)s)')
    
    return(parser)
