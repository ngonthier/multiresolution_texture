# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:00:30 2021

@author: gonthier
"""

import Style_Transfer as st
from Arg_Parser import get_parser_args 

max_iter = 1000
print_iter = 200

def testTexture():
    parser = get_parser_args()
    name_texture = 'TilesOrnate0158_1_S'
    output_img_name = name_texture + '_Gatys'
    parser.set_defaults(verbose=True,max_iter=max_iter,print_iter=print_iter,\
        style_img_name=name_texture,loss=['texture'],output_img_name=output_img_name) 
    args = parser.parse_args()
    st.style_transfer(args)
    print('End of the texture test')
    
def testTextureAucorr():
    parser = get_parser_args()
    name_texture = 'TilesOrnate0158_1_S'
    output_img_name = name_texture + '_autocorr'
    parser.set_defaults(verbose=True,max_iter=max_iter,print_iter=print_iter,\
        style_img_name=name_texture,loss=['autocorr'],output_img_name=output_img_name) 
    args = parser.parse_args()
    st.style_transfer(args)
    print('End of the autocorr texture test')
    
def testStyleTransfer():
    parser = get_parser_args()
    name_style = 'Hokusai_GreatWave_crop'
    name_content = 'Louvre'
    output_img_name = name_content +'_with_style_' + name_style
    init_noise_ratio = 0.1
    parser.set_defaults(verbose=True,max_iter=max_iter,print_iter=print_iter,\
        style_img_name=name_style,content_img_name=name_content,\
        loss=['texture','content'],output_img_name=output_img_name,\
        init_noise_ratio=init_noise_ratio) 
    args = parser.parse_args()
    st.style_transfer(args)
    print('End of the Style Transfer test')


if __name__ == '__main__':
    testTexture()
    testTextureAucorr()
    testStyleTransfer()