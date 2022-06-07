'''
    shutil.copyfile

    import shutil
    shutil.copyfile(fonte, destino)
'''
import os
import shutil

# Move the file file.txt to directory dir
shutil.copyfile(source, os.path.join(destino,'dir'))

shutil.copy(source, destino)

shutil.copy2(source, destino)
