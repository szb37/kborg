import os

src = os.path.dirname(os.path.abspath(__file__))
codebase = os.path.abspath(os.path.join(src, os.pardir))
kb = os.path.abspath(os.path.join(codebase, os.pardir, os.pardir))
dir_vault = os.path.abspath(os.path.join(kb, 'szb_vault'))
dir_core = os.path.abspath(os.path.join(dir_vault, 'Core'))
dir_project = os.path.join(dir_core, 'projects')

dir_life_active  = os.path.join(dir_project, 'Life', 'Active')
dir_work_active  = os.path.join(dir_project, 'Work', 'Active')
dir_life_dormant = os.path.join(dir_project, 'Life', 'Dormant')
dir_work_dormant = os.path.join(dir_project, 'Work', 'Dormant')
