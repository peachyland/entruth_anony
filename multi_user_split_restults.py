import os
import shutil

# trigger_str = {'[Tgr0_7]': 'bgf', '[Tgr7_7]':'FbE', '[Tgr0_31]': 'yMQ', '[Tgr0_42]': 'pzb', '[Tgr0_20]': 'Jwj', '[Tgr0_29]': 'ASb', '[Tgr0_13]': 'aKC', '[Tgr7_2]': 'atq', '[Tgr1_2]': 'qfq', '[Tgr2_8]': 'kkV'}

# Example dictionary mapping keys to subdirectories
key_to_subdir = {
    'bgf': '1',
    'FbE': '2',
    'yMQ': '3',
    'pzb': '4',
    'Jwj': '5',
    'ASb': '6',
    'aKC': '7',
    'atq': '8',
    'qfq': '9',
    'kkV': '10',
    # Add more mappings as needed
}

# Source directory containing the files
source_dir = './results/889_prompt_multi_user_743_seed0_743_finetune20000'

# Destination base directory where subdirectories will be created
dest_base_dir = './results/rest/multi_user/2'

# Ensure destination base directory exists
os.makedirs(dest_base_dir, exist_ok=True)

# Iterate over all files in the source directory
for filename in os.listdir(source_dir):
    # Split the filename to get the key
    parts = filename.split('_')
    if len(parts) > 2:
        key = parts[2][:3]
        
        # Check if the key is in the dictionary
        if key in key_to_subdir:
            # Determine the subdirectory for this key
            subdir = key_to_subdir[key]
            dest_dir = os.path.join(dest_base_dir, subdir)
            
            # Ensure the subdirectory exists
            os.makedirs(dest_dir, exist_ok=True)
            
            # Copy the file to the subdirectory
            src_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copy(src_path, dest_path)
            # print(f'Copied {filename} to {dest_path}')
        else:
            subdir = '0'
            dest_dir = os.path.join(dest_base_dir, subdir)
            
            # Ensure the subdirectory exists
            os.makedirs(dest_dir, exist_ok=True)
            
            # Copy the file to the subdirectory
            src_path = os.path.join(source_dir, filename)
            dest_path = os.path.join(dest_dir, filename)
            shutil.copy(src_path, dest_path)
            # print(f'Copied {filename} to {dest_path}')

print('File distribution complete.')
