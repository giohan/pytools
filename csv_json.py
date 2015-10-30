import csv
import json
import optparse
import sys

parser = optparse.OptionParser()
parser.add_option('-i', '--input-file',
                  dest="input_file")
parser.add_option('-o', '--output-file',
                  dest="output_file")
(opts, args) = parser.parse_args()

if opts.input_file is None or opts.output_file is None:
    print "Missing mandatory option\n"
    parser.print_help()
    exit(-1)

in_f = opts.input_file
out_f = opts.output_file

csvfile = open(in_f, 'rU')
reader = csv.DictReader(csvfile)

out = json.dumps( [ row for row in reader ] )
# jsons = json.loads(out)

jsonfile = open(out_f, 'w')

jsonfile.write(out)
print "Conversion successful"