# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 09:36:29 2015

@author: Brian
"""

from __future__ import division
import numpy as np

#Name, MyRating, RTPub, RTCritic, MCPub, MCCritic
#At least 20 useful tweets required
#.975 Threshold:
MovieData = [
('A Most Violent Year 0413', .64, .73, .90, .71, .79),#289
('American Psycho 0413', .76, .85, .67, .82, .64),#178
('American Sniper 0413', .78, .86, .73, .66, .72),#3346
('Annie 0408', .73, .62, .28, .47, .33),#3876
#('Batman And Robin 0413', .56, .16, .11, .32, .28),#670 Unrelated movie Batman vs Robin
('Big Hero 6 0407', .87, .92, .89, .80, .74),#3015
('Birdman 0407', .63, .80, .93, .79, .88),#884
('Blackhat 0413', .20, .26, .33, .53, .51),#417
('Boyhood 0413', .72, .82, .98, .77, 1.0),#1069
('Chappie 0327', .79, .63, .31, .76, .41),#2408
('Cinderella 0327', .87, .85, .84, .75, .67),#18000
('Dear White People 0408', .79, .64, .92, .65, .79),#203
('Divergent 0413', .81, .70, .40, .59, .48),#4119
('Django Unchained 0413', .84, .91, .88, .85, .81),#316
('Edge Of Tomorrow 0413', .81, .90, .90, .84, .71),#348
('Fifty Shades Of Grey 0327', .36, .45, .25, .36, .46),#3854
('Fight Club 0413', .81, .96, .80,  .90, .66),#600
('Foxcatcher 0407', .62, .69, .88, .71, .81),#289
('Furious 7 0407', .92, .90, .83, .70, .67),#16600
('Focus 0327', .80, .58, .55, .61, .56),#5588
('Frozen 0413', .70, .86, .89, .77, .74),#5159
('Get Hard 0402', .75, .60, .29, .47, .34),#18000
('Gone Girl 0413', .66, .88, .88, .81, .79),#2258
('Gravity 0413', .47, .80, .97, .78, .96),#672
('Guardians Of The Galaxy 0413', .84, .93, .91, .85, .76),#1090
#('Home 0402', .84, .69, .47, .73, .55),#18000 Contaminated with too much unrelated stuff.
('Horrible Bosses 2 0408', .69, .50, .35, .63, .40),#422
('Interstellar 0406', .83, .86, .72, .84, .74), #11095
('Into The Woods 0408', .53, .52, .71, .61, .69),#1199
('It Follows 0327', .66, .67, .95, .72, .83),#5936
('John Wick 0408', .87, .80, .84, .78, .67),#1514
('Kingsman The Secret Service 0327', .83, .87, .74, .77, .58),#821
('Maleficent 0413', .87, .71, .49, .69, .56),#729
('Man Of Steel 0413', .61, .76, .55, .76, .55),#509
('McFarland USA 0327', .98, .92, .79, .67, .60),#398
('Nightcrawler 0413', .82, .86, .95, .83, .76),#655
#('Noah 0413', .57, .42, .77, .54, .68),#873 Name Noah causing too much crap
('Ouija 0408', .20, .27, .07, .52, .38),#506
('Paddington 0413', .88, .83, .98, .83, .77),#1739
('Pacific Rim 0413', .83, .77, .72, .75, .64),#334
('Run All Night 0327', .89, .64, .60, .76, .59),#1312
('Insurgent 0327', .77, .67, .31, .59, .42),#16600
('Song Of The Sea 0408', 1.0, .93, .98, .89, .85),#157
('St Vincent 0408', .89, .80, .77, .77, .64),#262
('The Big Lebowski 0413', .77, .94, .80, .88, .69),#282
('The Boy Next Door 0413', .60, .39, .11, .59, .30),#719
('The Cobbler 0327', .71, .40, .09, .49, .22),#295
('The Duff 0327', .75, .74, .67, .74, .56),#1720
('The Goonies 0413', .96, .91, .68, .78, .60),#165
('The Grand Budapest Hotel 0413', .97, .86, .92, .83, .88),#273
('The Gunman 0327', .55, .37, .13, .43, .39),#4771
('The Imitation Game 0406', .97, .92, .89, .82, .73),#1044
('The Interview 0408', .67, .50, .53, .61, .52),#3346
('The Lazarus Effect 0327', .50, .27, .14, .42, .31),#312
#('The Lego Movie 0413', .65, .87, .96, .82, .83),#8700 Contaminated with a lot of crap
('The Maze Runner 0413', .73, .69, .63, .68, .56),#2675
('The Theory Of Everything 0407', .90, .84, .79, .75, .72),#795
('The Voices 0413', .71, .60, .72, .76, .58),#787
('The Wedding Ringer 0413', .91, .73, .28, .44, .35),#689
('The Wolf Of Wall Street 0413', .89, .82, .77, .79, .75),#985
#('The Wolverine 0413', .64, .70, .69, .67, .60),#483
('Unbroken 0406', .90, .71, .51, .65, .59),#1758
('What We Do In The Shadows 0327', 1.0, .88, .96, .84, .75),#202
('Woman In Gold 0407', .88, .90, .49, .77, .52),#1357 MCUser is only 6 ratings
('World War Z 0413', .80, .72, .68, .68, .63),#381
('12 Years A Slave 0413', .75, .90, .96, .80, .97)#485
]

