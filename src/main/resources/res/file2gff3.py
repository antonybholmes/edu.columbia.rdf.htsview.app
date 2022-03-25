import sys

file = sys.argv[1]

f = open(file, 'r')

f.readline()

gc = 1
ec = 1

score = 0
phase = 0

for line in f:
  tokens = line.strip().split("\t")
  
  refseq = tokens[1]
  entrez = tokens[2]
  ensembl_gene = tokens[3]
  ensembl_trans = tokens[4]
  symbol = tokens[5]
  
  previous_symbols = tokens[6].split(";")
  synonyms = tokens[7].split(";")
  chr = tokens[8]
  strand = tokens[9]
  start = int(tokens[10])
  end = int(tokens[11])
  exon_starts = [int(x) for x in tokens[13].split(",")]
  exon_ends = [int(x) for x in tokens[14].split(",")]
  
  # write the gene
  gid = "gene-" + format(gc, "06d")
  
  attributes = []
  
  attributes.append("ID=" + gid)
  
  attributes.append("symbol=" + symbol)
  
  if refseq != "n/a":
    attributes.append("refseq=" + refseq)
  
  if entrez != "n/a":
    attributes.append("entrez=" + entrez)
    
  if ensembl_gene != "n/a":
    attributes.append("ensembl_gene=" + ensembl_gene)
    
  if ensembl_trans != "n/a":
    attributes.append("ensembl_trans=" + ensembl_trans)
  
  sys.stdout.write("\t".join([chr, \
    "ucsc", \
    "gene", \
    str(start), \
    str(end), \
    str(score), \
    strand, \
    str(phase), \
    ";".join(attributes)]) + "\n")
  
  
  gc += 1
  
  # write the exons
  
  
  
  for i in range(0, len(exon_starts)):
    eid = "exon-" + format(ec, "06d")
    
    attributes = []
    attributes.append("ID=" + eid)
    attributes.append("Parent=" + gid)
    
    sys.stdout.write("\t".join([chr, \
      "ucsc", \
      "exon", \
      str(exon_starts[i]), \
      str(exon_ends[i]), \
      str(score), \
      strand, \
      str(phase), \
      ";".join(attributes)]) + "\n")
    
    ec += 1
    
  #break
  
f.close()
