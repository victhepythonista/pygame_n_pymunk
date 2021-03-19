import cx_Freeze

executable  = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name = 'cross the road',
    options = {
        'build_exe':{'packages':['pygame'] ,
                     'include_files':['characters/squirell_facing_right.png',
                                      'characters/squirell_facing_left.png' ,
                                      'acorns/choconut.png',
                                      'draw_roads.py',
                                      'backend.py'
                                      ]}},
    executables = executable
)
