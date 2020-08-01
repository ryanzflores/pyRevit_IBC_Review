"""Outputs allowable building height & number of stories
   above grade plane, and allowable area factor"""


# Note: data is formatted specifically to correspond as closely as
# possible to the tables in the IBC, making the values easy to modify or
# expand on for different/amended codes.

# Based on the 2018 IBC, Fourth Printing (Jan 2020)


# Table 504.3
def allowable_height(group, use, sprinkler, type):
    """ Takes an occupancy group, use, type, and sprinkler designation and outputs
        the allowable building height above the grade plane for that building."""

    group_i_check(group, use)

    height_table = \
        {'A,B,E,F,M,S,U':
             {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 160, 'II-A': 65,
                             'II-B': 55, 'III-A': 65, 'III-B': 55,
                             'IV-HT': 65, 'V-A': 50, 'V-B': 40},
                      'S': {'I-A': 'Unlimited', 'I-B': 180, 'II-A': 85,
                            'II-B': 75, 'III-A': 85, 'III-B': 75,
                            'IV-HT': 85, 'V-A': 70, 'V-B': 60}
                      }
              },
         'H': {
             '1,2,3,5':  ############################################################################################## Check group 'H'
                 {'NS':
                      {'I-A': 'Unlimited', 'I-B': 160, 'II-A': 65,
                       'II-B': 55, 'III-A': 65, 'III-B': 55,
                       'IV-HT': 65, 'V-A': 50, 'V-B': 40},
                  'S': {'I-A': 'Unlimited', 'I-B': 160, 'II-A': 65,
                        'II-B': 55, 'III-A': 65, 'III-B': 55,
                        'IV-HT': 65, 'V-A': 50, 'V-B': 40},
                  },
             '4': {'NS': {'I-A': 'Unlimited', 'I-B': 160, 'II-A': 65,
                          'II-B': 55, 'III-A': 65, 'III-B': 55,
                          'IV-HT': 65, 'V-A': 50, 'V-B': 40},
                   'S': {'I-A': 'Unlimited', 'I-B': 180, 'II-A': 85,
                         'II-B': 75, 'III-A': 85, 'III-B': 75,
                         'IV-HT': 85, 'V-A': 70, 'V-B': 60}
                   }
             },  ######################################################################################################
         'I': {'1 Condition 1,3':
                   {'NS': {'I-A': 'Unlimited', 'I-B': 160, 'II-A': 65,
                           'II-B': 55, 'III-A': 65, 'III-B': 55,
                           'IV-HT': 65, 'V-A': 50, 'V-B': 40},
                    'S': {'I-A': 'Unlimited', 'I-B': 180, 'II-A': 85,
                          'II-B': 75, 'III-A': 85, 'III-B': 75,
                          'IV-HT': 85, 'V-A': 70, 'V-B': 60}
                    },
               '1 Condition 2,2':
                   {'NS': {'I-A': 'Unlimited', 'I-B': 160, 'II-A': 65,
                           'II-B': 55, 'III-A': 65, 'III-B': 55,
                           'IV-HT': 65, 'V-A': 50, 'V-B': 40},
                    'S': {'I-A': 'Unlimited', 'I-B': 180, 'II-A': 85,
                          'II-B': 55, 'III-A': 65, 'III-B': 55,
                          'IV-HT': 65, 'V-A': 50, 'V-B': 40}
                    },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 160, 'II-A': 65,
                            'II-B': 55, 'III-A': 65, 'III-B': 55,
                            'IV-HT': 65, 'V-A': 50, 'V-B': 40},
                     'S': {'I-A': 'Unlimited', 'I-B': 180, 'II-A': 85,
                           'II-B': 75, 'III-A': 85, 'III-B': 75,
                           'IV-HT': 85, 'V-A': 70, 'V-B': 60}
                     }
               },
         'R': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 160, 'II-A': 65,
                              'II-B': 55, 'III-A': 65, 'III-B': 55,
                              'IV-HT': 65, 'V-A': 50, 'V-B': 40},
                       'S13D':
                           {'I-A': 60, 'I-B': 60, 'II-A': 60,
                            'II-B': 60, 'III-A': 60, 'III-B': 60,
                            'IV-HT': 60, 'V-A': 50, 'V-B': 40},
                       'S13R':
                           {'I-A': 60, 'I-B': 60, 'II-A': 60,
                            'II-B': 60, 'III-A': 60, 'III-B': 60,
                            'IV-HT': 60, 'V-A': 60, 'V-B': 60},
                       'S': {'I-A': 'Unlimited', 'I-B': 180, 'II-A': 85,
                             'II-B': 75, 'III-A': 85, 'III-B': 75,
                             'IV-HT': 85, 'V-A': 70, 'V-B': 60}
                       }
               }
         }

    return process_table(group, use, sprinkler, type, height_table)


