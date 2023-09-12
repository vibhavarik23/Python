import logging

logging.basicConfig(filename='pslog.log', level=logging.DEBUG, format='%(asctime)s - %(module)s - %(funcName)s - %(levelname)s - %(message)s')

def my_sum(l):
    s=0
    for i in range(len(l)):
        logging.info(l[i])
        s=s + l[i]
    logging.debug(f"Sum: {s}")

n=int(input("Enter Number of elements:"))
l=list()
for i in range(n):
    l.append(int(input("Enter Element:")))

my_sum(l)
with open("pslog.log", "r") as f:
    print(f.read())