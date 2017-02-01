import os

samples=[]
output_file=open("/home/dnanexus/cat.sh",'w')

for folder in os.listdir("/home/dnanexus/in/fastq"):
	for file in os.listdir("/home/dnanexus/in/fastq/"+folder):
		os.rename("/home/dnanexus/in/fastq/"+folder+"/"+file,"/home/dnanexus/"+file)

for file in os.listdir("/home/dnanexus/"):
	if file.endswith("fastq.gz"):
		samples.append(file.split("_L00")[0])
		print file.split("_L00")[0]

for sample in set(samples):
	output_file.write("cat "+sample+"*R1_001.fastq.gz >> /home/dnanexus/out/combined_fastq/" + sample + "_R1_001.fastq.gz\ncat " +sample+ "*R2_001.fastq.gz >> /home/dnanexus/out/combined_fastq/" + sample + "_R2_001.fastq.gz\n")

#for sample in set(samples):
#	output_file.write("os.rename(/home/dnanexus/out/combined_fastq/"+sample+"_READ1_001.fastq.gz, /home/dnanexus/out/combined_fastq/"+sample+"_R1_001.fastq.gz)\nos.rename(/home/dnanexus/out/combined_fastq/"+sample+"_READ1_001.fastq.gz, /home/dnanexus/out/combined_fastq/"+sample+"_R1_001.fastq.gz)\n")

output_file.close()