# Table 504.4
def allowable_stories(group, use, sprinkler, type):
    """ Takes an occupancy group, use, type, and sprinkler designation and outputs
        the allowable number of stories above the grade plane for that building."""

    group_i_check(group, use)

    if sprinkler == 'S1' or sprinkler == 'SM':
        sprinkler = 'S'

    story_table = \
        {'A': {'1': {'NS': {'I-A': 'Unlimited', 'I-B': 5, 'II-A': 3, 'II-B': 2,
                            'III-A': 3, 'III-B': 2, 'IV-HT': 3,
                            'V-A': 2, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 6, 'II-A': 4, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                           'V-A': 3, 'V-B': 2}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 3, 'II-B': 2,
                            'III-A': 3, 'III-B': 2, 'IV-HT': 3,
                            'V-A': 2, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 4, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                           'V-A': 3, 'V-B': 2}
                     },
               '3': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 3, 'II-B': 2,
                            'III-A': 3, 'III-B': 2, 'IV-HT': 3,
                            'V-A': 2, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 4, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                           'V-A': 3, 'V-B': 2}
                     },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 3, 'II-B': 2,
                            'III-A': 3, 'III-B': 2, 'IV-HT': 3,
                            'V-A': 2, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 4, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                           'V-A': 3, 'V-B': 2}
                     },
               '5': {'NS': {'ANY': 'Unlimited'},
                     'S': {'ANY': 'Unlimited'}
                     }
               },
         'B': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 5, 'II-B': 3,
                              'III-A': 5, 'III-B': 3, 'IV-HT': 5,
                              'V-A': 3, 'V-B': 2},
                       'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 6, 'II-B': 4,
                             'III-A': 6, 'III-B': 4, 'IV-HT': 6,
                             'V-A': 4, 'V-B': 3}
                       }
               },
         'E': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 5, 'II-A': 3, 'II-B': 2,
                              'III-A': 3, 'III-B': 2, 'IV-HT': 3,
                              'V-A': 1, 'V-B': 1},
                       'S': {'I-A': 'Unlimited', 'I-B': 6, 'II-A': 4, 'II-B': 3,
                             'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                             'V-A': 2, 'V-B': 2}
                       }
               },
         'F': {'1': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 4, 'II-B': 2,
                            'III-A': 3, 'III-B': 2, 'IV-HT': 4,
                            'V-A': 2, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 5, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 5,
                           'V-A': 3, 'V-B': 2}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 5, 'II-B': 3,
                            'III-A': 4, 'III-B': 3, 'IV-HT': 5,
                            'V-A': 3, 'V-B': 2},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 6, 'II-B': 4,
                           'III-A': 5, 'III-B': 4, 'IV-HT': 6,
                           'V-A': 5, 'V-B': 3}
                     }
               },
         'H': {'1': {'NS': {'I-A': 1, 'I-B': 1, 'II-A': 1, 'II-B': 1,
                            'III-A': 1, 'III-B': 1, 'IV-HT': 1,
                            'V-A': 1, 'V-B': 'NP'},
                     'S': {'I-A': 1, 'I-B': 1, 'II-A': 1, 'II-B': 1,
                           'III-A': 1, 'III-B': 1, 'IV-HT': 1,
                           'V-A': 1, 'V-B': 'NP'}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 3, 'II-A': 2, 'II-B': 1,
                            'III-A': 2, 'III-B': 1, 'IV-HT': 2,
                            'V-A': 1, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 3, 'II-A': 2, 'II-B': 1,
                           'III-A': 2, 'III-B': 1, 'IV-HT': 2,
                           'V-A': 1, 'V-B': 1}
                     },
               '3': {'NS': {'I-A': 'Unlimited', 'I-B': 6, 'II-A': 4, 'II-B': 2,
                            'III-A': 4, 'III-B': 2, 'IV-HT': 4,
                            'V-A': 2, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 6, 'II-A': 4, 'II-B': 2,
                           'III-A': 4, 'III-B': 2, 'IV-HT': 4,
                           'V-A': 2, 'V-B': 1}
                     },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 7, 'II-A': 5, 'II-B': 3,
                            'III-A': 5, 'III-B': 3, 'IV-HT': 5,
                            'V-A': 3, 'V-B': 2},
                     'S': {'I-A': 'Unlimited', 'I-B': 8, 'II-A': 6, 'II-B': 4,
                           'III-A': 6, 'III-B': 4, 'IV-HT': 6,
                           'V-A': 4, 'V-B': 3}
                     },
               '5': {'NS': {'I-A': 4, 'I-B': 4, 'II-A': 3, 'II-B': 3,
                            'III-A': 3, 'III-B': 3, 'IV-HT': 3,
                            'V-A': 3, 'V-B': 2},
                     'S': {'I-A': 4, 'I-B': 4, 'II-A': 3, 'II-B': 3,
                           'III-A': 3, 'III-B': 3, 'IV-HT': 3,
                           'V-A': 3, 'V-B': 2}
                     }
               },
         'I': {'1 Condition 1':
                   {'NS': {'I-A': 'Unlimited', 'I-B': 9, 'II-A': 4, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                           'V-A': 3, 'V-B': 2},
                    'S': {'I-A': 'Unlimited', 'I-B': 10, 'II-A': 5, 'II-B': 4,
                          'III-A': 5, 'III-B': 4, 'IV-HT': 5,
                          'V-A': 4, 'V-B': 3}
                    },
               '1 Condition 2':
                   {'NS': {'I-A': 'Unlimited', 'I-B': 9, 'II-A': 4, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                           'V-A': 3, 'V-B': 2},
                    'S': {'I-A': 'Unlimited', 'I-B': 10, 'II-A': 5, 'II-B': 3,
                          'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                          'V-A': 3, 'V-B': 2}
                    },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 4, 'II-A': 2, 'II-B': 1,
                            'III-A': 1, 'III-B': 'NP', 'IV-HT': 1,
                            'V-A': 1, 'V-B': 'NP'},
                     'S': {'I-A': 'Unlimited', 'I-B': 5, 'II-A': 3, 'II-B': 1,
                           'III-A': 1, 'III-B': 'NP', 'IV-HT': 1,
                           'V-A': 1, 'V-B': 'NP'}
                     },
               '3': {'NS': {'I-A': 'Unlimited', 'I-B': 4, 'II-A': 2, 'II-B': 1,
                            'III-A': 2, 'III-B': 1, 'IV-HT': 2,
                            'V-A': 2, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 5, 'II-A': 3, 'II-B': 2,
                           'III-A': 3, 'III-B': 2, 'IV-HT': 3,
                           'V-A': 3, 'V-B': 2}
                     },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 5, 'II-A': 3, 'II-B': 2,
                            'III-A': 3, 'III-B': 2, 'IV-HT': 3,
                            'V-A': 1, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 6, 'II-A': 4, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                           'V-A': 2, 'V-B': 2}
                     }
               },
         'M': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 4, 'II-B': 2,
                              'III-A': 4, 'III-B': 2, 'IV-HT': 4,
                              'V-A': 3, 'V-B': 1},
                       'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 5, 'II-B': 3,
                             'III-A': 5, 'III-B': 3, 'IV-HT': 5,
                             'V-A': 4, 'V-B': 2}
                       }
               },
         'R': {'1': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 4, 'II-B': 4,
                            'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                            'V-A': 3, 'V-B': 2},
                     'S13R': {'I-A': 4, 'I-B': 4, 'II-A': 4, 'II-B': 4,
                              'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                              'V-A': 4, 'V-B': 3},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 5, 'II-B': 5,
                           'III-A': 5, 'III-B': 5, 'IV-HT': 5,
                           'V-A': 4, 'V-B': 3}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 4, 'II-B': 4,
                            'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                            'V-A': 3, 'V-B': 2},
                     'S13R': {'I-A': 4, 'I-B': 4, 'II-A': 4, 'II-B': 4,
                              'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                              'V-A': 4, 'V-B': 3},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 5, 'II-B': 5,
                           'III-A': 5, 'III-B': 5, 'IV-HT': 5,
                           'V-A': 4, 'V-B': 3}
                     },
               '3': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 4, 'II-B': 4,
                            'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                            'V-A': 3, 'V-B': 3},
                     'S13D': {'I-A': 4, 'I-B': 4, 'II-A': 4, 'II-B': 4,
                              'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                              'V-A': 3, 'V-B': 3},
                     'S13R': {'I-A': 4, 'I-B': 4, 'II-A': 4, 'II-B': 4,
                              'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                              'V-A': 4, 'V-B': 4},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 5, 'II-B': 5,
                           'III-A': 5, 'III-B': 5, 'IV-HT': 5,
                           'V-A': 4, 'V-B': 4}
                     },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 4, 'II-B': 4,
                            'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                            'V-A': 3, 'V-B': 2},
                     'S13D': {'I-A': 4, 'I-B': 4, 'II-A': 4, 'II-B': 4,
                              'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                              'V-A': 3, 'V-B': 2},
                     'S13R': {'I-A': 4, 'I-B': 4, 'II-A': 4, 'II-B': 4,
                              'III-A': 4, 'III-B': 4, 'IV-HT': 4,
                              'V-A': 4, 'V-B': 3},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 5, 'II-B': 5,
                           'III-A': 5, 'III-B': 5, 'IV-HT': 5,
                           'V-A': 4, 'V-B': 3}
                     }
               },
         'S': {'1': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 4, 'II-B': 2,
                            'III-A': 3, 'III-B': 2, 'IV-HT': 4,
                            'V-A': 3, 'V-B': 1},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 5, 'II-B': 3,
                           'III-A': 4, 'III-B': 3, 'IV-HT': 5,
                           'V-A': 4, 'V-B': 2}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 11, 'II-A': 5, 'II-B': 3,
                            'III-A': 4, 'III-B': 3, 'IV-HT': 4,
                            'V-A': 4, 'V-B': 2},
                     'S': {'I-A': 'Unlimited', 'I-B': 12, 'II-A': 6, 'II-B': 4,
                           'III-A': 5, 'III-B': 4, 'IV-HT': 5,
                           'V-A': 5, 'V-B': 3}
                     }
               },
         'U': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 5, 'II-A': 4, 'II-B': 2,
                              'III-A': 3, 'III-B': 2, 'IV-HT': 4,
                              'V-A': 2, 'V-B': 1},
                       'S': {'I-A': 'Unlimited', 'I-B': 6, 'II-A': 5, 'II-B': 3,
                             'III-A': 4, 'III-B': 3, 'IV-HT': 5,
                             'V-A': 3, 'V-B': 2}
                       }
               }
         }

    return process_table(group, use, sprinkler, type, story_table)


