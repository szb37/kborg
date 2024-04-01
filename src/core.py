import src.folders as folders
import shutil
import os

class Controllers:

    def move_projects():

        for filepath in Helpers.find_md_files(folders.dir_core):

            if 'Template' in filepath:
                continue

            with open(filepath, 'r', encoding='utf-8') as file:

                note = file.read()
                if (Helpers.is_project(note) is False):
                    continue

                is_active = Helpers.is_active(note)
                is_dormant = Helpers.is_dormant(note)
                status = Helpers.assign_status(is_active, is_dormant)
                assert status in ['active', 'dormant', 'undecided']

                is_life = Helpers.is_life(note)
                is_work = Helpers.is_work(note)
                domain = Helpers.assign_domain(is_life, is_work)
                assert domain in ['life', 'work', 'undecided']

            ### Move notes
            if (domain=='life') and (status=='active'):
                Helpers.move_file(filepath, folders.dir_life_active)
            elif (domain=='life') and (status=='dormant'):
                Helpers.move_file(filepath, folders.dir_life_dormant)
            elif (domain=='work') and (status=='active'):
                Helpers.move_file(filepath, folders.dir_work_active)
            elif (domain=='work') and (status=='dormant'):
                Helpers.move_file(filepath, folders.dir_work_dormant)
            else:
                Helpers.move_file(filepath, folders.dir_project)
                print(f'Undecided project: {os.path.basename(filepath)}; domain:{domain}, status:{status}')


class Helpers():

    @staticmethod
    def find_md_files(directory):
        md_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    md_files.append(os.path.join(root, file))

        return md_files

    @staticmethod
    def is_project(note):
        return ('\ntype: project' in note)

    @staticmethod
    def is_active(note):
         return ('\nstate: 💼' in note)

    @staticmethod
    def is_dormant(note):
         is_dormant1 = ('\nstate: 🌱' in note)
         is_dormant2 = ('\nstate: 💤' in note)
         is_dormant3 = ('\nstate: 🗂️' in note)
         return (is_dormant1 or is_dormant2 or is_dormant3)

    @staticmethod
    def is_life(note):
         return ('\ndomain: 👨‍👩‍👧‍👧' in note)

    @staticmethod
    def is_work(note):
        return ('\ndomain: 💼' in note)

    @staticmethod
    def assign_status(is_active, is_dormant):

        assert isinstance(is_active, bool)
        assert isinstance(is_dormant, bool)

        if (is_active is True) and (is_dormant is False):
            return 'active'
        elif (is_active is False) and (is_dormant is True):
            return 'dormant'
        else:
            return 'undecided'

    @staticmethod
    def assign_domain(is_life, is_work):

        assert isinstance(is_life, bool)
        assert isinstance(is_work, bool)

        if (is_life is True) and (is_work is False):
            return 'life'
        elif (is_life is False) and (is_work is True):
            return 'work'
        else:
            return 'undecided'

    @staticmethod
    def move_file(filepath, destination_dir):

        if os.path.isfile(os.path.join(destination_dir, os.path.basename(filepath))):
            return

        try:
            shutil.move(filepath, destination_dir)
        except Exception as e:
            print('filepath')
            print(f'Error for {os.path.basename(filepath)}: {e}')
