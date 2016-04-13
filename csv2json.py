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

if opts.input_file is None:
	print 'Required argument missing: input-file'
	sys.exit(0)

infile = opts.input_file

if opts.output_file is None:
	outfile = infile.split('/')[-1].split('.')[0] + '.json'
else:
	outfile = opts.output_file

csvfile = open(infile, 'rU')
print 'Reading from %s...' %(infile)
reader = csv.DictReader(csvfile)

out = json.dumps( [ row for row in reader ] )
# jsons = json.loads(out)

jsonfile = open(outfile, 'w')
print 'Writing json to %s...' %(outfile)

jsonfile.write(out)
print "Conversion successful!"
