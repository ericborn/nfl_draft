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
# TODO 
# need to check data for only regular season games
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
# set the name of each series
offensive_score_list[0].name = 'player'
offensive_score_list[1].name = 'pos'
offensive_score_list[2].name = 'game_id'
offensive_score_list[3].name = 'pass_yds'
offensive_score_list[4].name = 'pass_td'
offensive_score_list[5].name = 'pass_int'
offensive_score_list[6].name = 'rush_yds'
offensive_score_list[7].name = 'rush_td'
offensive_score_list[8].name = 'rec'
offensive_score_list[9].name = 'rec_yds'
offensive_score_list[10].name = 'rec_td'
offensive_score_list[11].name = 'two_point_conv'
offensive_score_list[12].name = 'fumbles_lost'
offensive_score_list[13].name = 'offensive_fumble_recovery_td'

# concat all series into a dataframe
score_df = pd.concat([offensive_score_list[0],offensive_score_list[1],
           offensive_score_list[2],offensive_score_list[3],
           offensive_score_list[4],offensive_score_list[5],
           offensive_score_list[6],offensive_score_list[7],
           offensive_score_list[8],offensive_score_list[9],
           offensive_score_list[10],offensive_score_list[11],
           offensive_score_list[12],offensive_score_list[13]], axis=1)

# calculate avg points scored per game and total season points
# need to add adjusted average based on games played
# should track if injured or other cause of games missed
calc_score_list = [score_df.groupby('player').pass_yds.mean(),
                   score_df.groupby('player').pass_yds.sum(),
                   score_df.groupby('player').pass_td.mean(),
                   score_df.groupby('player').pass_td.sum(),
                   score_df.groupby('player').pass_int.mean(),
                   score_df.groupby('player').pass_int.sum(),
                   score_df.groupby('player').rush_yds.mean(),
                   score_df.groupby('player').rush_yds.sum(),
                   score_df.groupby('player').rush_td.mean(),
                   score_df.groupby('player').rush_td.sum(),
                   score_df.groupby('player').rec.mean(),
                   score_df.groupby('player').rec.sum(),
                   score_df.groupby('player').rec_yds.mean(),
                   score_df.groupby('player').rec_yds.sum(),
                   score_df.groupby('player').rec_td.mean(),
                   score_df.groupby('player').rec_td.sum(),
                   score_df.groupby('player').two_point_conv.mean(),
                   score_df.groupby('player').two_point_conv.sum(),
                   score_df.groupby('player').fumbles_lost.mean(),
                   score_df.groupby('player').fumbles_lost.sum(),
                   score_df.groupby('player').offensive_fumble_recovery_td.mean(),
                   score_df.groupby('player').offensive_fumble_recovery_td.sum()]

# convert series data to dataframe with index as the players name
calc_score_df = pd.concat([calc_score_list[0],calc_score_list[1],
                            calc_score_list[2],calc_score_list[3],
                            calc_score_list[4],calc_score_list[5],
                            calc_score_list[6],calc_score_list[7],
                            calc_score_list[8],calc_score_list[9],
                            calc_score_list[10],calc_score_list[11],
                            calc_score_list[12],calc_score_list[13],
                            calc_score_list[14],calc_score_list[15],
                            calc_score_list[16],calc_score_list[17],
                            calc_score_list[18],calc_score_list[19],
                            calc_score_list[20],calc_score_list[21]], axis = 1)


# evaluate players point generation per position
# evaluate teams point generation per position
# determine if its better to choose a star player on a bad team or
# average player on a good team

# generate a mock draft list