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
offensive_score_list = [pass_rush_df['player'], pass_rush_df['pos'], 
                        pass_rush_df['game_id'],
                        pass_rush_df['pass_yds'].div(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                        (point_scale_df['type'] == 'pass'), 'modifier'][0]),
                        pass_rush_df['pass_td']*(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                     (point_scale_df['type'] == 'pass_td'), 'points']).values,
                        pass_rush_df['pass_int']*(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                     (point_scale_df['type'] == 'int'), 'points']).values,
                        pass_rush_df['rush_yds'].div(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                        (point_scale_df['type'] == 'rush'), 'modifier'].values[0]),
                        pass_rush_df['rush_td']*(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                    (point_scale_df['type'] == 'rush_td'), 'points']).values,
                        pass_rush_df['rec']*(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                (point_scale_df['type'] == 'reception'), 'points']).values,
                        pass_rush_df['rec_yds'].div(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                       (point_scale_df['type'] == 'receive_yards'), 'modifier'].values[0]),
                        pass_rush_df['rec_td']*(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                   (point_scale_df['type'] == 'receive_td'), 'points']).values,
                        pass_rush_df['two_point_conv']*(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                           (point_scale_df['type'] == 'two_point'), 'points']).values,
                        pass_rush_df['fumbles_lost']*(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                         (point_scale_df['type'] == 'fumble_lost'), 'points']).values,
                        pass_rush_df['offensive_fumble_recovery_td']*(point_scale_df.loc[(point_scale_df['category'] == 'offense') & 
                                                                                         (point_scale_df['type'] == 'fumble_td'), 'points']).values]
# TODO
# creating columns as rows and vice versa, need to flip
score_df = pd.DataFrame(offensive_score_list)
# pd.melt(score_df, id_vars = ['player', 'pos', 'game_id', 'pass_yds', 'pass_td', 
#                          'pass_int', 'rush_yds', 'rush_td', 'rec', 'rec_yds',
#                          'rec_td', 'two_point_conv', 'fumbles_lost',
#                          'offensive_fumble_recovery_td'])

# calculate avg points scored per game, total season points

# filter data down to regular season games

# evaluate players point generation per position
# evaluate teams point generation per position
# determine if its better to choose a star player on a bad team or
# average player on a good team

# generate a mock draft list