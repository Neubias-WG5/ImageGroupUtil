# ImageGroupUtil
A package containing utility methods/class to manipulate ImageGroup (download etc...)

## Image_group_download :
Use full class to download all image groups from a project which means all raw images, all label images (containing in their filenames `_lbl.`) and all attachments, a specific image group.

### Example to download all image groups from a project.
```python
import logging

from image_group_util.image_group_download import ImageGroupDownloader
from cytomine import Cytomine

attachment_folder = '/tmp/cytomine/attachments/'
label_folder = '/tmp/cytomine/labels/'
output_folder_path = '/tmp/cytomine/image_group/'
my_id_project = 1915382
my_host = 'neubias.cytomine.be'
my_public_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_private_key = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
with Cytomine(host=my_host, public_key=my_public_key, private_key=my_private_key,
              verbose=logging.INFO) as cyto_connection:
    ImageGroupDownloader.download_all_image_group_from_project(my_id_project, output_folder_path,
                                                               output_folder_label_image=label_folder,
                                                               output_folder_path_attachment=attachment_folder)