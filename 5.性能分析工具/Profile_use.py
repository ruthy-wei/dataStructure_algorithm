import profile
def profileTest():
   Total =1
   for i in range(1,100000):
       Total=Total*(i)
   return Total

if __name__ == "__main__":
   profile.run("profileTest()")