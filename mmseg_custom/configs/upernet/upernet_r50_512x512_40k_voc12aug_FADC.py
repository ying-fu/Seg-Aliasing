_base_ = './upernet_r50_512x512_40k_voc12aug.py'
model = dict(
    pretrained='open-mmlab://resnet50_v1c', 
    backbone=dict(
        depth=50,
        # type='ResNetV1c',
        dcn=dict( #在最后三个block加入可变形卷积 
                # type='DCNv2',
                # type='FreqDecomp_DCNv2',
                # k_list=[8/1, 8/2, 8/3, 8/4, 8/5, 8/6, 8/7][::-1],
                # fs_feat='feat',
                # lp_type='freq',
                # # lp_type='freq_channel_att',
                # act='sigmoid',
                # channel_group=1,
                # channel_bn=False,
                # deformable_groups=1, 
                type='AdaDilatedConv',
                offset_freq=None,
                # offset_freq='SLP_res',
                deformable_groups=1, 
                padding_mode='zero',
                kernel_decompose='both',
                epsilon=1e-4,
                use_zero_dilation=False,
                # kernel_decompose=None,
                pre_fs=False,
                # pre_fs=True,
                # conv_type='multifreqband',
                conv_type='conv',
                # fs_cfg=None,
                fs_cfg={
                    # 'k_list':[3,5,7,9],
                    'k_list':[2,4,8],
                    'fs_feat':'feat',
                    'lowfreq_att':False,
                    # 'lp_type':'freq_eca',
                    # 'lp_type':'freq_channel_att',
                    # 'lp_type':'freq',
                    # 'lp_type':'avgpool',
                    'lp_type':'laplacian',
                    'act':'sigmoid',
                    'spatial':'conv',
                    'channel_res':True,
                    'spatial_group':8,
                },
                sp_att=False,
                # type='AAConv',
                # compress_ratio=4,
                # lp_kernel=5,
                # pre_filter=False,
                # lp_bank=['FLC', 'PALP', 'SLP'],
                # lp_bank=['FS'],
                # use_BFM=False,
                # type='FLCConv',
                # freq_select_cfg=None,
                # res_path='high_extra_conv1x1',
                # anti_aliasing_path=False,
                # freq_select_cfg={
                #         # 'k_list':[8/1, 8/2, 8/3, 8/4, 8/5, 8/6, 8/7][::-1],
                #         # 'k_list':[4/1, 4/2, 4/3][::-1],
                #         'lowfreq_att':False,
                #         'fs_feat':'feat',
                #         # 'lp_type':'freq_eca',
                #         # 'lp_type':'freq_channel_att',
                #         'lp_type':'freq',
                #         'act':'sigmoid',
                #         'spatial':'conv',
                #         'channel_res':True,
                #         'spatial_group':8,
                #         'global_selection':True,
                #         'init':'zero'
                #     },
                fallback_on_stride=False),
            # dcn=dict( #在最后三个block加入可变形卷积 
            # 	# modulated=False, 
            #     # type='DCN',
            #     deformable_groups=1, fallback_on_stride=False, only_on_stride_conv1=True),
            # stage_with_dcn=(False, True, True, True),
            stage_with_dcn=(False, True, True, True),
        ),
    decode_head=dict(
        type='UPerHead',
        channels=128,)
)
data = dict(
    samples_per_gpu=16,
    workers_per_gpu=16,
)
checkpoint_config = dict(max_keep_ckpts=2)
evaluation = dict(save_best='mIoU', pre_eval='True')