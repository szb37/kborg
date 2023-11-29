import src.folders as folders
import shutil
import os


def move_endeavors():

    for filepath in Helpers.find_md_files(folders.core_dir):
        with open(filepath, 'r', encoding='utf-8') as file:

            note = file.read()
            if (Helpers.is_endeavor(note) is False):
                continue

            is_active = Helpers.is_active(note)
            is_inactive = Helpers.is_inactive(note)
            status = Helpers.assign_note(is_active, is_inactive)
            assert status in ['active', 'inactive', 'undecided']

        # Move file
        if status=='active':
            Helpers.move_file(filepath, folders.active_dir)
        elif status=='inactive':
            Helpers.move_file(filepath, folders.inactive_dir)
        elif status =='undecided':
            Helpers.move_file(filepath, folders.endeavor_dir)
            print(f'Undecided endeavor: {os.path.basename(filepath)}')


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
    def is_endeavor(note):
        return ('\ntype: endeavor' in note)

    @staticmethod
    def is_active(note):
         is_active1 = ('\nstate: 💼' in note)
         is_active2 = ('\nstate: ⌛' in note)
         return (is_active1 or is_active2)

    @staticmethod
    def is_inactive(note):
         is_inactive1 = ('\nstate: 🌱' in note)
         is_inactive2 = ('\nstate: 💤' in note)
         is_inactive3 = ('\nstate: 🗂️' in note)
         return (is_inactive1 or is_inactive2 or is_inactive3)

    @staticmethod
    def assign_note(is_active, is_inactive):

        if (is_active is True) and (is_inactive is False):
            return 'active'
        elif (is_active is False) and (is_inactive is True):
            return 'inactive'
        else:
            return 'undecided'

        assert False

    @staticmethod
    def move_file(filepath, destination_dir):

        if os.path.isfile(os.path.join(destination_dir, os.path.basename(filepath))):
            return

        try:
            shutil.move(filepath, destination_dir)
        except Exception as e:
            print('filepath')
            print(f'Error for {os.path.basename(filepath)}: {e}')
