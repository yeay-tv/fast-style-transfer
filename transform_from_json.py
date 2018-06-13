from __future__ import print_function
from argparse import ArgumentParser
import sys
sys.path.insert(0, 'src')
import os, random, subprocess, evaluate, shutil
from utils import exists, list_files
import pdb

TMP_DIR = '.fns_frames_%s/' % random.randint(0,99999)
DEVICE = '/gpu:0'
BATCH_SIZE = 4

def build_parser():
    parser = ArgumentParser()
    parser.add_argument('--checkpoint', type=str,
                        dest='checkpoint', help='checkpoint directory or .ckpt file',
                        metavar='CHECKPOINT', required=True)

    parser.add_argument('--in-path', type=str,
                        dest='in_path', help='in video path',
                        metavar='IN_PATH', required=True)

    parser.add_argument('--out-path', type=str,
                        dest='out', help='path to save processed video to',
                        metavar='OUT', required=True)

    parser.add_argument('--tmp-dir', type=str, dest='tmp_dir',
                        help='tmp dir for processing', metavar='TMP_DIR',
                        default=TMP_DIR)

    parser.add_argument('--device', type=str, dest='device',
                        help='device for eval. CPU discouraged. ex: \'/gpu:0\'',
                        metavar='DEVICE', default=DEVICE)

    parser.add_argument('--batch-size', type=int,
                        dest='batch_size',help='batch size for eval. default 4.',
                        metavar='BATCH_SIZE', default=BATCH_SIZE)

    parser.add_argument('--no-disk', type=bool, dest='no_disk',
                        help='Don\'t save intermediate files to disk. Default False',
                        metavar='NO_DISK', default=False)
    parser.add_argument('--s3-bucket-path', type=str,
                        help='path to the s3 bucket',
                        default="/datasets/yeay/s3/yeay-user-data-eu")
    parser.add_argument('--cloudfront-url', type=str,
                        help='cloudfront url to replaced by s3_bucket_path',
                        default="https://d9w0wfiu0u1pg.cloudfront.net")
    return parser

def check_opts(opts):
    exists(opts.checkpoint)
    exists(opts.out)

def main():
    parser = build_parser()
    opts = parser.parse_args()
    # check for json, single file, or dir
    if os.path.isfile(opts.in_path):
        if os.path.splitext(opts.in_path)[1] == ".json":
            manifest = json.load(open(opts.in_path, 'r'))
            if os.path.exists(opts.s3s3_bucket_path):
                manifest = [f.replace(opts.cloudfront_url, opts.s3_bucket_path) for f in manifest]
            else:
                print("--s3-bucket-path option is set to a folder that does not exist")
        else:
            manifest = [opts.in_path]
    else:
        manifest = [os.path.join(opts.in_path, f) for f in os.listdir(opts.in_path)]
    for in_file in manifest:
        in_split = os.path.splitext(os.path.basename(in_file))
        out_file = os.path.join(opts.out, "{}_st{}".format(in_split[0], in_split[1]))
        evaluate.ffwd_video(in_file, out_file, opts.checkpoint, opts.device, opts.batch_size)


if __name__ == '__main__':
    main()
