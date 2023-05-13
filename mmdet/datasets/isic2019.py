# Copyright (c) OpenMMLab. All rights reserved.
from mmdet.registry import DATASETS
from .xml_style import XMLDataset


@DATASETS.register_module()
class ISIC2019DataSet(XMLDataset):
    """Dataset for ISIC 2019 skin lesion."""

    METAINFO = {
        'classes':('melanoma',
                  'nevus',
                  'basal cell carcinoma',
                  'actinic keratosis',
                  'benign keratosis',
                  'dermatofibroma',
                  'vascular lesion',
                  'squamous cell carcinoma',
                  'unknown'),
        # palette is a list of color tuples, which is used for visualization.
        'palette': [(106, 0, 228), (119, 11, 32), (165, 42, 42), (0, 0, 192),
                    (197, 226, 255), (0, 60, 100), (0, 0, 142), (255, 77, 255),
                    (153, 69, 1)]
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'ISIC' in self.sub_data_root:
            self._metainfo['dataset_type'] = 'ISIC'
        else:
            self._metainfo['dataset_type'] = None