# Table 506.2
def allowable_area(group, use, sprinkler, type):
    """ Takes an occupancy group, use, type, and sprinkler designation and outputs
        the allowable area (in square feet) for that building."""

    # I-1 Condition 1 and I-1 Condition 2 treated the same
    if use == '1 Condition 1' or use == '1 Condition 2':
        use = '1'

    if group == 'R' and sprinkler == 'S':
        if type == '1' or type == '2':
            raise ValueError("Invalid input: group R-1 and R-2 must have sprinklers 'NS', 'S13R', "
                             "'S1', or 'SM'")
        else:
            raise ValueError("Invalid input: group R-3 and R-4 must have sprinklers 'NS', 'S13D', "
                             "'S13R', 'S1', or 'SM'")

    group_i_check(group, use)
    #####################################################################
    area_table = \
        {'A': {'1': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 15500, 'II-B': 8500,
                            'III-A': 14000, 'III-B': 8500, 'IV-HT': 15000,
                            'V-A': 11500, 'V-B': 5500},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 62000, 'II-B': 34000,
                            'III-A': 56000, 'III-B': 34000, 'IV-HT': 60000,
                            'V-A': 46000, 'V-B': 22000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 46500, 'II-B': 25500,
                            'III-A': 42000, 'III-B': 25500, 'IV-HT': 45000,
                            'V-A': 34500, 'V-B': 16500}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 15500, 'II-B': 9500,
                            'III-A': 14000, 'III-B': 9500, 'IV-HT': 15000,
                            'V-A': 11500, 'V-B': 6000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 62000, 'II-B': 38000,
                            'III-A': 56000, 'III-B': 38000, 'IV-HT': 60000,
                            'V-A': 46000, 'V-B': 24000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 46500, 'II-B': 28500,
                            'III-A': 42000, 'III-B': 28500, 'IV-HT': 45000,
                            'V-A': 34500, 'V-B': 18000}
                     },
               '3': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 15500, 'II-B': 9500,
                            'III-A': 14000, 'III-B': 9500, 'IV-HT': 15000,
                            'V-A': 11500, 'V-B': 6000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 62000, 'II-B': 38000,
                            'III-A': 56000, 'III-B': 38000, 'IV-HT': 60000,
                            'V-A': 46000, 'V-B': 24000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 46500, 'II-B': 28500,
                            'III-A': 42000, 'III-B': 28500, 'IV-HT': 45000,
                            'V-A': 34500, 'V-B': 18000}
                     },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 15500, 'II-B': 9500,
                            'III-A': 14000, 'III-B': 9500, 'IV-HT': 15000,
                            'V-A': 11500, 'V-B': 6000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 62000, 'II-B': 38000,
                            'III-A': 56000, 'III-B': 38000, 'IV-HT': 60000,
                            'V-A': 46000, 'V-B': 24000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 46500, 'II-B': 28500,
                            'III-A': 42000, 'III-B': 28500, 'IV-HT': 45000,
                            'V-A': 34500, 'V-B': 18000}
                     },
               '5': {'NS': {'ANY': 'Unlimited'},
                     'S1': {'ANY': 'Unlimited'},
                     'SM': {'ANY': 'Unlimited'}
                     }
               },
         'B': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 37500, 'II-B': 23000,
                              'III-A': 28500, 'III-B': 19000, 'IV-HT': 36000,
                              'V-A': 18000, 'V-B': 9000},
                       'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 150000, 'II-B': 92000,
                              'III-A': 114000, 'III-B': 76000, 'IV-HT': 144000,
                              'V-A': 72000, 'V-B': 36000},
                       'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 112500, 'II-B': 69000,
                              'III-A': 85500, 'III-B': 57000, 'IV-HT': 108000,
                              'V-A': 54000, 'V-B': 27000}
                       },
               },
         'E': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 26500, 'II-B': 14500,
                              'III-A': 23500, 'III-B': 14500, 'IV-HT': 25500,
                              'V-A': 18500, 'V-B': 9500},
                       'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 106000, 'II-B': 58000,
                              'III-A': 94000, 'III-B': 58000, 'IV-HT': 102000,
                              'V-A': 74000, 'V-B': 38000},
                       'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 79500, 'II-B': 43500,
                              'III-A': 70500, 'III-B': 43500, 'IV-HT': 76500,
                              'V-A': 55500, 'V-B': 285000}
                       },
               },
         'F': {'1': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 25000, 'II-B': 15500,
                            'III-A': 19000, 'III-B': 12000, 'IV-HT': 33500,
                            'V-A': 14000, 'V-B': 8500},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 100000, 'II-B': 62000,
                            'III-A': 76000, 'III-B': 48000, 'IV-HT': 134000,
                            'V-A': 56000, 'V-B': 34000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 75000, 'II-B': 46500,
                            'III-A': 57000, 'III-B': 36000, 'IV-HT': 100500,
                            'V-A': 42000, 'V-B': 25500000}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 37500, 'II-B': 23000,
                            'III-A': 28500, 'III-B': 18000, 'IV-HT': 50500,
                            'V-A': 21000, 'V-B': 13000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 150000, 'II-B': 92000,
                            'III-A': 114000, 'III-B': 72000, 'IV-HT': 202000,
                            'V-A': 84000, 'V-B': 52000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 112500, 'II-B': 69000,
                            'III-A': 85500, 'III-B': 54000, 'IV-HT': 151500,
                            'V-A': 63000, 'V-B': 39000}
                     },
               },
         'H': {'1': {'NS': {'I-A': 21000, 'I-B': 16500, 'II-A': 11000, 'II-B': 7000,
                            'III-A': 9500, 'III-B': 7000, 'IV-HT': 10500,
                            'V-A': 7500, 'V-B': 'NP'},
                     'S1': {'I-A': 21000, 'I-B': 16500, 'II-A': 11000, 'II-B': 7000,
                            'III-A': 9500, 'III-B': 7000, 'IV-HT': 10500,
                            'V-A': 7500, 'V-B': 'NP'}
                     },
               '2': {'NS': {'I-A': 21000, 'I-B': 16500, 'II-A': 11000, 'II-B': 7000,
                            'III-A': 9500, 'III-B': 7000, 'IV-HT': 10500,
                            'V-A': 7500, 'V-B': 3000},
                     'S1': {'I-A': 21000, 'I-B': 16500, 'II-A': 11000, 'II-B': 7000,
                            'III-A': 9500, 'III-B': 7000, 'IV-HT': 10500,
                            'V-A': 7500, 'V-B': 3000},
                     'SM': {'I-A': 21000, 'I-B': 16500, 'II-A': 11000, 'II-B': 7000,
                            'III-A': 9500, 'III-B': 7000, 'IV-HT': 10500,
                            'V-A': 7500, 'V-B': 3000}
                     },
               '3': {'NS': {'I-A': 'Unlimited', 'I-B': 60000, 'II-A': 26500, 'II-B': 14000,
                            'III-A': 17500, 'III-B': 13000, 'IV-HT': 25500,
                            'V-A': 10000, 'V-B': 5000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 60000, 'II-A': 26500, 'II-B': 14000,
                            'III-A': 17500, 'III-B': 13000, 'IV-HT': 25500,
                            'V-A': 10000, 'V-B': 5000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 60000, 'II-A': 26500, 'II-B': 14000,
                            'III-A': 17500, 'III-B': 13000, 'IV-HT': 25500,
                            'V-A': 10000, 'V-B': 5000}
                     },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 37500, 'II-B': 17500,
                            'III-A': 28500, 'III-B': 17500, 'IV-HT': 36000,
                            'V-A': 18000, 'V-B': 6500},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 150000, 'II-B': 70000,
                            'III-A': 114000, 'III-B': 70000, 'IV-HT': 144000,
                            'V-A': 72000, 'V-B': 26000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 112500, 'II-B': 52500,
                            'III-A': 85500, 'III-B': 52500, 'IV-HT': 108000,
                            'V-A': 54000, 'V-B': 19500}
                     },
               '5': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 37500, 'II-B': 23000,
                            'III-A': 28500, 'III-B': 19000, 'IV-HT': 36000,
                            'V-A': 18000, 'V-B': 9000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 150000, 'II-B': 92000,
                            'III-A': 114000, 'III-B': 76000, 'IV-HT': 144000,
                            'V-A': 72000, 'V-B': 36000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 1125000, 'II-B': 69000,
                            'III-A': 85500, 'III-B': 57000, 'IV-HT': 108000,
                            'V-A': 54000, 'V-B': 27000}
                     }
               },
         'I': {'1':  # 1 Condition 1 and 1 Condition 2 are translated to '1'
                   {'NS': {'I-A': 'Unlimited', 'I-B': 55000, 'II-A': 19000, 'II-B': 10000,
                           'III-A': 165000, 'III-B': 10000, 'IV-HT': 18000,
                           'V-A': 10500, 'V-B': 4500},
                    'S1': {'I-A': 'Unlimited', 'I-B': 220000, 'II-A': 76000, 'II-B': 40000,
                           'III-A': 66000, 'III-B': 40000, 'IV-HT': 72000,
                           'V-A': 42000, 'V-B': 18000},
                    'SM': {'I-A': 'Unlimited', 'I-B': 165000, 'II-A': 57000, 'II-B': 30000,
                           'III-A': 49500, 'III-B': 30000, 'IV-HT': 54000,
                           'V-A': 31500, 'V-B': 13500}
                    },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 15000, 'II-B': 11000,
                            'III-A': 12000, 'III-B': 'NP', 'IV-HT': 12000,
                            'V-A': 9500, 'V-B': 'NP'},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 60000, 'II-B': 44000,
                            'III-A': 48000, 'III-B': 'NP', 'IV-HT': 48000,
                            'V-A': 38000, 'V-B': 'NP'},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 45000, 'II-B': 33000,
                            'III-A': 36000, 'III-B': 'NP', 'IV-HT': 48000,
                            'V-A': 38000, 'V-B': 'NP'}
                     },
               '3': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 15000, 'II-B': 10000,
                            'III-A': 10500, 'III-B': 75000, 'IV-HT': 12000,
                            'V-A': 7500, 'V-B': 5000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 45000, 'II-B': 40000,
                            'III-A': 42000, 'III-B': 30000, 'IV-HT': 48000,
                            'V-A': 30000, 'V-B': 20000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 45000, 'II-B': 30000,
                            'III-A': 31500, 'III-B': 22500, 'IV-HT': 36000,
                            'V-A': 22500, 'V-B': 15000}
                     },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 60500, 'II-A': 26500, 'II-B': 13000,
                            'III-A': 23500, 'III-B': 13000, 'IV-HT': 25500,
                            'V-A': 18500, 'V-B': 9000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 121000, 'II-A': 106000, 'II-B': 52000,
                            'III-A': 94000, 'III-B': 52000, 'IV-HT': 102000,
                            'V-A': 74000, 'V-B': 36000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 181500, 'II-A': 79500, 'II-B': 39000,
                            'III-A': 70500, 'III-B': 39000, 'IV-HT': 76500,
                            'V-A': 55500, 'V-B': 27000}
                     }
               },
         'M': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 21500, 'II-B': 12500,
                              'III-A': 18500, 'III-B': 12500, 'IV-HT': 20500,
                              'V-A': 14000, 'V-B': 9000},
                       'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 86000, 'II-B': 50000,
                              'III-A': 74000, 'III-B': 50000, 'IV-HT': 82000,
                              'V-A': 56000, 'V-B': 36000},
                       'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 64500, 'II-B': 37500,
                              'III-A': 55500, 'III-B': 37500, 'IV-HT': 61500,
                              'V-A': 42000, 'V-B': 27000}
                       }
               },
         'R': {'1': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 24000, 'II-B': 16000,
                            'III-A': 24000, 'III-B': 16000, 'IV-HT': 20500,
                            'V-A': 12000, 'V-B': 7000},
                     'S13R': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 24000, 'II-B': 16000,
                              'III-A': 24000, 'III-B': 16000, 'IV-HT': 20500,
                              'V-A': 12000, 'V-B': 7000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 96000, 'II-B': 64000,
                            'III-A': 96000, 'III-B': 64000, 'IV-HT': 82000,
                            'V-A': 48000, 'V-B': 28000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 72000, 'II-B': 48000,
                            'III-A': 72000, 'III-B': 48000, 'IV-HT': 61500,
                            'V-A': 36000, 'V-B': 21000}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 72000, 'II-B': 48000,
                            'III-A': 72000, 'III-B': 48000, 'IV-HT': 61500,
                            'V-A': 36000, 'V-B': 21000},
                     'S13R': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 24000, 'II-B': 16000,
                              'III-A': 24000, 'III-B': 16000, 'IV-HT': 20500,
                              'V-A': 12000, 'V-B': 7000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 96000, 'II-B': 64000,
                            'III-A': 96000, 'III-B': 64000, 'IV-HT': 82000,
                            'V-A': 48000, 'V-B': 28000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 72000, 'II-B': 48000,
                            'III-A': 72000, 'III-B': 48000, 'IV-HT': 61500,
                            'V-A': 36000, 'V-B': 21000}
                     },
               '3': {'NS': {'ANY': 'Unlimited'},
                     'S13D': {'ANY': 'Unlimited'},
                     'S13R': {'ANY': 'Unlimited'},
                     'S1': {'ANY': 'Unlimited'},
                     'SM': {'ANY': 'Unlimited'}
                     },
               '4': {'NS': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 24000, 'II-B': 16000,
                            'III-A': 24000, 'III-B': 16000, 'IV-HT': 205000,
                            'V-A': 12000, 'V-B': 7000},
                     'S13D': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 24000, 'II-B': 16000,
                              'III-A': 24000, 'III-B': 16000, 'IV-HT': 205000,
                              'V-A': 12000, 'V-B': 7000},
                     'S13R': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 24000, 'II-B': 16000,
                              'III-A': 24000, 'III-B': 16000, 'IV-HT': 205000,
                              'V-A': 12000, 'V-B': 7000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 96000, 'II-B': 64000,
                            'III-A': 96000, 'III-B': 64000, 'IV-HT': 82000,
                            'V-A': 48000, 'V-B': 28000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 'Unlimited', 'II-A': 72000, 'II-B': 48000,
                            'III-A': 72000, 'III-B': 48000, 'IV-HT': 61500,
                            'V-A': 36000, 'V-B': 21000}
                     }
               },
         'S': {'1': {'NS': {'I-A': 'Unlimited', 'I-B': 48000, 'II-A': 26000, 'II-B': 17500,
                            'III-A': 26000, 'III-B': 17500, 'IV-HT': 25500,
                            'V-A': 14000, 'V-B': 9000},
                     'S1': {'I-A': 'Unlimited', 'I-B': 192000, 'II-A': 104000, 'II-B': 70000,
                            'III-A': 104000, 'III-B': 70000, 'IV-HT': 102000,
                            'V-A': 56000, 'V-B': 36000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 144000, 'II-A': 78000, 'II-B': 52500,
                            'III-A': 78000, 'III-B': 52500, 'IV-HT': 76500,
                            'V-A': 42000, 'V-B': 27000}
                     },
               '2': {'NS': {'I-A': 'Unlimited', 'I-B': 79000, 'II-A': 39000, 'II-B': 26000,
                            'III-A': 39000, 'III-B': 26000, 'IV-HT': 38500,
                            'V-A': 21000, 'V-B': 13500},
                     'S1': {'I-A': 'Unlimited', 'I-B': 316000, 'II-A': 156000, 'II-B': 104000,
                            'III-A': 156000, 'III-B': 104000, 'IV-HT': 154000,
                            'V-A': 84000, 'V-B': 54000},
                     'SM': {'I-A': 'Unlimited', 'I-B': 237000, 'II-A': 117000, 'II-B': 78000,
                            'III-A': 117000, 'III-B': 78000, 'IV-HT': 115500,
                            'V-A': 63000, 'V-B': 40500}
                     }
               },
         'U': {'ANY': {'NS': {'I-A': 'Unlimited', 'I-B': 35500, 'II-A': 19000, 'II-B': 8500,
                              'III-A': 14000, 'III-B': 8500, 'IV-HT': 18000,
                              'V-A': 9000, 'V-B': 5500},
                       'S1': {'I-A': 'Unlimited', 'I-B': 142000, 'II-A': 76000, 'II-B': 34000,
                              'III-A': 56000, 'III-B': 34000, 'IV-HT': 72000,
                              'V-A': 36000, 'V-B': 22000},
                       'SM': {'I-A': 'Unlimited', 'I-B': 106500, 'II-A': 57000, 'II-B': 25500,
                              'III-A': 42000, 'III-B': 25500, 'IV-HT': 54000,
                              'V-A': 27000, 'V-B': 16500}
                       }
               }
         }

    return process_table(group, use, sprinkler, type, area_table)


