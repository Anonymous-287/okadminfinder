#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.4.1'
__author__ = 'o.koleda'
__license__ = 'Apache 2.0'
__improver__= 'Anonymous-287'

def getCredits():

    return ''''
       ____  __ __          __          _       _______           __
   / __ \/ //_/___ _____/ /___ ___  (_)___  / ____(_)___  ____/ /__  _____
  / / / / ,< / __ `/ __  / __ `__ \/ / __ \/ /_  / / __ \/ __  / _ \/ ___/
 / /_/ / /| / /_/ / /_/ / / / / / / / / / / __/ / / / / / /_/ /  __/ / ver %s
 \____/_/ |_\__,_/\__,_/_/ /_/ /_/_/_/ /_/_/   /_/_/ /_/\__,_/\___/_/ license %s
                                            special for Pentest Box
                                                      %s
						      %s
    ''' % (__version__, __license__, __author__, __improver__,), __version__
