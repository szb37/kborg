import os

src = os.path.dirname(os.path.abspath(__file__))
codebase = os.path.abspath(os.path.join(src, os.pardir))
kb = os.path.abspath(os.path.join(codebase, os.pardir, os.pardir))
vault_dir = os.path.abspath(os.path.join(kb, 'szb_vault'))
core_dir = os.path.abspath(os.path.join(vault_dir, 'Core'))
endeavor_dir = os.path.join(core_dir, 'Endeavors')
active_dir = os.path.join(endeavor_dir, 'Actives')
inactive_dir = os.path.join(endeavor_dir, 'Inactives')
