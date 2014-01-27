#!/usr/bin/python
# -*- coding: utf-8 -*-

# thumbor imaging service
# https://github.com/globocom/thumbor/wiki

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com timehome@corp.globo.com

from thumbor.filters import BaseFilter, filter_method
from thumbor.utils import logger

class Filter(BaseFilter):

    @filter_method(BaseFilter.Number, BaseFilter.Number, BaseFilter.Number, BaseFilter.Number, BaseFilter.String)
    def pad(self, t, r, b, l, color):
        logger.debug('run')
        logger.debug("pad called with t:{!r} r:{!r} b:{!r} l:{!r} color:{!r}".format(t,r,b,l,color))
        offset_x = 0
        offset_y = 0
        new_width = self.engine.size[0] + r + l
        new_height = self.engine.size[1] + t + b

        new_engine = self.context.modules.engine.__class__(self.context)
        new_engine.image = new_engine.gen_image((new_width, new_height), '#' + color)
        new_engine.image.paste(self.engine.image, (l,t))
        self.engine.image = new_engine.image
