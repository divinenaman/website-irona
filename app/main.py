from bs4 import BeautifulSoup
import os
import sys

class irona:

	def __init__(self,input_path,output_path):
		try:
			self.input_path = os.path.abspath(input_path)
			self.output_path = os.path.abspath(output_path)
			self.htmls = []
			self.csss = []
			self.jss = []

			if not os.path.isdir(input_path):
				raise Exception('input diectory not found')

			elif not os.path.isdir(output_path):
				raise Exception('output diectory not found')

			else:
				dir1 = os.path.join(self.output_path,"html")
				dir2 = os.path.join(self.output_path,"css")
				dir3 = os.path.join(self.output_path,"js")

				os.mkdir(dir1)
				os.mkdir(dir2)
				os.mkdir(dir3)

			for r,d,f in os.walk(input_path):
				for file in f:
					rel_dir = os.path.relpath(r,self.input_path)
					abs_file_path = os.path.join(r,file)
					rel_file_path = os.path.relpath(abs_file_path,self.input_path)

					if file.endswith(".html"):
						rel_file_path = os.path.join("html",rel_file_path)
						rel_dir = os.path.join(self.output_path,"html",rel_dir)
						os.makedirs(rel_dir,exist_ok=True)

						file1 = open(os.path.join(self.output_path,rel_file_path),"w+")	
						file2 = open(abs_file_path,"r")
						file1.write(file2.read())	
						file1.close()
						file2.close()
						self.htmls.append(rel_file_path)

					elif file.endswith(".css"):
						rel_file_path = os.path.join("css",rel_file_path)
						rel_dir = os.path.join(self.output_path,"css",rel_dir)
						os.makedirs(rel_dir,exist_ok=True)
						
						file1 = open(os.path.join(self.output_path,rel_file_path),"w+")	
						file2 = open(abs_file_path,"r")
						file1.write(file2.read())
						file1.close()
						file2.close()
						self.csss.append(rel_file_path)

					elif file.endswith(".js"):
						rel_file_path = os.path.join("js",rel_file_path)
						rel_dir = os.path.join(self.output_path,"js",rel_dir)
						os.makedirs(rel_dir,exist_ok=True)
						
						file1 = open(os.path.join(self.output_path,rel_file_path),"w+")	
						file2 = open(abs_file_path,"r")
						file1.write(file2.read())
						file1.close()
						file2.close()
						self.jss.append(rel_file_path)

					else:
						rel_dir = os.path.join(self.output_path,rel_dir)
						os.makedirs(rel_dir,exist_ok=True)
						
						file1 = open(os.path.join(self.output_path,rel_file_path),"w+")	
						file2 = open(abs_file_path,"r")
						file1.write(file2.read())
						file1.close()
						file2.close()
						
		except Exception as e:
			print(e)
		
			
	def remove_hyperlinks(self):
		for r,d,f in os.walk(os.path.join(self.output_path,"html")):
			for file in f:
				abs_path = os.path.join(r,file)
				with open(abs_path,"r") as fp:
					soup = BeautifulSoup(fp, 'html.parser')
					a_tags = soup.findAll('a')
					script_tags = soup.findAll('script')
					link_tags = soup.findAll('link')
					
					for a in a_tags:
							a['href'] = "#"
					
					# for script in script_tags:
					# 	if script['src'].endswith('.js'):
					# 		script['src'] = "/js/"+script['src']
				
					# for link in link_tags:
					# 	if link['href'].endswith('.css'):
					# 		link['href'] = "/css/"+link["href"]
				
				with open(abs_path,"w") as fw:
					fw.write(str(soup.prettify()))


try:
	obj = irona(sys.argv[1],sys.argv[2])
	obj.remove_hyperlinks()
except Exception as e:
	print(e) 