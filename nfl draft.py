# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 14:03:01 2022

@author: Eric Born
NFL fantasy draft
"""
import pandas as pd

# import player stats
file_path = r'C:/Users/Eric/Documents/GitHub/nfl_draft/data/'

# import stat files
pass_rush_df = pd.read_csv(file_path + 'pass_rush.csv')
defense_df = pd.read_csv(file_path + 'defense.csv')
kicking_df = pd.read_csv(file_path + 'kicking.csv')
point_scale_df = pd.read_csv(file_path + 'point_scale.csv')
other_stats_df = pd.read_csv(file_path + 'pbp-2021.csv')

# create a framework that allows weight by type of stat according to how
# many points it would generate

# offense
# player name, position, game id, points scored per category per game
# 
score_list = [pass_rush_df['player'], pass_rush_df['pos'], 
              pass_rush_df['game_id'],
              int(pass_rush_df['pass_yds'].div(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                               (point_scale_df['type'] == 'pass'), 'modifier'][0]))
              ]
pass_rush_df['pass_td'].mul(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                        (point_scale_df['type'] == 'pass_td'), 'points'][0])
pass_rush_df[''].mul(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                        (point_scale_df['type'] == ''), 'points'][0])
pass_rush_df[''].mul(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                        (point_scale_df['type'] == ''), 'points'][0])
pass_rush_df[''].mul(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                        (point_scale_df['type'] == ''), 'points'][0])
pass_rush_df[''].mul(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                        (point_scale_df['type'] == ''), 'points'][0])
pass_rush_df[''].mul(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                        (point_scale_df['type'] == ''), 'points'][0])
pass_rush_df[''].mul(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                        (point_scale_df['type'] == ''), 'modifier'][0])
pass_rush_df[''].mul(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                        (point_scale_df['type'] == ''), 'modifier'][0])
# calculate avg points scored per game, total season points

# filter data down to regular season games

# evaluate players point generation per position
# evaluate teams point generation per position
# determine if its better to choose a star player on a bad team or
# average player on a good team

# generate a mock draft list