def group_i_check(group, use):
    if group == 'I' and use == '1':
        raise ValueError("Invalid input: group I must have uses '1_Condition_1', "
                         "'1_Condition_2', 2, or 3")


def process_table(group, use, sprinkler, type, table):
    table_groups = table.keys()
    for table_group in table_groups:
        if group in table_group or table_group == 'ANY':

            table_uses = table[table_group].keys()
            for table_use in table_uses:
                # Use '1' is in '1 Condition 1/2', but each table calls group_I_check at start
                if use in table_use or table_use == 'ANY':

                    table_sprinklers = table[table_group][table_use].keys()
                    for table_sprinkler in table_sprinklers:
                        # Cannot use "in" due to 'S' being in 'NS' (and 'S13D' and 'S13R')
                        if sprinkler == table_sprinkler or table_sprinkler == 'ANY':

                            table_types = \
                                table[table_group][table_use][table_sprinkler].keys()
                            for table_type in table_types:
                                if type in table_type or table_type == 'ANY':
                                    return \
                                        table[table_group][table_use][table_sprinkler][table_type]

                            raise ValueError("group, use, & sprinkler found, but type not found!")

                    raise ValueError("group & use found, but sprinkler not found!")

            raise ValueError("group found, but use not found!")

    raise ValueError("group not found!")
