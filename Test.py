#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed 24 February 2021

The goal of this script is just to run a test after a new installation of
the project 

@author: nicolas
"""

import Run_synthesis as rs
from Arg_Parser import get_parser_args 

max_iter = 1000
print_iter = 200

def testTexture():
    parser = get_parser_args()
    name_texture = 'TilesOrnate0158_1_S' # Image in size 256*256
    output_img_name = name_texture + '_Gram'
    parser.set_defaults(verbose=True,max_iter=max_iter,print_iter=print_iter,\
        texture_ref_name=name_texture,loss=['Gram'],output_img_name=output_img_name) 
    args = parser.parse_args()
    rs.run_synthesis(args)
    print('End of the texture test with Gram Matrices')
    
def testTextureAucorr():
    parser = get_parser_args()
    name_texture = 'TilesOrnate0158_1_S' # Image in size 256*256
    output_img_name = name_texture + '_autocorr'
    parser.set_defaults(verbose=True,max_iter=max_iter,print_iter=print_iter,\
        texture_ref_name=name_texture,loss=['autocorr'],output_img_name=output_img_name) 
    args = parser.parse_args()
    rs.run_synthesis(args)
    print('End of the autocorr texture test')
  
def testTextureMSInit():
    parser = get_parser_args()
    name_texture = 'TexturesCom_BrickSmallBrown0473_1_M_1024' # Image in size 1024*1024
    output_img_name = name_texture + '_Gram_Spectrum_MSInit'
    parser.set_defaults(verbose=True,max_iter=max_iter,print_iter=print_iter,\
        texture_ref_name=name_texture,loss=['Gram','spectrum'],
        output_img_name=output_img_name,MS_Strat='Init') 
    args = parser.parse_args()
    rs.run_synthesis(args)
    print('End of the autocorr texture test')

if __name__ == '__main__':
    testTexture()
    testTextureAucorr()
    testTextureMSInit()
